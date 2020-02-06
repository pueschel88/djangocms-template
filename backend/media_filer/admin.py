from django.contrib import admin
from filer.admin import Image
from filer.admin import ImageAdmin


class FilerImageAdmin(ImageAdmin):
    change_form_template = 'admin/filer/image/change_form.html'


admin.site.unregister(Image)
admin.site.register(Image, FilerImageAdmin)
