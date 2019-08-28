import hashlib
import requests
def get_request_parmes(parmes):
    parme_list = parmes.split('&')
    parme_dict = {}
    for parme in parme_list:
        parme_per = parme.split('=')
        parme_dict[parme_per[0]] = parme_per[1]
    print(parme_dict)
    return parme_dict

def get_request_api_sign(parme_dict, keys_normal_li):
    encryption_parme(parme_dict, 'cs', 'imei')
    print('parme_dict__:', parme_dict)
    api_keys_dict = {
        'cb412e048ee48f5f6ca62f9bf339a069' : '84ccd57681cea4ae9ccac0517fd2e0dd',
        '9dac6633be895da152187b9c1a5c0042' : '587ca62428fbb663bb652a49d88bf7e7',
    }
    # keys_normal_li = ['api_key', 'imei' , 'model' , 'city' , 'app_ver' , 'sdk_ver', 'version', 'sysvs',  'nettype',  'ver',  'andorid']
    keys_li = []
    parme_values = ''
    if 'api_key' not in parme_dict.keys():
        parme_dict['api_key'] = '9dac6633be895da152187b9c1a5c0042'
    for key in parme_dict.keys():
        if key in keys_normal_li:
            keys_li.append(key)
    if keys_li.__len__() > 0:
        keys_li.sort()
    for key in keys_li:
        parme_values = parme_values + parme_dict[key]

    parme_values = parme_values + api_keys_dict[parme_dict['api_key']]
    print('parme_values:', parme_values)
    api_sign = get_values_MD5(parme_values)
    print('api_sign:', api_sign)
    parme_dict['api_sign'] = api_sign
    return parme_dict

def get_values_MD5(values_string):
    m2 = hashlib.md5()
    m2.update(values_string.encode('utf-8'))
    return m2.hexdigest()

def encryption_parme(parme_dict, *args):
    for en_key in args:
        if en_key in parme_dict.keys():
            parme_dict[en_key] = encryption_s(parme_dict[en_key])
    # return parme_dict

def encryption_s(s):
    url = 'http://t-osapi-3g.gionee.com/api/adminapi/imei?type=encode&imei=%s' % s
    r = requests.get(url)
    print(r.text)
    return r.text

def for_get_request(url, parme):
    requests.get(url, params=parme).json()

if __name__ == '__main__':
    pass

