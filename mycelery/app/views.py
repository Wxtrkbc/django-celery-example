
# Create your views here.

from django.shortcuts import HttpResponse
from django.http import JsonResponse
from app import tasks


def add_test(request):

    # http://www.cnblogs.com/shhnwangjian/category/906800.html
    username = request.GET.get('username')
    tasks.create.delay(username)
    return JsonResponse({'name': username})

