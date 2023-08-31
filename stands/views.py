from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.

def index(request):
    reserva = Reserva.objects.all()
    context = {
        'reserva' : reserva
    }
    return render(request, 'reserva/index.html',context)


def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)  
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,request.FILES,instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reserva/form_reserva.html',{'form':form})


def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar') 


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect('reserva_listar')
    else:
        form = ReservaForm()

    return render(request, "reserva/form_reserva.html", {'form': form})


def product(request, id):
    reserva = get_object_or_404(Reserva,id=id)
    context ={
        'reserva':reserva
    }
    return render(request, "reserva/product.html",context)
