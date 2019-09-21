import unittest
import code.server.trends.db.admin.authentication as auth;


class MyTestCase(unittest.TestCase):

    def test_invalid_login_none(self):
        self.assertFalse(auth.login(None, None, None))

    def test_invalid_login_none_username(self):
        self.assertFalse(auth.login("Hello", None, "password"))

    def test_invalid_login_none_password(self):
        self.assertFalse(auth.login("Hello", None, "password"))

    def test_invalid_login_none_request(self):
        self.assertFalse(auth.login("Hello", None, "password"))

    def test_invalid_login_wrong_password(self):
        self.assertFalse()

    def test_invalid_login_unknown_username(self):
        self.assertFalse()

    def test_valid_login(self):
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()
