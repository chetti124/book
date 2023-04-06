from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from .models import Book

def home(request):
    if request.method == "POST":
        DATA = request.POST
        bid = DATA.get("book_id")
        name = DATA.get("Book_name")
        price = DATA.get("Book_price")
        qty = DATA.get("Book_qty")
        author = DATA.get("Book_author")
        is_active = DATA.get("Book_isactive")
        if is_active=="Yes":
            is_active = True
        else :
            is_active=False
            
        if not bid:
            Book.objects.create(name=name, price=price, qty=qty, author=author, is_active=is_active)

        else:
            data = Book.objects.get(id=bid)
            data.name = name
            data.price = price
            data.qty = qty
            data.author = author
            data.is_active = is_active
            data.save()

        return redirect("home_page")


    elif request.method == "GET":
        return render(request, "home.html")
    

def store_books(request):
    return render(request, "store_books.html", context = {"all_books":Book.objects.filter(is_active=True), "active":False})

def update_book(request, id):
    data = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book":data})

def delete_book(request, id):
    data = Book.objects.get(id=id)
    data.delete()
    data.save()
    return redirect("store_books")

def soft_delete(request, id):
    data = Book.objects.get(id=id)
    data.is_active=False
    data.save()
    return redirect("store_books")

def inactive_books(request):
    return render(request, "store_books.html", context={"all_books":Book.objects.filter(is_active=False), "inactive":True})

def restore_book(request, id):
    data = Book.objects.get(id=id)
    data.is_active=True
    data.save()
    return redirect("store_books")