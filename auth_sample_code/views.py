from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.views.decorators.csrf import csrf_protect

#@csrf_protect
def main_page(request):
    print 'what the fuck'
    return render_to_response('index.html')


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
