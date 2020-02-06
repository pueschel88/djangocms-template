"""
Backend for django-filer
https://github.com/divio/django-filer
Usage: Subsititute FilerImageField for CroppableFilerImageField
"""

from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.source_generators import pil_image
from image_cropping.backends.base import ImageBackend

from backend.media_filer.widgets import FilerCropWidget


class FilerBackend(ImageBackend):
    version_suffix = 'crop'

    WIDGETS = dict(ImageBackend.WIDGETS)
    WIDGETS['CroppableFilerImageField'] = FilerCropWidget

    def get_thumbnail_url(self, image_path, thumbnail_options):
        thumb = get_thumbnailer(image_path)
        return thumb.get_thumbnail(thumbnail_options).url

    def get_size(self, image):
        return pil_image(image).size
