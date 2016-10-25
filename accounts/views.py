from django.contrib.auth import login
from django.http import HttpResponse

from accounts.authentication import PersonaAuthenticationBackend


def persona_login(request):
    assertion = request.POST['assertion']
    persona_backend = 'accounts.authentication.PersonaAuthenticationBackend'
    user = ''
    pab = PersonaAuthenticationBackend()
    try:
        user = pab.authenticate(assertion=assertion)
    except Exception as e:
        print('Persona authentication didnt work. Error: {0}'.format(e))
    if user:
        login(request, user, backend=persona_backend)
    return HttpResponse('OK')
