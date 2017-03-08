# coding: utf-8
import json
import urlparse
from django.http import HttpResponse
from lib import response


class JsonMiddleware(object):
    def process_request(self, request):
        try:
            request.json = json.loads(request.body)
        except:
            request.json = {}


class QuertStringMiddleware(object):
    def process_request(self, request):
        query_string = request.META.get("QUERY_STRING", "")
        # convert to json, flat it
        try:
            request.qs = {}
            for k, v in urlparse.parse_qs(query_string).items():
                if len(v) == 1:
                    request.qs[k] = v[0]
                else:
                    request.qs[k] = v
        except:
            request.qs = {}
