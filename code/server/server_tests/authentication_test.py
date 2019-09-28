from django.test import TestCase, tag
from unittest import TestCase
from code.server.trends.db.admin.authentication import login, logout

#           Authentication

# - Testing for login and logout
# - Determining functionality proper authentication of users.
# - To run all these tests use:
#       python manage.py test server
# - To run these tests specifically as unit tests e.g. run by tag.
#       python manage.py test server --tag=unit


class Authentication(TestCase):

    @tag('unit', 'auth')
    def test_invalid_login_none(self):
        self.assertFalse(login(None, None, None))

    @tag('unit', 'auth')
    def test_invalid_login_none_username(self):
        self.assertFalse(login("Hello", None, "password"))

    @tag('unit', 'auth')
    def test_invalid_login_none_password(self):
        self.assertFalse(login("Hello", "user", None))

    @tag('unit', 'auth')
    def test_invalid_login_none_request(self):
        self.assertFalse(login(None, "user", "password"))

    @tag('unit', 'auth')
    def test_invalid_login_wrong_password(self):
        self.assertFalse(login("clintbot", "user", "fakePassword"))

    @tag('unit', 'auth')
    def test_invalid_login_unknown_username(self):
        self.assertFalse(login("fakeUser", "user1", "password"))

    @tag('unit', 'auth')
    def test_invalid_logout_none(self):
        self.assertFalse(logout(None))

    @tag('unit', 'auth')
    def test_invalid_logout_already_logged_in(self):
        self.assertFalse(logout("Hello"))

    @tag('unit', 'auth')
    def test_valid_logout(self):
        self.assertTrue(logout("fakeUser"))
