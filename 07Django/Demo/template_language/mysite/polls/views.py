import time
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    now_time = time.ctime()
    print(now_time)
    inform = {'name': 'zhangsan', 'age': 18, 'job': 'Huawei'}
    list_test = ['0 name', '1 age', '2 sex']
    # return HttpResponse("Hello, world.")
    return render(request, 'index.html', 
        {'now_time': now_time, 'inform': inform, 'list_test': list_test})
    # return render(request, 'postcard.html')

