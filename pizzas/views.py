from django.shortcuts import render

from .models import Pizza

# Create your views here.

def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request, pizzas_id):
    """Show a single pizza and all its toppings."""
    pizzas = Pizza.objects.get(id=pizzas_id)
    toppings = pizzas.entry_set.order_by('-date_added')
    context = {'pizzas': pizzas, 'toppings': toppings}
    return render(request, 'pizzas/pizzas.html', context)