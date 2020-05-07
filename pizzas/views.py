from django.shortcuts import render

from .models import Pizza

# Create your views here.

def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """List all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show individual pizzas and their toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)