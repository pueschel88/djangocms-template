from filer.fields.image import AdminImageFormField
from filer.fields.image import FilerImageField

from backend.media_filer.widgets import FilerCropWidget


class CroppableFormField(AdminImageFormField):
    widget = FilerCropWidget


class CroppableFilerImageField(FilerImageField):
    default_form_class = CroppableFormField
