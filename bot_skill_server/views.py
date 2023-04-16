from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import json
import random

def healthcheck(request):
    response_string = "ok"
    response_json = json.dumps(response_string)
    return HttpResponse(response_json)