from django.shortcuts import render
import datetime
# Create your views here.
from django.template import loader 
from django.http import HttpResponse 
from bookifyapp.forms import bookForm
from django.shortcuts import redirect
from bookifyapp.models import Book
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url="/login")
@permission_required(["store.view_store"], raise_exception=True)

def hello(request): 
        if request.method == "POST":
            form = bookForm(request.POST)
            if form.is_valid():
                try: 
                    form.save()
                    return redirect('index')
                except:
                    pass
            else:
                form = bookForm()
        return render(request, 'index.html', {'form':form})

@login_required
def create(request):
    bk = bookForm(request.POST or None)
    if bk.is_valid():
        bk.save()
        return redirect("index")
    return render(request, "index.html",{'form':bk})

def index(request):
    books = Book.objects.all()
    return render(request, "show.html",{'books':books})

def edit(request, id):  
    book = Book.objects.get(id=id)  
    return render(request,'edit.html', {'book':book}) 

def update(request, id):  
    book = Book.objects.get(id=id)  
    form = bookForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/bookify/index")  
    return render(request, 'edit.html', {'book': book})  

def destroy(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()  
    return redirect("/bookify/index")  