from django.conf import settings


def tag_manager_id(request):
    return {
        "TAG_MANAGER_ID": settings.TAG_MANAGER_ID
    }