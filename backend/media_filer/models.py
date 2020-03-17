from django.db import models
from filer.models import BaseImage
from filer.models import Folder
from filer.models import Image
from image_cropping import ImageRatioField

from backend.media_filer.fields import CroppableFilerImageField


class FilerImage(BaseImage):
    image_ptr = CroppableFilerImageField(
        parent_link=True,
        related_name='%(app_label)s_%(class)s_file',
        on_delete=models.CASCADE,
    )
    cropping = ImageRatioField(
        'image_ptr',
        '100x100',
        hide_image_field=True,
    )

    class Meta:
        app_label = 'backend_media_filer'


class FilerFolder(Folder):
    class Meta:
        proxy = True
