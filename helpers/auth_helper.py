import json
import os

from helpers.assertion_helper import assert_status_code
from helpers.json_helper import read_json

filepath = os.path.abspath("target.json")
target = read_json(filepath)


class AuthorizationHelper:
    tokens = {"user": None, "admin": None}
    cookies = {"user": None, "admin": None}

    def authorize(self, session, email, password, role):
        if self.tokens[role]:
            session.headers.update({
                "Authorization": f"Bearer {self.tokens[role]}",
                "Cookie": f"token_signature={self.cookies[role]}"
            })
        else:
            session.headers.update({"Content-Type": "application/json"})

            data = {
                "data": {
                    "email": email,
                    "password": password
                }
            }
            with session.post(target["authorization"]["host"],
                              data=json.dumps(data),
                              name=f"/SIGN IN {role.upper()}",
                              verify=False,
                              catch_response=True) as response:
                assert_status_code(response)
                rs_json = response.json()
            if not rs_json["data"]["accessToken"]:
                response.failure("No authorization token found in response")
            else:
                token = rs_json["data"]["accessToken"]
                cookie = response.cookies.get("token_signature")
                self.tokens[role] = token
                self.cookies[role] = cookie
                session.headers.update({
                    "Authorization": f"Bearer {token}",
                    "Cookie": f"token_signature={cookie}"
                })
                response.success()
