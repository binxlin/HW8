from django.http import HttpResponse

# Create your views here.
def myIndex(request):
    my_name = request.POST.get('name',"BINBINSISTER")
    return HttpResponse("Hello"+my_name)
