from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(req):
    forma = Avtomotor()
    av = Avto.objects.all()
    data = {'forma': forma, 'avtobasa': av}
    return render(req, 'index.html', context=data)

def motor(req):
    avt = Avto()
    avt.marka = 'LADA'
    avt.zavod = 'AVTOVAZ'
    avt.yaer = 5
    avt.nomer = 'E555KX55'
    avt.save()
    return redirect('home')

def create(req):
    if req.POST:
        avt = Avto()
        avt.marka = req.POST.get('marka1')
        avt.zavod = req.POST.get('zavod1')
        avt.yaer = req.POST.get('yaer1')
        avt.nomer = req.POST.get('nomer1')
        avt.save()
        return redirect('home')

def delete (req,ids):
    avt = Avto.objects.get(id=ids)
    avt.delete()
    return redirect('home')
