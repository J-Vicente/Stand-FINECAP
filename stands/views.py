from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva
from .forms import ReservaForm
from .filters import ReservaFilter

# Create your views here.

def index(request):
    reserva = Reserva.objects.all().order_by('data')
    filter = ReservaFilter(request.GET, queryset=Reserva.objects.all())
    context = {
        'reserva' : reserva, 'filter' : filter
    }
    return render(request, 'reserva/index.html',context)


def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)  
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,request.FILES,instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reserva/form_reserva.html',{'form':form})


def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('index') 


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect('index')
    else:
        form = ReservaForm()

    return render(request, "reserva/form_reserva.html", {'form': form})


def reserva(request, id):
    reserva = get_object_or_404(Reserva,id=id)
    if reserva.quitado == True:
        reserva.quitado = 'Sim'
    else:
        reserva.quitado = 'Não'
    context ={
        'reserva':reserva
    }
    return render(request, "reserva/reserva.html",context)
