from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("Stewart says Hello!")
   return render (request, 'home.html')

def todos(request):
    return render (request, 'todos.html', {'todos: items'})