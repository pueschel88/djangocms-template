from django.contrib import admin
from filer.admin import FolderAdmin
from filer.admin import ImageAdmin
from filer.admin.imageadmin import ImageAdminForm

from backend.media_filer.models import FilerFolder
from backend.media_filer.models import ProxyFilerImage


@admin.register(FilerFolder)
class FilerFolderAdmin(FolderAdmin):
    directory_listing_template = 'folder/directory_listing.html'


@admin.register(ProxyFilerImage)
class FilerImageAdmin(ImageAdmin):
    change_form_template = 'admin/image/change_form.html'
    form = ImageAdminForm
