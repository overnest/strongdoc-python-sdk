#
# All Rights Reserved 2020
#

from datetime import datetime, timedelta, timezone
from time import sleep
from os import path
import io
import unittest

from strongdoc.api import account, billing, document, login, search 

PASSWORD = "password"
ADDRESS = "123 Street"

ORG1_NAME = "testingorg1"
ORG1_USER_NAME = "admin"
ORG1_EMAIL = "admin@"+ORG1_NAME+".com"
ORG1_SUB_TYPE = "Test Active"

ORG2_NAME = "testingorg2"
ORG2_USER_NAME = "admin"
ORG2_EMAIL = "admin@"+ORG2_NAME+".com"
ORG2_SUB_TYPE = "Test Active"

NEW_USER_NAME = "newuser"
NEW_USER_EMAIL = "newuser@email.com"

DOC_PATH = "test-data/BedMounts.pdf"
DOC_NAME = "BedMounts.pdf"
DOC_SEARCH_QUERY = "bed mounts"

class TestSDK(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Register Organizations
        cls.org1_id, cls.org1_adminid = account._register_organization(ORG1_NAME, ORG1_EMAIL, ADDRESS, ORG1_USER_NAME, 
            PASSWORD, ORG1_EMAIL, ORG1_SUB_TYPE, "")
        cls.org2_id, cls.org2_adminid = account._register_organization(ORG2_NAME, ORG2_EMAIL, ADDRESS, ORG2_USER_NAME, 
            PASSWORD, ORG2_EMAIL, ORG2_SUB_TYPE, "")
        
        # Login
        cls.org1_token = login.login(cls.org1_adminid, PASSWORD, cls.org1_id)
        cls.org2_token = login.login(cls.org2_adminid, PASSWORD, cls.org2_id)

    @classmethod
    def tearDownClass(cls):
        # Remove Organizations
        assert account.remove_organization(cls.org1_token, True)
        assert account.remove_organization(cls.org2_token, True)

    def test_get_account_info(self):
        account_info = account.get_account_info(TestSDK.org1_token)

        self.assertEqual(account_info.orgid, TestSDK.org1_id)

        self.assertEqual(account_info.subscription.type, ORG1_SUB_TYPE)
        self.assertEqual(account_info.subscription.status, "Subscribed")
        
        self.assertTrue(isinstance(account_info.payments[0].billed_at, datetime))
        self.assertTrue(isinstance(account_info.payments[0].period_start, datetime))
        self.assertTrue(isinstance(account_info.payments[0].period_end, datetime))
        self.assertTrue(isinstance(account_info.payments[0].amount, float))
        self.assertTrue(isinstance(account_info.payments[0].status, str))

        self.assertEqual(account_info.org_email, ORG1_EMAIL)
        self.assertEqual(account_info.org_address, ADDRESS)
        self.assertTrue(isinstance(account_info.multilevel_sharing, bool))
        self.assertTrue(isinstance(account_info.sharable_orgs, list))

    def test_set_account_info(self):
        new_email = "testorgchange@website.com"
        new_address = "123 Test St."

        success = account.set_account_info(TestSDK.org1_token, new_email, new_address)

        self.assertTrue(success)

        account_info = account.get_account_info(TestSDK.org1_token)

        self.assertEqual(account_info.org_email, new_email)
        self.assertEqual(account_info.org_address, new_address)

        self.assertTrue(account.set_account_info(TestSDK.org1_token, ORG1_EMAIL, ADDRESS))

    def test_get_user_info(self):
        user_info = account.get_user_info(TestSDK.org1_token)

        self.assertEqual(user_info.email, ORG1_EMAIL)
        self.assertEqual(user_info.name, ORG1_USER_NAME)
        self.assertTrue(user_info.is_admin)
        self.assertEqual(user_info.userid, TestSDK.org1_adminid)
        self.assertEqual(user_info.orgid, TestSDK.org1_id)

    def test_set_user_info(self):
        new_name = "NewUserName"
        new_email = "testuserchange@website.com"

        success = account.set_user_info(TestSDK.org1_token, new_name, new_email)

        self.assertTrue(success)

        user_info = account.get_user_info(TestSDK.org1_token)

        self.assertEqual(user_info.name, new_name)
        self.assertEqual(user_info.email, new_email)

        self.assertTrue(account.set_user_info(TestSDK.org1_token, ORG1_USER_NAME, ORG1_EMAIL))

    def test_change_user_password(self):
        new_password = "NewPassword"

        self.assertTrue(account.change_user_password(TestSDK.org1_token, PASSWORD, new_password))

        self.assertTrue(account.change_user_password(TestSDK.org1_token, new_password, PASSWORD))

    def test_register_remove_promote_demote_user(self):
        new_user_id = account.register_user(TestSDK.org1_token, NEW_USER_NAME, PASSWORD, NEW_USER_EMAIL, False)
        
        self.assertTrue(account.promote_user(TestSDK.org1_token, new_user_id))
        self.assertTrue(account.demote_user(TestSDK.org1_token, new_user_id))

        self.assertTrue(account.remove_user(TestSDK.org1_token, new_user_id))

    def test_list_users(self):
        users = account.list_users(TestSDK.org1_token)
        
        self.assertEqual(users[0].name, ORG1_USER_NAME)
        self.assertEqual(users[0].userid, TestSDK.org1_adminid)
        self.assertTrue(users[0].is_admin)

    def test_logout(self):
        self.assertTrue(login.logout(TestSDK.org1_token))
        sleep(1)
        TestSDK.org1_token = login.login(TestSDK.org1_adminid, "password", TestSDK.org1_id)

    def test_test(self):
        self.assertTrue(True)

    def test_sharing(self):
        with open(DOC_PATH, "rb") as f:
            docid = document.upload_document(TestSDK.org1_token, DOC_NAME, f)
        
        self.assertTrue(account.set_multilevel_sharing(TestSDK.org1_token, True))
        self.assertTrue(account.add_sharable_org(TestSDK.org1_token, TestSDK.org2_id))

        self.assertTrue(document.share_document(TestSDK.org1_token, docid, TestSDK.org2_adminid))
        self.assertTrue(document.unshare_document(TestSDK.org1_token, docid, TestSDK.org2_adminid))

        self.assertTrue(account.remove_sharable_org(TestSDK.org1_token, TestSDK.org2_id))
        self.assertTrue(account.set_multilevel_sharing(TestSDK.org1_token, False))

        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

    def test_search(self):
        with open(DOC_PATH, "rb") as f:
            docid = document.upload_document(TestSDK.org1_token, DOC_NAME, f)

        results = search.search(TestSDK.org1_token, DOC_SEARCH_QUERY)

        self.assertEqual(results[0].docid, docid)
        self.assertTrue(isinstance(results[0].score, float))

        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

    def check_billing_frequency(self, billing_frequency):
        self.assertIn(billing_frequency.frequency, billing._TimeInterval.__members__)
        self.assertTrue(isinstance(billing_frequency.valid_from, datetime))
        self.assertTrue(isinstance(billing_frequency.valid_to, datetime))

    def test_get_billing_details(self):
        response = billing.get_billing_details(TestSDK.org1_token)

        self.assertTrue(isinstance(response.period_start, datetime))
        self.assertTrue(isinstance(response.period_end, datetime))
        self.assertTrue(isinstance(response.total_cost, float))

        self.assertTrue(isinstance(response.documents.cost, float))
        self.assertTrue(isinstance(response.documents.size, float))
        self.assertTrue(isinstance(response.documents.tier, str))

        self.assertTrue(isinstance(response.search.cost, float))
        self.assertTrue(isinstance(response.search.size, float))
        self.assertTrue(isinstance(response.search.tier, str))

        self.assertTrue(isinstance(response.traffic.cost, float))
        self.assertTrue(isinstance(response.traffic.incoming, float))
        self.assertTrue(isinstance(response.traffic.outgoing, float))
        self.assertTrue(isinstance(response.traffic.tier, str))

        self.check_billing_frequency(response.billing_frequency)
    
    """
    def test_get_billing_frequency_list(self):
        response = billing.get_billing_frequency_list(TestSDK.org1_token)

        self.check_billing_frequency(response[0])
    """

    """
    def test_set_next_billing_frequency(self):
        new_time = datetime.utcnow() + timedelta(days=30)
        new_time = datetime(new_time.year, new_time.month, 1, tzinfo=timezone.utc)

        billing_frequency = billing.set_next_billing_frequency(TestSDK.org1_token, billing.FREQ_YEARLY, new_time)
        self.check_billing_frequency(billing_frequency)

        billing_frequency = billing.set_next_billing_frequency(TestSDK.org1_token, billing.FREQ_MONTHLY, new_time)
        self.check_billing_frequency(billing_frequency)
    """

    def test_get_large_traffic(self):
        response = billing.get_large_traffic(TestSDK.org1_token)

        self.assertTrue(isinstance(response.period_end, datetime))
        self.assertTrue(isinstance(response.period_start, datetime))

        self.assertTrue(isinstance(response.large_traffic_list[0].time, datetime))
        self.assertEqual(response.large_traffic_list[0].userid, TestSDK.org1_adminid)
        self.assertTrue(isinstance(response.large_traffic_list[0].method, str))
        self.assertTrue(isinstance(response.large_traffic_list[0].uri, str))
        self.assertTrue(isinstance(response.large_traffic_list[0].incoming, float))
        self.assertTrue(isinstance(response.large_traffic_list[0].outgoing, float))

    def test_upload_download(self):
        with open(DOC_PATH, "rb") as f:
            doc_bytes = f.read()

        with open(DOC_PATH, "rb") as f:
            docid = document.upload_document(TestSDK.org1_token, DOC_NAME, f)

        down_bytes = document.download_document(TestSDK.org1_token, docid)
        self.assertEqual(doc_bytes, down_bytes)
        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

        docid = document.upload_document(TestSDK.org1_token, DOC_NAME, doc_bytes)

        down_bytes = document.download_document(TestSDK.org1_token, docid)
        self.assertEqual(doc_bytes, down_bytes)

        output_stream = io.BytesIO()
        document.download_document_stream(TestSDK.org1_token, docid, output_stream)
        self.assertEqual(doc_bytes, output_stream.getvalue())
        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

    def test_encrypt_decrypt(self):
        with open(DOC_PATH, "rb") as f:
            doc_bytes = f.read()

        # Encrypt bytes to bytes
        docid, ciphertext = document.encrypt_document(TestSDK.org1_token, DOC_NAME, doc_bytes)

        # Decrypt bytes to bytes
        plaintext = document.decrypt_document(TestSDK.org1_token, docid, ciphertext)

        self.assertEqual(doc_bytes, plaintext)
        
        # Decrypt stream bytes to io.BufferedIOBase
        plaintext_stream = io.BytesIO()
        document.decrypt_document_stream(TestSDK.org1_token, docid, ciphertext, plaintext_stream)
        self.assertEqual(doc_bytes, plaintext_stream.getvalue())

        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

        # Encrypt io.BufferedIOBase to bytes
        with open(DOC_PATH, "rb") as f:
            docid, ciphertext = document.encrypt_document(TestSDK.org1_token, DOC_NAME, f)
        plaintext = document.decrypt_document(TestSDK.org1_token, docid, ciphertext)

        self.assertEqual(doc_bytes, plaintext)

        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

        # Encrypt stream bytes to io.BufferedIOBase
        ciphertext_stream = io.BytesIO()
        docid = document.encrypt_document_stream(TestSDK.org1_token, DOC_NAME, doc_bytes, ciphertext_stream)

        ciphertext_stream.seek(0)
        plaintext = document.decrypt_document(TestSDK.org1_token, docid, ciphertext_stream.getvalue())

        self.assertEqual(doc_bytes, plaintext)

        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

        # Encrypt stream io.BufferedIOBase to io.BufferedIOBase
        ciphertext_stream = io.BytesIO()
        with open(DOC_PATH, "rb") as f:
            docid = document.encrypt_document_stream(TestSDK.org1_token, DOC_NAME, f, ciphertext_stream)
        ciphertext_stream.seek(0)

        # Decrypt stream io.BufferedIOBase to io.BufferedIOBase
        plaintext_stream = io.BytesIO()
        document.decrypt_document_stream(TestSDK.org1_token, docid, ciphertext_stream, plaintext_stream)

        self.assertEqual(doc_bytes, plaintext_stream.getvalue())

        self.assertTrue(document.remove_document(TestSDK.org1_token, docid))

if __name__ == '__main__':
    unittest.main()
