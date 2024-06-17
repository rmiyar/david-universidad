from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def group_required(group_name):
    def in_group(user):
        if user.groups.filter(name=group_name).exists() or user.is_superuser:
            return True
        else:
            raise PermissionDenied

    return user_passes_test(in_group)
