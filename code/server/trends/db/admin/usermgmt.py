from django.contrib.auth.models import User


def create_user(username, password, firstname, lastname, email):
    u = User.objects.get(username, email, password)
    u.first_name = firstname
    u.last_name = lastname
    u.save()
