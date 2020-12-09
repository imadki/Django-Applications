from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import  City, Voie
from .forms import VoieForm


class VoieListView(ListView):
    model = Voie
    context_object_name = 'voies'
    
from django.contrib import messages 

class VoieCreateView(CreateView):
    
    model = Voie
    form_class = VoieForm

    def get(self, request, *args, **kwargs):   
        form = VoieForm(request.POST)
        context = {'form': form}
        return render(request, 'voie-create.html', context)

    def post(self, request, *args, **kwargs):
        
        user = request.user
     
        form = VoieForm(request.POST)
        context = {'form': form}
        
        if form.is_valid():
            #instance = form.save(commit=False)
            #instance.user = user
            #instance.save()
            #messages.success(request, "Successfully created") 

            #region= form.cleaned_data.get("region")
            #city = form.cleaned_data.get("city")
            voies = Voie.objects.all().order_by("id")
            
           # print("ici", voies)
            
            #print(region, city)
            context={'form': form, 'voies':voies}#'region':region, 'city':city, 'voies':voies}
            
            
        return render(request, 'voie_list.html', context)
 

class VoieUpdateView(UpdateView):
    model = Voie
    form_class = VoieForm
    success_url = reverse_lazy('voie_changelist')

def load_cities(request):
    region_id = request.GET.get('region')
    cities = City.objects.filter(region_id=region_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})

    
def load_voies(request):
    operation_id = request.GET.get('operation')
    voies = Voie.objects.filter(operation_id=operation_id).order_by('name')  
    return render(request, 'voie_dropdown_list_options.html', {'voies': voies})
