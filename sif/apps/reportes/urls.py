from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('sif.apps.reportes.views',
	url(r'^reporte_entrada/$','reporte_view_entrada', name = 'vista_reporte_entrada'),
	url(r'^reporte_salida/$','reporte_view_salida', name = 'vista_reporte_salida'),
	url(r'^lista_reportes/$','reportes_view', name = 'vista_reportes'),
<<<<<<< HEAD
	#url(r'^generar_pdf/$', 'generar_pdf' , name = 'vista_pdf'),
	url(r"^pdf/(?P<fecha_inicio>[^/]+)/(?P<fecha_fin>[^/]+)/(?P<tipo>[^/]+)$", 'generar_pdf_view' , name = 'generar_pdf'),
=======

>>>>>>> 8bf3e0241d0b5598f8167dfcfdabe3bfe8c4feba
)