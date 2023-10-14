from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva
from .forms import ReservaForm
from .filters import ReservaFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    reserva = Reserva.objects.all().order_by('data')
    filter = ReservaFilter(request.GET, queryset=Reserva.objects.all())
    paginator = Paginator(reserva, 5)
    page = request.GET.get('page')
    pag_obj = paginator.get_page(page)
    context = {
        'reserva' : reserva, 'filter' : filter, 'pag_obj' : pag_obj
    }
    return render(request, 'reserva/index.html',context)

@login_required
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

@login_required
def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('index') 

@login_required
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

@login_required
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
