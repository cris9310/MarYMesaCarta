
from .models import *

from django.views.generic import ( ListView)
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy


def RedirectView(request):

    return HttpResponseRedirect(
        reverse_lazy('menu_app:letter')
    )


class DishesListview(ListView):
    model = Dishes
    template_name = 'menu/dishes_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        data = []
        data_prin = Dishes.objects.all().order_by("nombre")
        for i in data_prin:
            
            data_json = {"tipo": str(i.dishes.tipe), "nombre": i.nombre,"description":i.description, "costo": f'$ {i.costo:,.0f}'}   
            data.append(data_json)
        queryset = data
        return queryset
    
