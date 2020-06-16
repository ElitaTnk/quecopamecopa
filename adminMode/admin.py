from django.contrib import admin
from .models import Marca, Producto
import admin_thumbnails


@admin.register(Marca)
@admin_thumbnails.thumbnail('imagen_de_marca')
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Producto)
@admin_thumbnails.thumbnail('imagen')
class ProductoAdmin(admin.ModelAdmin):
    pass
