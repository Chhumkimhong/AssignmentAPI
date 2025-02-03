from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","Categoryname","image_preview","CategoryDate"]
    list_filter = ["Categoryname","CategoryDate"]
    search_fields = ["Categoryname"]
    readonly_fields = ["image_preview"]

    
    def image_preview(self, obj):
        if obj.CategoryImage:
            return format_html('<img src="{}" style="width: 200px; height: auto;" />', obj.CategoryImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'


class ProductAdmin(admin.ModelAdmin):
    list_display=["id","ProductName","CategoryID","image_preview","ProductTitle","Instock","PriceOut","ProductDescription","ProductDate"]
    list_filter = ["ProductName","ProductDate"]
    search_fields = ["ProductName"]
    readonly_fields = ["image_preview"]

    
    def image_preview(self, obj):
        if obj.ProductImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.ProductImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'


admin.site.register(Customer)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Supplier)
admin.site.register(tblClients)
admin.site.register(tblProducts,ProductAdmin)
admin.site.register(tblTopMenu)
admin.site.register(tblSubTopMenu)
admin.site.register(tblSlides)
admin.site.register(tblFreshOrganic)
admin.site.register(BestSeller)
admin.site.register(ListCart)
admin.site.register(CartItem)





