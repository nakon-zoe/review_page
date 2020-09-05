from django.shortcuts import render, get_object_or_404
from .models import Bakery_Info, Bakery_Review


# Create your views here.
def index(request):
    bakeries = Bakery_Info.objects.all()
    return render(request, 'index.html', {'bakeries': bakeries})


def show(request, bakery_id):
    bakery = get_object_or_404(Bakery_Info, pk=bakery_id)
    reviews = Bakery_Review.objects.all()
    return render(request, 'show.html', {'bakery': bakery, 'reviews': reviews})
