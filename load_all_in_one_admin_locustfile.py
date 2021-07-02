import os
from pprint import pprint

from locust import HttpUser, between, task, TaskSet
import urllib3

from helpers.json_helper import read_json
from helpers.auth_helper import AuthorizationHelper
from helpers.requests_helper import send_get_request, send_patch_request, send_post_request

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

    # @task
    def get_system_maturity(self):
        endpoint = target["admin"]["get_system_maturity"]["endpoint"]
        name = "/SYSTEM MATURITY"
        filename = target["admin"]["get_system_maturity"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   ## 504
    def get_system_overview_export(self):
        endpoint = target["admin"]["get_system_overview_export"]["endpoint"]
        name = "/SYSTEM OVERVIEW EXPORT"
        send_get_request(self.client, endpoint, name)

    # @task   ## 504
    def get_system_overview(self):
        endpoint = target["admin"]["get_system_overview"]["endpoint"]
        name = "/SYSTEM OVERVIEW"
        filename = target["admin"]["get_system_overview"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   ## 500
    def patch_request_by_id(self):
        endpoint = target["admin"]["patch_request_by_id"]["endpoint"]
        request_id = target["admin"]["patch_request_by_id"]["request_id"]
        endpoint += request_id
        name = "/REQUEST BY ID"
        filename = target["admin"]["patch_request_by_id"]["filename"]
        send_patch_request(self.client, endpoint, name, filename)

    # @task
    def post_owt_request(self):
        endpoint = target["admin"]["post_owt_request"]["endpoint"]
        user_id = target["authorization"]["user"]["user_id"]
        endpoint += user_id
        name = "/OWT REQUEST"
        filename = target["admin"]["post_owt_request"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def get_user_sort(self):
        endpoint = target["admin"]["get_user_sort"]["endpoint"]
        name = "/USER SORT"
        filename = target["admin"]["get_user_sort"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task
    def get_request_by_id(self):
        endpoint = target["admin"]["get_request_by_id"]["endpoint"]
        request_id = target["admin"]["get_request_by_id"]["request_id"]
        endpoint += request_id
        name = "/REQUEST BY ID"
        rs = send_get_request(self.client, endpoint, name)
        pprint(rs)

    # @task
    def post_owt_request_preview(self):
        endpoint = target["admin"]["post_owt_request_preview"]["endpoint"]
        user_id = target["authorization"]["user"]["user_id"]
        endpoint += user_id
        name = "/OWT REQUEST PREVIEW"
        filename = target["admin"]["post_owt_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_tba_request(self):
        endpoint = target["admin"]["post_tba_request"]["endpoint"]
        user_id = target["authorization"]["user"]["user_id"]
        endpoint += user_id
        name = "/TBA REQUEST"
        filename = target["admin"]["post_tba_request"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_tba_request_preview(self):
        endpoint = target["admin"]["post_tba_request_preview"]["endpoint"]
        user_id = target["authorization"]["user"]["user_id"]
        endpoint += user_id
        name = "/TBA REQUEST PREVIEW"
        filename = target["admin"]["post_tba_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_tbu_request(self):
        endpoint = target["admin"]["post_tbu_request"]["endpoint"]
        user_id = target["authorization"]["user"]["user_id"]
        endpoint += user_id
        name = "/TBU REQUEST"
        filename = target["admin"]["post_tbu_request"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_tbu_request_preview(self):
        endpoint = target["admin"]["post_tbu_request_preview"]["endpoint"]
        user_id = target["authorization"]["user"]["user_id"]
        endpoint += user_id
        name = "/TBU REQUEST PREVIEW"
        filename = target["admin"]["post_tbu_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_ca_request(self):
        endpoint = target["admin"]["post_ca_request"]["endpoint"]
        name = "/CA REQUEST"
        filename = target["admin"]["post_ca_request"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_ca_request_preview(self):
        endpoint = target["admin"]["post_ca_request_preview"]["endpoint"]
        name = "/CA REQUEST PREVIEW"
        filename = target["admin"]["post_ca_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_da_request(self):
        endpoint = target["admin"]["post_da_request"]["endpoint"]
        name = "/DA REQUEST"
        filename = target["admin"]["post_da_request"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_da_request_preview(self):
        endpoint = target["admin"]["post_da_request_preview"]["endpoint"]
        name = "/DA REQUEST PREVIEW"
        filename = target["admin"]["post_da_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_dra_request(self):
        endpoint = target["admin"]["post_dra_request"]["endpoint"]
        name = "/DRA REQUEST"
        filename = target["admin"]["post_dra_request"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task
    def post_dra_request_preview(self):
        endpoint = target["admin"]["post_dra_request_preview"]["endpoint"]
        name = "/DRA REQUEST PREVIEW"
        filename = target["admin"]["post_dra_request_preview"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task   # 502
    def post_messages_send_to_all(self):
        endpoint = target["admin"]["post_messages_send_to_all"]["endpoint"]
        name = "/MESSAGES SENT TO ALL"
        filename = target["admin"]["post_messages_send_to_all"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task   # 502
    def post_messages_send_to_group(self):
        endpoint = target["admin"]["post_messages_send_to_group"]["endpoint"]
        name = "/MESSAGES SENT TO GROUP"
        filename = target["admin"]["post_messages_send_to_group"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task  # 502
    def post_messages_send_to_users(self):
        endpoint = target["admin"]["post_messages_send_to_users"]["endpoint"]
        name = "/MESSAGES SENT TO USERS"
        filename = target["admin"]["post_messages_send_to_users"]["filename"]
        send_post_request(self.client, endpoint, name, filename)

    # @task   # 0
    def get_transfer_requests_export(self):
        endpoint = target["admin"]["get_transfer_requests_export"]["endpoint"]
        name = "/TRANSFER REQUESTS EXPORT"
        filename = target["admin"]["get_transfer_requests_export"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   # 400
    def get_transactions_export(self):
        endpoint = target["admin"]["get_transactions_export"]["endpoint"]
        name = "/TRANSACTIONS EXPORT"
        filename = target["admin"]["get_transactions_export"]["filename"]
        send_get_request(self.client, endpoint, name, filename)

    # @task   # 500
    def get_reports_transaction(self):
        endpoint = target["admin"]["get_reports_transaction"]["endpoint"]
        name = "/TRANSACTIONS REPORT"
        filename = target["admin"]["get_reports_transaction"]["filename"]
        rs = send_get_request(self.client, endpoint, name, filename)
        pprint(rs)


class LoadTestUser(HttpUser):
    wait_time = between(1, 2)
    host = target["host"]

    tasks = [AdminBehavior]
