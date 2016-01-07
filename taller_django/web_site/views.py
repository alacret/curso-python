from django.shortcuts import render
from django.http import HttpResponse
from web_site.models import Articulo, Persona

# Create your views here.

def articulos(request):
	if 'titulo' in request.GET:
		titulo = request.GET['titulo']
		persona = Persona.objects.get(id=1)
		a = Articulo(titulo = titulo, autor = persona)
		a.save()
	#
	formulario = "<form method='get'><input type='text' name='titulo' /></form><br>"	
	#
	articulos = Articulo.objects.all()
	texto = ''
	for i in articulos:
		texto += i.titulo + '<br>'
	respuesta = HttpResponse(formulario + texto)
	return respuesta
	
