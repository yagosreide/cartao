from django.shortcuts import render
from cartaoApp.forms import ValidarForm
from cartaoApp.models import Validar
#def ola(request):
   # return render(request,"cartao/ola.html")

#def index(request):
  #  return render(request, "cartao/index.html")

#def logim(request):
  #  return render(request, "cartao/logim.html") 

def base(request):
  return render(request, "cartao/base.html") 
  
def consulta(request):
  form = ValidarForm(request.POST)
  if request.method == "POST":
      form = ValidarForm(request.POST, request.FILES)
      if form.is_valid():
        obj = form.save()
        obj.save()
        form = ValidarForm()
        
  return render(request,"cartao/consulta.html",{"form":form}) 

def index(request):
  return render(request, "cartao/index.html")

def inicio(request):
  return render(request, "cartao/inicio.html")

def mostrar(request):
    cartoes = Validar.objects.all()
    return render(request, 'cartao/mostrar.html', {'cartoes':cartoes})