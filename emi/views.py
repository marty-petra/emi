from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, EMI App V1.0")
