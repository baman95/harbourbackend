# harbourbackend/views.py

from django.shortcuts import redirect

def redirect_to_auth(request):
    return redirect('/api/auth/')
