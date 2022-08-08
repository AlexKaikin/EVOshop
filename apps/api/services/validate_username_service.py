from apps.accounts.models import Profile


def get_username_validate(request):
    username = request.GET.get('username', None)
    return Profile.objects.filter(username__iexact=username).exists()
