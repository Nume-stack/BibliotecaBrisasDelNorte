from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Usuario)
admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)