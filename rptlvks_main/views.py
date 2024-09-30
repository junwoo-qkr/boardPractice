from django.shortcuts import render
from .models import rptlrmf

# Create your views here.

def index(request):
    if rptlrmf.objects.exists():
        texts = rptlrmf.objects.values('title', 'publisher', 'view_num')
        return render(request, 'rptlvks_main/index.html', {'texts':texts})
    return render(request, 'rptlvks_main/index.html', {})
