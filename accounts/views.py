from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def persona_login(request):
    assertion = request.POST['assertion']
    user = authenticate(assertion)
    # user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request, user)
    return HttpResponse('OK')
