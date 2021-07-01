import os
from pprint import pprint

from locust import HttpUser, between, task, TaskSet
import urllib3

from helpers.json_helper import read_json
from helpers.auth_helper import AuthorizationHelper
from helpers.requests_helper import send_get_request

urllib3.disable_warnings()

filepath = os.path.abspath("target.json")
target = read_json(filepath)

auth_helper = AuthorizationHelper()


class AdminBehavior(TaskSet):

    def on_start(self):
        auth_helper.authorize(
            session=self.client,
            email=target["authorization"]["admin"]["email"],
            password=target["authorization"]["admin"]["password"],
            role="admin"
        )
        self.client.headers.update({"Content-Type": "application/json"})

    # @task
    def get_accounts(self):
        endpoint = target["admin"]["get_accounts"]["endpoint"]
        name = "/ACCOUNTS"
        filename = target["admin"]["get_accounts"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_account_by_id(self):
        endpoint = target["admin"]["get_account_by_id"]["endpoint"]
        account_id = target["admin"]["get_account_by_id"]["account_id"]
        endpoint += account_id
        name = "/ACCOUNT BY ID"
        send_get_request(self.client, endpoint, name)

    # @task
    def get_admin_group(self):
        endpoint = target["admin"]["get_admin_group"]["endpoint"]
        name = "ADMIN GROUP"
        send_get_request(self.client, endpoint, name)

    # @task
    def get_admin_messages(self):
        endpoint = target["admin"]["get_admin_messages"]["endpoint"]
        name = "/ADMIN MESSAGES"
        filename = target["admin"]["get_admin_messages"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_permission(self):
        endpoint = target["admin"]["get_permission"]["endpoint"]
        name = "/PERMISSION"
        filename = target["admin"]["get_permission"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_requests(self):
        endpoint = target["admin"]["get_requests"]["endpoint"]
        name = "/REQUESTS"
        filename = target["admin"]["get_requests"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_cards(self):
        endpoint = target["admin"]["get_cards"]["endpoint"]
        name = "/CARDS"
        filename = target["admin"]["get_cards"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_registration_requests(self):
        endpoint = target["admin"]["get_registration_requests"]["endpoint"]
        name = "/REGISTRATION REQUESTS"
        filename = target["admin"]["get_registration_requests"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_revenue_accounts(self):
        endpoint = target["admin"]["get_revenue_accounts"]["endpoint"]
        name = "/REVENUE ACCOUNTS"
        filename = target["admin"]["get_revenue_accounts"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_user_groups(self):
        endpoint = target["admin"]["get_user_groups"]["endpoint"]
        name = "/USER GROUPS"
        filename = target["admin"]["get_user_groups"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_short_users(self):
        endpoint = target["admin"]["get_short_users"]["endpoint"]
        name = "/SHORT USERS"
        filename = target["admin"]["get_short_users"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   ## 502
    def get_reports_interests_export(self):
        endpoint = target["admin"]["get_reports_interests_export"]["endpoint"]
        name = "/REPORTS INTERESTS EXPORT"
        send_get_request(self.client, endpoint, name)

    # @task   ## 502
    def get_reports_interests(self):
        endpoint = target["admin"]["get_reports_interests"]["endpoint"]
        name = "/REPORTS INTERESTS"
        filename = target["admin"]["get_reports_interests"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   ## 502
    def get_system_balance_export(self):
        endpoint = target["admin"]["get_system_balance_export"]["endpoint"]
        name = "/SYSTEM BALANCE EXPORT"
        send_get_request(self.client, endpoint, name)

    # @task   ## 504, 502
    def get_system_balance(self):
        endpoint = target["admin"]["get_system_balance"]["endpoint"]
        name = "/SYSTEM BALANCE"
        filename = target["admin"]["get_system_balance"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   ## 502
    def get_system_manual_transaction(self):
        endpoint = target["admin"]["get_system_manual_transaction"]["endpoint"]
        name = "/SYSTEM MANUAL TRANSACTION"
        filename = target["admin"]["get_system_manual_transaction"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   ## 502
    def get_system_maturity_export(self):
        endpoint = target["admin"]["get_system_maturity_export"]["endpoint"]
        name = "/SYSTEM MATURITY EXPORT"
        send_get_request(self.client, endpoint, name)


class LoadTestUser(HttpUser):
    wait_time = between(1, 2)
    host = target["host"]

    tasks = [AdminBehavior]
