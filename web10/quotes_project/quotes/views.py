from django.shortcuts import render, redirect
from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 5)  # 5 цитат на сторінку
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "quotes/index.html", {"page_obj": page_obj})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "quotes/author_detail.html", {"author": author})

@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", {"form": form})

@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AuthorForm()
    return render(request, "quotes/add_author.html", {"form": form})
