import os
from pprint import  pprint

from locust import HttpUser, between, task, TaskSet
import urllib3

from helpers.json_helper import read_json
from helpers.auth_helper import AuthorizationHelper
from helpers.requests_helper import send_get_request, send_patch_request, send_post_request

urllib3.disable_warnings()

filepath = os.path.abspath("target.json")
target = read_json(filepath)

auth_helper = AuthorizationHelper()


class UserBehavior(TaskSet):

    def on_start(self):
        auth_helper.authorize(
            session=self.client,
            email=target["authorization"]["user"]["email"],
            password=target["authorization"]["user"]["password"],
            role="user"
        )
        self.client.headers.update({"Content-Type": "application/json"})

    # @task
    def get_article(self):
        endpoint = target["user"]["get_article"]["endpoint"]
        name = "/ARTICLE"
        filename = target["user"]["get_article"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_currencies(self):
        endpoint = target["user"]["get_currencies"]["endpoint"]
        name = "/CURRENCIES"
        filename = target["user"]["get_currencies"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_me(self):
        endpoint = target["user"]["get_me"]["endpoint"]
        name = "/ME"
        send_get_request(self.client, endpoint, name)

    # @task
    def get_modules(self):
        endpoint = target["user"]["get_modules"]["endpoint"]
        name = "/MODULES"
        send_get_request(self.client, endpoint, name)

    # @task   # 502
    def get_user_messages(self):
        endpoint = target["user"]["get_user_messages"]["endpoint"]
        name = "/USER MESSAGES"
        filename = target["user"]["get_user_messages"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_notifications_user_settings(self):
        endpoint = target["user"]["get_user_notifications_user_settings"]["endpoint"]
        name = "/USER NOTIFICATIONS USER SETTINGS"
        send_get_request(self.client, endpoint, name)

    # @task
    def get_user_own_cards(self):
        endpoint = target["user"]["get_user_own_cards"]["endpoint"]
        name = "/USER OWN CARDS"
        filename = target["user"]["get_user_own_cards"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_reports_balance(self):
        endpoint = target["user"]["get_user_reports_balance"]["endpoint"]
        name = "/USER REPORTS BALANCE"
        filename = target["user"]["get_user_reports_balance"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_requests(self):
        endpoint = target["user"]["get_user_requests"]["endpoint"]
        name = "/USER REQUESTS"
        filename = target["user"]["get_user_requests"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_transaction_by_id(self):
        endpoint = target["user"]["get_user_transaction_by_id"]["endpoint"]
        transaction_id = target["user"]["get_user_transaction_by_id"]["transaction_id"]
        endpoint += transaction_id
        name = "/USER TRANSACTIONS BY ID"
        filename = target["user"]["get_user_transaction_by_id"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_transactions(self):
        endpoint = target["user"]["get_user_transactions"]["endpoint"]
        name = "/USER TRANSACTIONS"
        filename = target["user"]["get_user_transactions"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   # 403
    def post_cft_request(self):
        endpoint = target["user"]["post_cft_request"]["endpoint"]
        name = "/CFT REQUEST"
        filename = target["user"]["post_cft_request"]["filename"]
        rs = send_post_request(self.client, endpoint, name, filename)
        pprint(rs)

    # @task   # 403
    def post_cft_request_preview(self):
        endpoint = target["user"]["post_cft_request_preview"]["endpoint"]
        name = "/CFT REQUEST PREVIEW"
        filename = target["user"]["post_cft_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task   # дописать
    def post_owt_request(self):
        endpoint = target["user"]["post_owt_request"]["endpoint"]
        name = "/OWT REQUEST"
        filename = target["user"]["post_owt_request"]["filename"]
        rs = send_post_request(self.client, endpoint, name, filename)
        pprint(rs)

    # @task   # дописать
    def post_owt_request_preview(self):
        pass

    # @task   # дописать
    def post_tba_request(self):
        pass

    # @task   # дописать
    def post_tba_request_preview(self):
        pass

    # @task   # дописать
    def post_tbu_request(self):
        pass

    # @task   # дописать
    def post_tbu_request_preview(self):
        pass

    # @task   # 502
    def post_user_messages(self):
        endpoint = target["user"]["post_user_messages"]["endpoint"]
        name = "/USER MESSAGES"
        filename = target["user"]["post_user_messages"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task   # 400
    def get_user_reports_account_export(self):
        endpoint = target["user"]["get_user_reports_account_export"]["endpoint"]
        name = "/USER REPORTS ACCOUNT EXPORT"
        filename = target["user"]["get_user_reports_account_export"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_reports_balance_export(self):
        endpoint = target["user"]["get_user_reports_balance_export"]["endpoint"]
        name = "/USER REPORTS BALANCE EXPORT"
        send_get_request(self.client, endpoint, name)

    # @task
    def get_user_reports_transaction_export(self):
        endpoint = target["user"]["get_user_reports_transaction_export"]["endpoint"]
        name = "/USER REPORTS TRANSACTION EXPORT"
        filename = target["user"]["get_user_reports_transaction_export"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_reports_transaction(self):
        endpoint = target["user"]["get_user_reports_transaction"]["endpoint"]
        name = "/USER REPORTS TRANSACTION"
        filename = target["user"]["get_user_reports_transaction"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # 1 не хватает


class LoadTestUser(HttpUser):
    wait_time = between(1, 2)
    host = target["host"]

    tasks = [UserBehavior]
