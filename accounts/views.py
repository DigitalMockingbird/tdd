from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect

from accounts.authentication import PersonaAuthenticationBackend


def persona_login(request):
    assertion = request.POST['assertion']
    user = ''
    pab = PersonaAuthenticationBackend()
    try:
        user = pab.authenticate(assertion=assertion)
        # user = authenticate()
    except Exception as e:
        print('Persona authentication didnt work. Error: {0}'.format(e))
    # user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request, user, backend='accounts.authentication.PersonaAuthenticationBackend')
    return HttpResponse('OK')
