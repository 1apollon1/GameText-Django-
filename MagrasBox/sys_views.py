from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect

def hand404(request, exception):
    return redirect('get_to_main')