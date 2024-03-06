from django.db import models

# Create your models here.

class Autor(models.Model):
    idAutor = models.AutoField( primary_key=True)
    NombreAutor = models.CharField(max_length=100) 
    activoAutor = models.BooleanField(default=True)
    actualizaAutor = models.DateField(auto_now_add=True)

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.NombreAutor)

class Categoria(models.Model):
    idCategoria = models.AutoField( primary_key=True)
    NombreCategoria = models.CharField(max_length=100) 
    activoCategoria = models.BooleanField(default=True)
    actualizaCategoria = models.DateField(auto_now_add=True)

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.NombreCategoria)

class Editorial(models.Model):
    idEditorial = models.AutoField( primary_key=True)
    NombreEditorial = models.CharField(max_length=100) 
    activoEditorial = models.BooleanField(default=True)
    actualizaEditorial = models.DateField(auto_now_add=True)

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.NombreEditorial)

class Usuario(models.Model):
    idUsuario = models.AutoField( primary_key=True)
    nombreUsuario = models.CharField(max_length=100)
    direccionUsuario = models.CharField(max_length=100)
    telefonoUsuario = models.CharField(max_length=50)
    correoUsuario = models.CharField(max_length=50)
    documentoUsuario = models.CharField(max_length=50)
    activoUsuario = models.BooleanField(default=True)
    actualizaUsuario = models.DateField()

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombreUsuario)

class Lector(models.Model):
    idLector = models.AutoField( primary_key=True)
    nombreLector = models.CharField(max_length=100)
    direccionLector = models.CharField(max_length=100)
    telefonoLector = models.CharField(max_length=50)
    correoLector = models.CharField(max_length=50)
    documentoLector = models.CharField(max_length=50)
    activoLector = models.BooleanField(default=True)
    actualizaLector = models.DateField(auto_now_add=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombreLector)

class Libro(models.Model):
    idLibro = models.AutoField(primary_key=True)
    tituloLibro = models.CharField(max_length=100)
    activoLibro = models.BooleanField(default=True)
    actualizaLibro = models.DateField(auto_now_add=True)
    id_categoria = models.ForeignKey(Categoria,null=False, blank=False,on_delete=models.CASCADE)
    id_editorial = models.ForeignKey(Editorial, null=False, blank=False, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.tituloLibro)

class Prestamo(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    estados = [
        ('1', 'Libre'),
        ('2', 'Prestado')
    ]
    estadoPrestamo = models.CharField(max_length=10, choices=estados, default='1')

class DetallePrestamo(models.Model):
    id_prestamo = models.ForeignKey(Prestamo, null=False, blank=False, on_delete=models.CASCADE)
    id_libro = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, null=False, blank=False, on_delete=models.CASCADE)
    id_Usuari0 = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    fechaDePrestamo = models.DateField(auto_now_add=True)
    fechaDeDevolucion = models.DateField()