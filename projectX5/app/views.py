from django.shortcuts import render
from app.models import company
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy


# Create your views here.
class companylist(ListView):
    model=company

class companydetail(DetailView):
    model=company

class companyupdateview(UpdateView):
    model=company
    fields=('name','ceo')

class companycreateview(CreateView):
     model=company
     fields=('name','ceo','city')

class companydeleteview(DeleteView):
     model=company
     success_url=reverse_lazy('company')
