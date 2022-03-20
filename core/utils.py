import base64
from datetime import datetime, timezone
from user.models import UserIp
from django.core.files.base import ContentFile
from django.utils.text import get_valid_filename, slugify
from django.db import models


def set_user_ip(request):
    ip = None
    user = request.user
    if request.META.get("HTTP_X_FORWARDED_FOR"):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    if user.is_authenticated:
        UserIp.objects.update_or_create(user=user, ip_address=ip)

def generate_file_and_name(image_data: str, user_id: int):
    """
    This method is used to generate a file name for the profile photo.
    """
    current_timestamp = datetime.now(timezone.utc).strftime("%Y_%m_%d_%H_%M_%S_%f")
    mimetype, data = image_data.split(";base64,")
    file_extention = mimetype.split("/")[-1]
    image_name = get_valid_filename(f"{user_id}_{current_timestamp}.{file_extention}")
    image_file = ContentFile(base64.b64decode(data), name=image_name)
    return image_name, image_file