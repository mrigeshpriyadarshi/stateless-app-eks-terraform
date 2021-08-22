"""Unit test file for app.py"""
import unittest
from app import app
 
class TestApp(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
     
    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
     
    # executed after each test
    def tearDown(self):
        pass
     
    ###############
    #### tests ####
    ###############
     
    def test_main_page(self):
        response = self.app.get('/api/v1/connect', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
if __name__ == "__main__":
    unittest.main()