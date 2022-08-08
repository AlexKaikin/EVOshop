from apps.accounts.models import Profile


def get_email_validate(request):
    email = request.GET.get('email', None)
    return Profile.objects.filter(email__iexact=email).exists()
