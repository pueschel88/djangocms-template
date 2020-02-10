from django.db import models
from filer.models import Folder
from filer.models import Image

from backend.media_filer.fields import CroppableFilerImageField


class FilerImage(Image):
    cropping = CroppableFilerImageField(on_delete=models.PROTECT, related_name='+')


class ProxyFilerImage(FilerImage):
    class Meta:
        proxy = True


class FilerFolder(Folder):
    class Meta:
        proxy = True
