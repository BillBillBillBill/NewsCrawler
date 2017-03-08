# coding: utf-8
from django.http import HttpResponse
import json
from error_code import get_message


def JsonErrorResponse(code=10001, error_body=None):
    try:
        if error_body:
            data = json.dumps({
                'code': code,
                'message': error_body
            })
        else:
            data = '{"code": %s, "message": "%s"}' % (code, get_message(code))
    except:
        return JsonErrorResponse(10005)
    response = HttpResponse(
        content=data,
        content_type='application/json; charset=utf-8',
        status=400
    )
    return response


def JsonResponse(json_data={}):
    try:
        if isinstance(json_data, str):
            data = '{"code": 0, "data": %s}' % json_data
        else:
            data = {
                "code": 0,
                "data": json_data
            }
            data = json.dumps(data)
    except:
        return JsonErrorResponse(10005)
    response = HttpResponse(
        content=data,
        content_type='application/json; charset=utf-8',
        status=200
    )
    return response


def not_match_func(request):
    return JsonErrorResponse(10002)
