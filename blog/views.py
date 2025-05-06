from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category,Year


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    
    # print(posts)

    cats = Category.objects.all()
    years = Year.objects.all()

    data = {
        'posts': posts,
        'cats': cats,
        'years': years
                         }
    return render(request, 'index.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    years = Year.objects.all()

    data = {
        'posts': posts,
        'cats': cats,
        'years': years
                         }
    

    # print(post)
    return render(request, 'post.html', {'post': post, 'cats': cats, 'posts': posts, 'years':years})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    years = Year.objects.all()

    data = {
        'posts': posts,
        
        'years': years
                         }
    return render(request, "category.html", {'cat': cat, 'posts': posts, 'years':years})


def year(request, url):
    batch = Year.objects.get(url=url)
    posts = Post.objects.filter(batch=batch)
    cats = Category.objects.all()
    years = Year.objects.all()

    data = {
        'posts': posts,
        
        
                         }
    return render(request, "years.html", {'batch':batch, 'posts': posts, 'cats': cats, 'years':years})





def search_results(request):
  if request.method == 'GET':
    query = request.GET['query']
    posts= Post.objects.filter(title__icontains=query)

    cats = Category.objects.all()
    years = Year.objects.all()

    return render(request, 'search_results.html', { 'posts': posts, 'cats': cats, 'years':years})
  else:
    return render(request, 'search_results.html', {})


def about_us(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    years = Year.objects.all()

    return render(request, 'About_us.html', { 'cats': cats, 'posts': posts, 'years':years})
 

def contact(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    years = Year.objects.all()

    return render(request, 'contact.html', { 'cats': cats, 'posts': posts, 'years':years})

def desclaimer(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    years = Year.objects.all()

    return render(request, 'desclamer.html', { 'cats': cats, 'posts': posts, 'years':years})

def privacy(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    years = Year.objects.all()

    return render(request, 'privacy.html', { 'cats': cats, 'posts': posts, 'years':years})

def terms(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    years = Year.objects.all()

    return render(request, 'terms.html', { 'cats': cats, 'posts': posts, 'years':years})