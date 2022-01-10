from .models import Profile

def create_profile(user, **kwargs):
    if Profile.objects.filter(user=user).exists():
        pass
    else:
        new_profile = Profile(user=user)
        new_profile.save()
    return kwargs

def cleanup_social_account(backend, uid, user=None, *args, **kwargs):
    """
    3rd party: python-social-auth.

    Social auth pipeline to cleanup the user's data.  Must be placed
    after 'social_core.pipeline.user.create_user'.
    """

    # Check if the user object exists and a new account was just created.
    if user and kwargs.get('is_new', False):
        user.your_name = kwargs['details']['first_name']
        user.is_staff = False
        user.is_superuser = False
        user.save()

    return {'user': user}


