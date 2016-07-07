from django.db import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import models

class Referencia(models.Model):
	ciudad 			= models.CharField(max_length = 20)
	def __unicode__(self):
		return self.ciudad

class Proveedor(models.Model):

	identificacion 	= models.CharField(max_length=50, unique = True)
	nombre 			= models.CharField(max_length=50)
	apellido 		= models.CharField(max_length=50)
	telefono 		= models.CharField(max_length=50)
	direccion 		= models.CharField(max_length=50)
	email 			= models.EmailField()
	razon_social 	= models.ForeignKey(Referencia)

	def __unicode__(self):
<<<<<<< HEAD
		return  self.nombre + "  " + self.razon_social.ciudad

class CodigoBarras(models.Model):

	codigo 			= models.CharField(max_length=20)
	fecha 			= models.DateField(auto_now = True)

	def __unicode__(self):
		return self.codigo


class Sede(models.Model):
	nombre_sede 	= models.CharField(max_length = 30)
	direccion 		= models.CharField(max_length=30)
	telefono 		= models.CharField(max_length=20)

	
	def __unicode__(self):
		return self.nombre_sede

=======
		return  self.nombre

class CodigoBarras(models.Model):

	codigo 			= models.CharField(max_length=20, unique = True)
	fecha 			= models.DateField(auto_now = True)


	def __unicode__(self):
		return self.codigo
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba

class Producto(models.Model):

	def url(self,filename):
		ruta = "Cofres/Producto/%s%s"%(self.nombre, str(filename))
		return ruta

	imagen			= models.ImageField(upload_to = url , blank = True, null = True)
	nombre 			= models.CharField(max_length=50)
	fecha_ingreso 	= models.DateField(auto_now = True)
	dimenciones	 	= models.CharField(max_length = 20)
	codigobarras 	= models.ForeignKey(CodigoBarras)
	valor 			= models.IntegerField()
	descripcion 	= models.TextField(max_length= 150 , blank = True)
	cantidad		= models.IntegerField(default = 0)
	estado 			= models.BooleanField(default = True)
<<<<<<< HEAD
	sede 			= models.ForeignKey(Sede)
	def __unicode__(self):
		return self.nombre

=======

	def __unicode__(self):
		return self.nombre



class Sede(models.Model):
	nombre_sede 	= models.CharField(max_length = 30)
	direccion 		= models.CharField(max_length=30)
	telefono 		= models.CharField(max_length=20)

	
	def __unicode__(self):
		return self.nombre_sede


>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
class Salida(models.Model):
	traslados = (
			(u'Traslado',u'Traslado'),
			(u'Cliente',u'Cliente'),
			(u'Reparacion',u'Reparacion'),
			
		)
	
	codigobarras 	= models.ForeignKey(CodigoBarras)
	descripcion 	= models.CharField(max_length=150,blank=True)
	fecha_salida	= models.DateField()
<<<<<<< HEAD
	sede 			= models.ForeignKey(Sede, default = 1)	
	tipo_salida 	= models.CharField(max_length=50,choices = traslados, default = "Traslado")
	producto 		= models.ForeignKey(Producto)
	cantidad 		= models.IntegerField()	
=======
	tipo_salida 	= models.CharField(max_length=50,choices = traslados, default = "Traslado")
	producto 		= models.ForeignKey(Producto)
	cantidad 		= models.IntegerField()
	sede 			= models.ForeignKey(Sede)
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
	numero_contrato = models.IntegerField(blank = True, null = True)


	def __unicode__(self):
		return str(self.fecha_salida)


class Entrada(models.Model):

	fecha_ingreso	= models.DateField()
<<<<<<< HEAD
	codigobarras 	= models.ForeignKey(CodigoBarras)
	producto 		= models.ForeignKey(Producto)
	referencia 		= models.ForeignKey(Proveedor)
	sede_entrada	= models.ForeignKey(Sede, default = 1)
=======
	producto 		= models.ForeignKey(Producto)
	referencia 		= models.ForeignKey(Proveedor)
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
	cantidad 		= models.IntegerField()
	observacion		= models.TextField(max_length = 500,blank=True, null = True)

	def __unicode__(self):
		return str(self.fecha_ingreso)
