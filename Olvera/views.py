from django.shortcuts import render

def inicio (request):
    return render (request, 'Olvera/inicio.html')

def registro (request):
    return render (request, 'Olvera/formregistro.html') 

# Create your views here.
