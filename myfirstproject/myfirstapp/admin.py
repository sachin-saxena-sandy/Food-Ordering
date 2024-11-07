from django.contrib import admin
from myfirstapp.models import Contact
from myfirstapp.models import Image
from django.utils.html import format_html


# Register your models here.
admin.site.register(Contact)
#admin.site.register(Addvehicle)

class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.addvehicle.url))

    image_tag.short_description = 'Image'
    list_display = ['id','photo','date']

admin.site.register(Image, ImageAdmin)
