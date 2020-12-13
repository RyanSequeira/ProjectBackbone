from django.shortcuts import render
from . import forms
from django.views.decorators.csrf import csrf_exempt
posts = [
    {
        'store_type': 'Antique Stores',
        'title': 'Dirty Jane\'s Antiques',
        'content': '1910 Dayton Blvd, Red Banks, TN 37415',
        'date_posted': 'Red Banks, TN'
    },
    {
        'store_type': 'Restaurants',
        'title': '2 Squares A Day',
        'content': '3399 Amnicola Hwy, Chattanooga, TN 37406',
        'date_posted': 'Chattanooga, TN'
    },
    {
        'store_type': 'Antique Stores',
        'title': 'Southside Antiques, LLC',
        'content': '2423 Broad Street, Chattanooga, TN 37406',
        'date_posted': 'Chattanooga, TN'
    },
    {
        'store_type': 'Restaurants',
        'title': 'Villy\'s',
        'content': '1038 White Street SW, Atlanta, GA 30341',
        'date_posted': 'Atlanta, GA'
    },
    {
        'store_type': 'Restaurants',
        'title': 'Fat Cats',
        'content': '2061 W 10th Street, Cleveland, OH 44113',
        'date_posted': 'Cleveland, OH'
    },
    {
        'store_type': 'Bookstores',
        'title': 'Atlanta Vintage Books',
        'content': '3660 Clairmont Rd Atlanta, GA 30341',
        'date_posted': 'Atlanta, GA'
    },
    {
        'store_type': 'Bookstores',
        'title': 'Calico Cat Bookshop',
        'content': '495 East Main St, Ventura, CA 93001',
        'date_posted': 'Ventura, CA'
    },
]


@csrf_exempt
def home(request):
    context = {}
    if request.method == 'GET':
        form = forms.inputForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data['searchInput'].lower().strip()
            newPosts = [i for i in posts if keyword in ([j.lower().strip() for j in list(i.values())])]
            if len(newPosts) == 0:
                newPosts = None
            context = {
                'posts': newPosts
            }
            if not context['posts'] == None:
                return render(request, 'blog/home.html', context)
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def company(request):
    context = {
        'posts': posts
    }
    return render (request, 'blog/company.html', context)

def dja(request):
    return render (request, 'blog/DirtyJane\'sAntiques.html', {'title': 'Dirty Jane\'s Antiques'})

def twosq(request):
    return render (request, 'blog/2SquaresADay.html', {'title': '2 Squares A Day'})

def southside_antiques(request):
    return render(request, 'blog/SouthsideAntiques,LLC.html', {'title': 'Southside Anques, LLC'})

def villys(request):
    return render(request, 'blog/Villys.html', {'title': 'Villy\'s'})

def fat_cats(request):
    return render(request, 'blog/FatCats.html', {'title': 'Fat Cats'})

def avb(request):
    return render(request, 'blog/AVB.html', {'title': 'Atlanta Vintage Books'})

def calico(request):
    return render(request, 'blog/Calico.html', {'title': 'Calico Cat Bookshop'})

def antique_stores(request):
    context = {
        'posts': [store for store in posts if store['store_type'] == "Antique Stores"]
    }
    return render (request, 'blog/AntiqueStores.html', context)

def restaurants(request):
    context = {
        'posts': [store for store in posts if store['store_type'] == "Restaurants"]
    }
    return render (request, 'blog/Restaurants.html', context)

def bookstores(request):
    context = {
        'posts': [store for store in posts if store['store_type'] == "Bookstores"]
    }
    return render (request, 'blog/Bookstores.html', context)
