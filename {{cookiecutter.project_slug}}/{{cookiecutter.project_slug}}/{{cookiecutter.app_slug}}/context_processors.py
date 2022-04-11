from django.conf import settings


def tag_manager_id(request):
    print(settings.TAG_MANAGER_CONTAINER_ID)
    return {
        "TAG_MANAGER_ENABLED": settings.TAG_MANAGER_ENABLED,
        "TAG_MANAGER_CONTAINER_ID": settings.TAG_MANAGER_CONTAINER_ID
    }