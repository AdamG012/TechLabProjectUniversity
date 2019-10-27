from django.contrib.auth.models import User


def create_user(username, password, firstname, lastname, email):

    u, created = User.objects.get_or_create(username=username)
    u.set_password(password)
    u.email = email
    u.first_name = firstname
    u.last_name = lastname
    u.save()
