# coding: utf-8
from lib.response import JsonResponse, not_match_func
from models import NewsItem


def ping(request):
    handler_map = {
        "GET": ping_get
    }
    return handler_map.get(request.method, not_match_func)(request)


def news(request):
    handler_map = {
        "GET": news_get
    }
    return handler_map.get(request.method, not_match_func)(request)


def ping_get(request):
    return JsonResponse(
        {
            'msg': 'pong'
        }
    )


def news_get(request):
    news_id = request.qs['news_id']
    return JsonResponse(
        {
            'news': NewsItem.objects.get(id=news_id).to_json()
        }
    )
