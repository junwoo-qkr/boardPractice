from django.shortcuts import render
from .models import post

# Create your views here.

def index(request):
    if post.objects.exists():
        texts = post.objects.values('title', 'view_num')
        return render(request, 'rptlvks_main/index.html', {'texts':texts})
    return render(request, 'rptlvks_main/index.html', {})
