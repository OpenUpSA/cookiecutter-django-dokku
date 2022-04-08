from base64 import b64encode
from random import randint

from django.conf import settings


def tag_manager_id(request):
    return {
        "TAG_MANAGER_ID": settings.TAG_MANAGER_ID,
        "TAG_MANAGER_SCRIPT_NONCE": b64encode(
            str(randint(10 ** 10, 10 ** 11)).encode()
        ).decode(),
    }