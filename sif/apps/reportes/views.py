from django.shortcuts import render_to_response
from django.template import RequestContext
from sif.apps.inventario.forms import *
from sif.apps.reportes.forms import *
from sif.apps.inventario.models import *
<<<<<<< HEAD
from sif.apps.home.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from datetime import date
from reportlab.pdfgen import canvas
from django.http import HttpResponse
=======
from django.http import HttpResponseRedirect
from datetime import date
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba

#lista reportes
def reportes_view(request):
	return render_to_response('reportes/lista_reportes.html', context_instance = RequestContext(request))

#reporte entrada
def reporte_view_entrada(request): 
	fecha = date.today()
	formulario = busqueda_form()
<<<<<<< HEAD
	sedes = Sede.objects.all()
	
	bandera = "entrada"
	if request.method == 'POST':
		name_sede = request.POST['sede']
		
=======
	bandera = "entrada"
	if request.method == 'POST':
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
		formulario = busqueda_form(request.POST)
		if formulario.is_valid():
			fecha_inicio = formulario.cleaned_data['fecha_inicio']
			fecha_fin = formulario.cleaned_data['fecha_fin']
<<<<<<< HEAD
			if str(fecha_inicio) > str(fecha):
				men = "La fecha de inicio no puede ser mayor a la fecha actual"
				print men
				ctx = {'form': formulario, 'men': men, 'sedes': sedes}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			if str(fecha_fin) < str(fecha_inicio): 
				men = "La fecha final no puede ser menor a la fecha inicial"
				ctx = {'form': formulario, 'men': men, 'sedes': sedes}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			lista_reporte = Entrada.objects.filter(fecha_ingreso__range=(str(fecha_inicio), str(fecha_fin)), sede_entrada__nombre_sede = name_sede)
			men = "No hay entradas disponibles en este rango de fechas"			
			ctx = {'repor': lista_reporte,'form': formulario, 'ban': bandera, 'men_2':men, 'fecha_inicio':fecha_inicio,'fecha_fin':fecha_fin, 'sedes': sedes}
			return render_to_response('reportes/reporte.html',ctx, context_instance = RequestContext(request))
	ctx = {'form': formulario, 'sedes': sedes, 'ban':bandera}
=======
			if str(fecha) < str(fecha_inicio):
				men = "La fecha de inicio no puede ser mayor a la fecha actual"
				ctx = {'form': formulario, 'men': men}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			if str(fecha_fin) < str(fecha_inicio) : 
				men = "La fecha final no puede ser menor a la fecha inicial"
				ctx = {'form': formulario, 'men': men}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			lista_reporte = Entrada.objects.filter(fecha_ingreso__range=(fecha_inicio, fecha_fin))		
			ctx = {'repor': lista_reporte,'form': formulario, 'ban': bandera}
			return render_to_response('reportes/reporte.html',ctx, context_instance = RequestContext(request))
	ctx = {'form': formulario}
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
	return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))


#reporte salida
def reporte_view_salida(request): 
	fecha = date.today()
	formulario = busqueda_form()
<<<<<<< HEAD
	sedes = Sede.objects.all()
	bandera = "salida"
	if request.method == 'POST':
		formulario = busqueda_form(request.POST)
		name_sede = request.POST['sede']
=======
	bandera = "salida"
	if request.method == 'POST':
		formulario = busqueda_form(request.POST)
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
		if formulario.is_valid():
			fecha_inicio = formulario.cleaned_data['fecha_inicio']
			fecha_fin = formulario.cleaned_data['fecha_fin']
			if str(fecha) < str(fecha_inicio):
				men = "La fecha de inicio no puede ser mayor a la fecha actual"
<<<<<<< HEAD
				ctx = {'form': formulario, 'men': men, 'sedes':sedes}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			if str(fecha_fin) < str(fecha_inicio) : 
				men = "La fecha final no puede ser menor a la fecha inicial"
				ctx = {'form': formulario, 'men': men,'sedes':sedes}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			lista_reporte = Salida.objects.filter(fecha_salida__range=(fecha_inicio, fecha_fin), sede__nombre_sede = name_sede)	
			men = "No hay entradas disponibles en este rango de fechas"

			ctx = {'repor': lista_reporte,'form': formulario ,'ban': bandera,'men_2':men,'fecha_inicio':fecha_inicio,'fecha_fin':fecha_fin}
			return render_to_response('reportes/reporte.html',ctx, context_instance = RequestContext(request))
	ctx = {'form': formulario,'ban':bandera, 'sedes':sedes}
	return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))


#Genera el pdf del reporte
def generar_pdf_view(request, fecha_inicio, fecha_fin, tipo):
	if request.user.is_authenticated() and request.user.is_superuser == True:
		fecha = date.today()
		if tipo == "salida":
			lista_reporte = Salida.objects.filter(fecha_salida__range=(fecha_inicio, fecha_fin))	
		else:
			lista_reporte = Entrada.objects.filter(fecha_ingreso__range=(str(fecha_inicio), str(fecha_fin)))

		response = HttpResponse(mimetype='application/pdf')
		response['Content-Disposition'] = 'attachment; filename=reporte.pdf'
		
		c = canvas.Canvas(response)
		y_1 = 700
		y_2 = 670
		y_3 = 680
		bandera = 1
		for p in lista_reporte:
			c.drawString(55,y_3,str(p.id))
			c.drawString(157,y_3,p.producto.nombre)
			c.drawString(295,y_3,str(p.cantidad))
			if tipo == "salida":
				c.drawString(360,y_3,p.tipo_salida)
				c.drawString(465,y_3,str(p.fecha_salida))
				c.drawString(50,30,"Sede de reporte " + p.sede.nombre_sede)
			else:
				c.drawString(360,y_3,p.referencia.razon_social.ciudad)
				c.drawString(465,y_3,str(p.fecha_ingreso))
				c.drawString(50,30,"Sede de reporte " + p.sede_entrada.nombre_sede)
			c.line(50,y_1,50,y_2)
			c.line(153,y_1,153,y_2)
			c.line(253,y_1,253,y_2)
			c.line(353,y_1,353,y_2)
			c.line(453,y_1,453,y_2)
			c.line(550,y_1,550,y_2)
			y_1 = y_1 - 30
			y_3 = y_3 - 30
			c.line(50,y_2,550,y_2)
			y_2 = y_2 - 30
			if y_2 < 100:
				y_1 = 700
				y_2 = 670
				y_3 = 680		
				ban = 1	
				c.showPage()
			if bandera == 1:
				c.drawString(250,800, "Funerales La Ermita")
				
				if tipo =="salida":
					c.drawString(55,710,"No. Salida")
					c.drawString(370,710,"Tipo Salida")
					c.drawString(465,710,"Fecha Salida")
					c.drawString(200,770, "REPORTE DE SALIDA DE COFRES")
				else:
					c.drawString(55,710,"No. Entrada")
					c.drawString(370,710,"Referencia")
					c.drawString(465,710,"Fecha Entrada")
					c.drawString(200,770, "REPORTE DE ENTRADA DE COFRES")
				c.drawString(175,710,"Producto")
				c.drawString(275,710,"Cantidad")

				c.line(50,730,550,730)
				c.line(50,700,550,700)
				c.line(50,730,50,700)
				c.line(153,730,153,700)
				c.line(253,730,253,700)
				c.line(353,730,353,700)
				c.line(453,730,453,700)
				c.line(550,730,550,700)


				c.drawString(50,70,"Fecha de generacion "+ str(fecha))
				c.drawString(50,50,"Reporte realizado entre "+ str(fecha_inicio) + "/" + str(fecha_fin))
				
				bandera = 2
		c.showPage()
		c.save()
		return response
	else:
		return render_to_response('reportes/reporte.html', context_instance=RequestContext(request))

=======
				ctx = {'form': formulario, 'men': men}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			if str(fecha_fin) < str(fecha_inicio) : 
				men = "La fecha final no puede ser menor a la fecha inicial"
				ctx = {'form': formulario, 'men': men}
				return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
			lista_reporte = Salida.objects.filter(fecha_salida__range=(fecha_inicio, fecha_fin))		
			ctx = {'repor': lista_reporte,'form': formulario ,'ban': bandera}
			return render_to_response('reportes/reporte.html',ctx, context_instance = RequestContext(request))
	ctx = {'form': formulario}
	return render_to_response('reportes/reporte.html',ctx , context_instance=RequestContext(request))
>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
