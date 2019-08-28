from django.shortcuts import render,HttpResponse
from browser_api import base_for_api
import requests
# Create your views here.
def api_sign_index(request):
    return render(request, 'for_api_sign.html')

def transform_api_sign(request):
    # url_name = 'http://3g.3gtest2.gionee.com/api/lock_screen/charging?sysvs=5.1.16&operators=&app_ver=5.5.6&nettype=1&third_ad_support=0&ver=1&model=M7&andorid=7.1.1'
    url_name = 'http://3g.3gtest2.gionee.com/api/lock_screen/charging?sysvs=5.1.16&operators=&app_ver=5.5.6&nettype=1&ver=1&model=M7&andorid=7.1.1'
    # url_name = request.GET.get('url_name')
    city = request.GET.get('city_name')
    imei_count = request.GET.get('imei_count')
    url = url_name.split('?')

    data = base_for_api.get_request_parmes(url[1])
    data['city'] = city
    # if 'city' in data.keys():
    #     city = data['city']
    result_li = []
    base_imei = '0086002116556'
    count = int(imei_count)
    for i in range(count):
        if i < 10:
            imei = base_imei + '0' + str(i)
        else:
            imei = base_imei + str(i)
        data['imei'] = imei
        # data['city'] = city
        parme = base_for_api.get_request_api_sign(data,
                                                  ["api_key", 'imei', 'model', 'city', 'app_ver',
                                                   'version'])
        print('parme:', parme)
        result = requests.get(url[0], params=parme)
        result.encoding = 'utf-8'
        result_content = '%s:%s' % (imei, str(result.json()['data']['obj']))
        result_li.append(result_content)
    return render(request, 'result_limit.html', {'result' : result_li})
