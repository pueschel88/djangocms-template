from django.contrib import admin
from filer.admin import FolderAdmin
from filer.admin import ImageAdmin
from filer.admin.imageadmin import ImageAdminForm
from filer.settings import FILER_IMAGE_MODEL
from filer.utils.loader import load_model
from image_cropping import ImageCroppingMixin

from backend.media_filer.models import FilerFolder
from backend.media_filer.models import FilerImage

Image = load_model(FILER_IMAGE_MODEL)


class FilerImageAdminForm(ImageAdminForm):
    class Meta:
        model = FilerImage
        exclude = ()


@admin.register(FilerFolder)
class FilerFolderAdmin(FolderAdmin):
    directory_listing_template = 'folder/directory_listing.html'


class FilerImageAdmin(ImageCroppingMixin, ImageAdmin):
    change_form_template = 'admin/image/filer_image_change_form.html'
    form = FilerImageAdminForm


FilerImageAdmin.fieldsets = FilerImageAdmin.build_fieldsets(
    extra_main_fields=('cropping', 'image_ptr'),
    extra_fieldsets=(
        ('Subject Location', {
            'fields': ('subject_location',),
            'classes': ('collapse',),
        }),
    )
)

admin.site.unregister(Image)
admin.site.register(FilerImage, FilerImageAdmin)
