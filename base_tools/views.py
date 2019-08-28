from django.shortcuts import render, HttpResponse
from django.http import HttpRequest, HttpResponseRedirect
import requests

def en_de_index(request):
    return render(request, 'imei_city_to_encryption_deciphering.html')

def encryption(request):
    name = request.GET.get('en_or_de_name')
    url = 'http://t-osapi-3g.gionee.com/api/adminapi/imei?type=encode&imei=%s' % name
    r = requests.get(url)
    return HttpResponse(r.text)

def deciphering(request):
    name = request.GET.get('en_or_de_name')
    url = 'http://t-osapi-3g.gionee.com/api/adminapi/imei?type=decode&imei=%s' % name
    r = requests.get(url)
    return HttpResponse(r.text)