from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dests = Destination.objects.all()

    """dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'the city that never sleep'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.desc = 'The city that only sleep'
    dest2.img = 'destination_2.jpg'
    dest2.price = 900
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Hyderabad'
    dest3.desc = 'the city that only fight'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1800
    dest3.offer = False

    dests = [dest1, dest2, dest3]"""

    return render(request, 'index.html', {'dests': dests})
