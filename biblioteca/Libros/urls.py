from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'autores'),
    path('registrarAutor/',views.registrarAutor ),
    path('eliminarAutor/<idAutor>', views.eliminarAutor),
    path('EdicionAutor/<idAutor>', views.EdicionAutor),
    path('EditarAutor/<idAutor>', views.editarAutor),
    path('categorias/', views.Categorias, name='categorias'),
    path('registrarCategoria/', views.registrarCategoria),
    path('categorias/EdicionCategoria/<idCategoria>', views.edicionCategorias),
    path('categorias/eliminarCategoria/<idCategoria>', views.eliminarCategoria),
    path('editarCategorias/<idCategoria>', views.editarCategorias),
    path('editoriales/', views.editoriales, name='editoriales'),
    path('registrarEditorial/', views.registrarEditorial),
    path('editoriales/eliminarEditorial/<idEditorial>', views.eliminarEditorial),
    path('editoriales/EdicionEditorial/<idEditorial>',views.edicionEditorial ),
    path('EditarEditorial/<idEditorial>', views.editarEditorial),
    path('Libros/', views.libro, name='Libros'),
    path('registrarLibro/', views.registrarLibro)
]