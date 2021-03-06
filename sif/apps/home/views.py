from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.inventario.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from sif.apps.home.forms import *
from django.contrib.auth import login, logout , authenticate
<<<<<<< HEAD
from django.core.mail import EmailMultiAlternatives
=======

>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba


def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))

#Sede
def sede_view(request):
	lista_sede = Sede.objects.all()
	ctx = {'sede': lista_sede}
	return render_to_response ('home/sedes.html', ctx, context_instance = RequestContext(request))

#Referencia
def referencia_view(request):
	lista_refe = Referencia.objects.all()
	ctx = {'refe': lista_refe}
	return render_to_response ('home/referencias.html', ctx, context_instance = RequestContext(request))

#Entrada
def single_entrada_view(request,id_entr):
	entrada = Entrada.objects.get(id = id_entr)
	ctx = {'entra': entrada}
	return render_to_response('home/single_entrada.html', ctx, context_instance = RequestContext(request))

def entrada_view(request):
<<<<<<< HEAD
	lista_entrada = Entrada.objects.filter(sede_entrada = 1)
	sede = "Principal"
	ctx = {'entra': lista_entrada, "id_sede" : 1,'sede':sede}
	return render_to_response ('home/entrada.html', ctx, context_instance = RequestContext(request))

def entrada_view_sede(request, id_sede):
	lista_entrada = Entrada.objects.filter(sede_entrada = id_sede)
	sede = Sede.objects.get(id = id_sede).nombre_sede
	ctx = {'entra': lista_entrada, 'sede':sede}
	return render_to_response ('home/entrada.html', ctx, context_instance = RequestContext(request))

#Usuario
=======
	lista_entrada = Entrada.objects.all()
	ctx = {'entra': lista_entrada}
	return render_to_response ('home/entrada.html', ctx, context_instance = RequestContext(request))

#Usuario

>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
def list_usuarios_view(request):
	return render_to_response('home/lista_usuarios.html', context_instance = RequestContext(request))


def single_usuario_view(request,id_user):
<<<<<<< HEAD
	if request.user.is_authenticated():
		usuarito = Usuario.objects.get(id = id_user)
		ctx = {'usuarito':usuarito}	
	else:
		ctx = {}
	
=======
	user = Usuario.objects.get(id =id_user)
	ctx = {'user':user}
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
	return render_to_response('home/single_usuario.html',ctx,context_instance= RequestContext(request))
	
def usuarios_admin_activos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = True, user__is_active = True).order_by('nombre')
	ctx = {'users':lista_usuarios, 'title': 'Lista Administradores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def usuarios_admin_inactivos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = True, user__is_active = False).order_by('nombre')
	ctx = {'users':lista_usuarios, 'title': 'Lista Administradores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def usuarios_oper_activos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = False, user__is_active = True).order_by('nombre')
	ctx = {'users':lista_usuarios, 'title': 'Lista Operadores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def usuarios_oper_inactivos_view(request):
	lista_usuarios = Usuario.objects.filter(user__is_superuser = False, user__is_active = False).order_by('nombre')
	ctx = {'users':lista_usuarios, 'title': 'Lista Operadores'}
	return render_to_response('home/usuarios.html',ctx,context_instance =RequestContext(request))

def inhabilitar_user_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	userito = userito.user
	userito.is_active = False
	userito.save()
	if userito.is_superuser == True:	
		return HttpResponseRedirect('/usuarios_adm/')
	else:
		return HttpResponseRedirect('/usuarios_opr/')

def habilitar_user_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	userito = userito.user
	userito.is_active = True
	userito.save()
	if userito.is_superuser == True:	
		return HttpResponseRedirect('/usuarios_inac_adm/')
	else:
		return HttpResponseRedirect('/usuarios_inac_opr/')

def edit_user_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	usua = userito.user
	iden = userito.id
	formulario = edit_user_form(instance = userito)
	if request.method == "POST":
		formulario = edit_user_form(request.POST, instance = userito)
		if formulario.is_valid():
			edit_user = formulario.save(commit = False)
			username = formulario.cleaned_data['identificacion']
			usua.first_name = formulario.cleaned_data['nombre']
			usua.last_name = formulario.cleaned_data['apellido']
			edit_user.save()
			usua.username = username
			tipo = formulario.cleaned_data['tipo']
			formulario.save()
			if tipo == "admin":
				usua.is_superuser = True
				usua.is_staff = False
			else:
				usua.is_staff = True
				usua.is_superuser = False
			usua.save()
			return HttpResponseRedirect('/list_usuarios')
	ctx = {'form': formulario, 'id': iden}
	return render_to_response('home/edit_user.html', ctx, context_instance = RequestContext(request))

def edit_pass_view(request, id_user):
	userito = Usuario.objects.get(id = id_user)
	userito = userito.user
	formulario = edit_pass_form()
	if request.method == "POST":
		formulario = edit_pass_form(request.POST)
		if formulario.is_valid():
			userito.set_password(formulario.cleaned_data['password_one'])
			userito.save()
			return HttpResponseRedirect('/list_usuarios')
	ctx = {'form': formulario}
	return render_to_response('home/edit_pass.html', ctx, context_instance = RequestContext(request))

#Salida
def single_salida_view(request, id_sal):
	sali = Salida.objects.get(pk = id_sal)
	ctx = {'salida': sali}
	return render_to_response('home/single_salida.html', ctx,  context_instance =RequestContext(request))

def salidas_view(request):
<<<<<<< HEAD
	sali = Salida.objects.filter(sede = 1)
	sede = "Principal"
	ctx = {'salida': sali, 'id_Sede' : 1, 'sede':sede}
	return render_to_response('home/salidas.html', ctx, context_instance = RequestContext(request))


def salida_view_sede(request, id_sede):
	lista_entrada = Salida.objects.filter(sede= id_sede)
	sede = Sede.objects.get(id = id_sede).nombre_sede
	ctx = {'salida': lista_entrada, 'id_Sede': id_sede, 'sede':sede}
	return render_to_response ('home/salidas.html', ctx, context_instance = RequestContext(request))

=======
	sali = Salida.objects.all()
	ctx = {'salida': sali}
	return render_to_response('home/salidas.html', ctx, context_instance = RequestContext(request))

>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
#Proveedor

def proveedor_view(request):
	prov = Proveedor.objects.all()
	ctx = {'proveedores': prov}
	return render_to_response('home/proveedor.html', ctx, context_instance = RequestContext(request))

<<<<<<< HEAD
def single_proveedor_view(request,id_prov):
	prov = Proveedor.objects.get(pk = id_prov)
	ctx = {'proveedor': prov}
	return render_to_response('home/single_proveedor.html',ctx, context_instance = RequestContext(request))


=======
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
#Producto
def  single_product_view(request, id_prod):
	prod = Producto.objects.get(id = id_prod)
	ctx = {'producto':prod}
	return render_to_response('home/single_producto.html',ctx,context_instance = RequestContext(request))
		
def productos_view(request):
<<<<<<< HEAD
	lista_prod = Producto.objects.filter(sede = 1)
	sedes = Sede.objects.all()
	total = 0
	for p in lista_prod:
		total = total + p.cantidad
	sede = "Principal"
	ctx = {'Producto': lista_prod, 'id_Sede' : 1, 'sede':sede, 'total':total, 'sedes':sedes}
	return render_to_response('home/productos.html', ctx,context_instance = RequestContext(request))

def producto_view_sede(request, id_sede):
	lista_prod = Producto.objects.filter(sede= id_sede)
	total = 0
	for p in lista_prod:
		total = total + p.cantidad
	sede = Sede.objects.get(id = id_sede).nombre_sede
	ctx = {'Producto': lista_prod, 'id_Sede': id_sede, 'sede':sede,'total':total}
	return render_to_response ('home/productos.html', ctx, context_instance = RequestContext(request))

=======
	lista_prod = Producto.objects.all()
	ctx = {'Producto': lista_prod}
	return render_to_response('home/productos.html', ctx,context_instance = RequestContext(request))

>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba

#Registro de usuario
def register_view(request):
	form = RegisterForm()
	form_oper = add_usuario_form()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		form_oper = add_usuario_form(request.POST)
		if form.is_valid() and form_oper.is_valid():
<<<<<<< HEAD
			email 	= form_oper.cleaned_data['email']
=======
			email 	= form.cleaned_data['email']
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			nombre = form_oper.cleaned_data['nombre']
			apellido= form_oper.cleaned_data['apellido']
			tipo = form.cleaned_data['tipo']		
			username = form_oper.cleaned_data['identificacion']
			u = User.objects.create_user(username = username, email = email, password = password_one, first_name = nombre, last_name = apellido)
			u.save()
			if tipo == "admin":
				u.is_superuser  = True
			else:
				u.is_staff = True
			u.save()		
			add_usuario = form_oper.save(commit = False)
			add_usuario.user = u
			add_usuario.save()
			return HttpResponseRedirect('/list_usuarios')
		else:
			ctx = {'form': form, 'form_oper': form_oper}
			return render_to_response('home/registro.html', ctx, context_instance = RequestContext(request))
	ctx = {'form': form, 'form_oper': form_oper}
	return render_to_response('home/registro.html', ctx, context_instance = RequestContext(request))


#Login - logout

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form': formulario, 'men': mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


#Generar cootizacion

<<<<<<< HEAD
list = []

def cotizacion_view(request):
	# o = falso 1 = verdadero
	info_enviado = 0
	
	detalle =[]
	if request.method == "POST":
		formulario = cotizacion_form(request.POST)
		formulario2 = agregar_cotizacion_forms(request.POST)
		if formulario.is_valid() or formulario2.is_valid():

			if formulario2.is_valid():
				info_enviado = 1

			if info_enviado == 0:
				for p in list:
					list.remove(p)		
				
				info_enviado = 1
				nombre		= formulario.cleaned_data['nombre']
				apellido	= formulario.cleaned_data['apellido']
				direccion	= formulario.cleaned_data['direccion']
				telefono	= formulario.cleaned_data['telefono']
				email 		= formulario.cleaned_data['email']
				formulario 	= agregar_cotizacion_forms()
				ctx = {'form':formulario,  "info_enviado":info_enviado}
				return render_to_response('home/cotizacion.html', ctx, context_instance = RequestContext(request))
			else:
				
				producto	= formulario2.cleaned_data['producto']
				cantidad	= formulario2.cleaned_data['cantidad']
				observacion	= formulario2.cleaned_data['observacion']

				total = producto.valor * cantidad 
				producto = producto.nombre

				detalle.append(producto)
				detalle.append(cantidad)
				detalle.append(total)
				detalle.append(observacion)
				list.append(detalle)
				detalle =[]
				subject = 'Prueba'
				text_content = 'Blablalbla'
				html_content = '<h2>Mensaje</h2><p>Linea 1<br>Linea 2</p>'
				from_email = '"origen" <yycampos@misena.edu.co>'
				to = 'datutalcha3@misena.edu.co'
				msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				agregado = True	
				formulario = agregar_cotizacion_forms()
				ctx = {'form':formulario, 'agregado':agregado, "info_enviado":info_enviado,'lista': list}
				return render_to_response('home/cotizacion.html', ctx, context_instance = RequestContext(request))
	else:	
		formulario = cotizacion_form()
	ctx = {'form': formulario,"info_enviado":info_enviado}
	return render_to_response('home/cotizacion.html',ctx,context_instance = RequestContext(request))
	
=======
def cotizacion_view(request):
	info_enviado = False 
	nombre		= ""
	apellido	= ""
	direccion	= ""
	telefono	= ""
	sede		= ""
	cantidad	= ""
	producto	= ""
	email		= ""
	observacion	= ""

	lista = []
	detalle =[]


	agregado = False

	if request.method == "POST":
		formulario = cotizacion_form(request.POST)
		if formulario.is_valid():
			agregado = True
			info_enviado = True
			nombre		= formulario.cleaned_data['nombre']
			apellido	= formulario.cleaned_data['apellido']
			direccion	= formulario.cleaned_data['direccion']
			telefono	= formulario.cleaned_data['telefono']
			sede		= formulario.cleaned_data['sede']
			producto	= formulario.cleaned_data['producto']
			cantidad	= formulario.cleaned_data['cantidad']
			email 		= formulario.cleaned_data['email']
			observacion	= formulario.cleaned_data['observacion']
			
			i = producto.id

			detalle.append(producto.nombre)
			detalle.append(producto.cantidad)
			detalle.append(producto.valor)

			detalle.append(producto.valor * producto.cantidad)

			lista.append(detalle)
			detalle=[]
	else:	
		formulario = cotizacion_form()
	ctx = {'form': formulario,'lista': lista,"info_enviado":info_enviado,'agregado': agregado}
	return render_to_response('home/cotizacion.html',ctx,context_instance = RequestContext(request))
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
