from django.shortcuts import render
from rptlvks_main.forms import postWriteForm

# Create your views here.

def write(request):
    form = postWriteForm()
    return render(request, 'rptlvks_write/write.html', {'form':form})