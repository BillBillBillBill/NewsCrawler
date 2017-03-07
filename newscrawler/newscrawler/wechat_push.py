# coding: utf-8
import json
import datetime
import urllib
import requests
import wechat_config as config


def update_token(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        # 刷新token
        if not config.expires_time or now >= config.expires_time:
            data = {
                'grant_type': 'client_credential',
                'appid': config.appid,
                'secret': config.appsecret
            }
            ret = requests.get(config.token_url + urllib.urlencode(data))
            result = json.loads(ret.text)
            config.access_token = result['access_token']
            config.expires_time = now + datetime.timedelta(hours=2)
        return func(*args, **kwargs)
    return wrapper


@update_token
def send_msg(title, data, openid=config.maintainers[0]):
    data = json.dumps({
        'touser': openid,
        'template_id': config.template_id,
        'url': config.template_url + title,  # 点击打开的链接
        'data': {
            'title': {
                'value': title,
                'color': '#173177'
            },
            'data': {
                'value': data,
                'color': '#173177'
            },
        }
    }).encode()
    url = config.send_url + config.access_token
    ret = requests.post(url, data)
    print 'send result: {}'.format(ret.text)


if __name__ == '__main__':
    from IPython import embed
    embed()
    for maintainer in config.maintainers:
        send_msg('hello', 'start running~', maintainer)
