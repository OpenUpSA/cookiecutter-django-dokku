from {{cookiecutter.project_slug}} import settings


def tag_manager_id(request):
    if settings.TAG_MANAGER_ENABLED:
        return {
            "TAG_MANAGER_ENABLED": settings.TAG_MANAGER_ENABLED,
            "TAG_MANAGER_CONTAINER_ID": settings.TAG_MANAGER_CONTAINER_ID
        }
    else:
        return dict()