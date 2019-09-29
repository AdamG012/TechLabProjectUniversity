import unittest
import trends.db.admin.authentication as auth;


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
        self.assertFalse(auth.login("clintbot", None, "fakePassword"))

    def test_invalid_login_unknown_username(self):
        self.assertFalse(auth.login("fakeUser", None, "password"))


if __name__ == '__main__':
    unittest.main()
