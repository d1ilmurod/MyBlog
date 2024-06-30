from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,MyBooks,AboutMe
from django.views.generic import TemplateView
from .forms import ContactForm
# Create your views here.

class HomePage(TemplateView):
    templates_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()

        blog_data = Blog.objects.all()
        books_data = MyBooks.objects.all()[:3]
        star = MyBooks.objects.order_by('-stars').first()
        word = AboutMe.objects.order_by('-about_me').first()
        num = "s" * star.stars
        about_data = AboutMe.objects.all()

        context = {
            'form': form,
            'word':word,
            "blog_data": blog_data,
            "books_data": books_data,
            'num': num,
            'about_data': about_data
        }

        return render(request, "main/index.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'main/index.html', context)



def profile_page(request,pk):
    detail = get_object_or_404(AboutMe,id=pk)

    context = {
        "detail": detail
    }

    return render(request,'main/profile.html',context)





def books_page(request):
    books = MyBooks.objects.all()

    context = {
        "books": books
    }

    return render(request,"main/books.html",context)



def books_detail_page(request,pk):
    book_details = get_object_or_404(MyBooks,id=pk)
    books = MyBooks.objects.all()



    context = {
        "book_details":book_details,
        'books':books
    }

    return render(request,'main/book_detail.html',context)