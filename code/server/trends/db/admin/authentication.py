from django.contrib import auth


def login(request, username, password):
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return True
    return False


def logout(request):
    auth.logout(request)
