from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, HttpResponseRedirect

def panel(request):
    msg = 'Hello, My name is Jiva!'
    return render(request, 'panel.html', {'msg':msg})