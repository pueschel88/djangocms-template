from filer.fields.image import AdminImageWidget
from filer.models import File
from image_cropping.widgets import CropWidget


class FilerCropWidget(AdminImageWidget, CropWidget):

    def render(self, name, value, attrs=None):
        if value:
            file_obj = File.objects.get(pk=value)
            attrs = attrs or {}
            attrs.update({
                'class': 'crop-thumb',
                'data-thumbnail-url':
                    file_obj.thumbnails['admin_sidebar_preview'],
                'data-field-name': name,
                'data-org-width': file_obj.width,
                'data-org-height': file_obj.height,
                'style': 'display:none',

            })
        return super(FilerCropWidget, self).render(name, value, attrs)
