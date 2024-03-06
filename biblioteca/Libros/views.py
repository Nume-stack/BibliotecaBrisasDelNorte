from django.shortcuts import render, redirect
from .models import *
import datetime

# Create your views here.

# Funciones para Autores
def home(request):
    autores = Autor.objects.all()
    return render(request,"Autor.html", {"autor": autores})

def registrarAutor(request):
    nombreAutor = request.POST['txtAutor']

    autor = Autor.objects.create(
        NombreAutor = nombreAutor
    )
    return redirect('/')

def eliminarAutor(request, idAutor):
    autor = Autor.objects.get(idAutor = idAutor)
    autor.activoAutor = False
    autor.actualizaAutor = datetime.datetime.now()
    autor.save()
    return redirect('/')

def EdicionAutor(request, idAutor):
    autor = Autor.objects.get(idAutor = idAutor)
    return render(request, "editarAutor.html", {"autor": autor} )

def editarAutor(request, idAutor):
    autor = Autor.objects.get(idAutor = idAutor)
    autor.NombreAutor = request.POST['txtAutor']
    autor.activoAutor = request.POST['txtActivo']
    autor.save()
    return redirect('/')

#Funciones para categorias
def Categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {"categoria":categorias})

def registrarCategoria(request):
    categoria = Categoria.objects.create(
        NombreCategoria = request.POST['txtCategoria']
    )
    return redirect('categorias')

def eliminarCategoria(request, idCategoria):
    categoria = Categoria.objects.get(idCategoria = idCategoria)
    categoria.activoCategoria = False
    categoria.actualizaCategoria = datetime.datetime.now()
    categoria.save()
    return redirect('categorias')

def edicionCategorias(request, idCategoria):
    categoria = Categoria.objects.get(idCategoria = idCategoria)
    return render(request, "edicionCategoria.html", {"categorias":categoria})

def editarCategorias(request, idCategoria):
    categoria = Categoria.objects.get(idCategoria = idCategoria)
    categoria.NombreCategoria = request.POST['txtCategoria']
    categoria.activoCategoria = request.POST['txtActivo']
    categoria.actualizaCategoria = datetime.datetime.now()
    categoria.save()
    return redirect('categorias')

#Funciones para Editoriales
def editoriales(request):
    editorial = Editorial.objects.all()
    return render(request, "editorial.html", {"editoriales":editorial})

def registrarEditorial(request):
    editorial = Editorial.objects.create(
        NombreEditorial = request.POST['txtEditorial']
    )
    return redirect('editoriales')

def eliminarEditorial(reques, idEditorial):
    editorial = Editorial.objects.get(idEditorial = idEditorial)
    editorial.activoEditorial = False
    editorial.actualizaEditorial = datetime.datetime.now()
    editorial.save()
    return redirect('editoriales')

def edicionEditorial(request, idEditorial):
    editorial = Editorial.objects.get(idEditorial = idEditorial)
    return render(request, "edicionEditorial.html", {"editoriales":editorial})

def editarEditorial(request, idEditorial):
    editorial = Editorial.objects.get(idEditorial = idEditorial)
    editorial.NombreEditorial = request.POST['txtEditorial']
    editorial.activoEditorial = request.POST['txtActivo']
    editorial.actualizaEditorial = datetime.datetime.now()
    editorial.save()
    return redirect('editoriales')

#Funciones de Libro
def libro(request):
    libro = Libro.objects.all()
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    editorial = Editorial.objects.all()
    return render(request, "Libros.html", ({"libros":libro,"autor": autores,"categoria":categorias, "editoriales":editorial}))


def registrarLibro(request):
    libro = Libro.objects.create(
        tituloLibro = request.POST['txtTitulo'],
        id_autor = request.POST['txtAutorLibro'],
        id_editorial = int(request.POST['txtEditorialLibro']),
        id_categoria = int(request.POST['txtCategoriaLibro'])
    )
    return redirect('Libros')


