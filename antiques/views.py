from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from .serializers import *
from .models import *
from .forms import *
import re


class AntiquesView(viewsets.ModelViewSet):
    queryset = Antiques.objects.all()
    serializer_class = AntiquesSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FavoritesView(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()


def create_range():
    r = [x for x in range(9, 19)]
    r2 = []
    for r1 in r:
        dict_ = {
            'century': r1,
            'years': [x for x in range(r1 * 100, r1 * 100 + 100)]
        }
        r2.append(dict_)
    return r2


def index(request):
    context = {
        'antiques': Antiques.objects.all().values(),
        'heart': 'yes',
        'range': create_range(),
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login.html')
    context = {
        'form': Login
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            User.objects.filter(email=email, pwd=pwd).get()
            if 'email' not in request.session or request.session['email'] == "logout":
                request.session['email'] = email
                request.session.modified = True
            return HttpResponseRedirect('index')
        except User.DoesNotExist:
            template = loader.get_template('login.html')
            context = {
                'form': Login,
                'valid': 'no'
            }
    return HttpResponse(template.render(context, request))


def signup(request):
    context = {
        'form': Signup
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        valid = True
        data = {
            'email': email,
            'pwd': pwd,
            'fname': fname,
            'lname': lname
        }
        if User.objects.filter(email=email).exists():
            context['v'] = 'no'
            context['email'] = 'yes'
            context['form'] = Signup(data)
            valid = False
        if not (re.search("[0-9]", pwd) and re.search("[A-Z]", pwd) and (
                re.search("[*!@#&%_.,$?+=-]", pwd) or re.search("-", pwd))):
            context['v'] = 'no'
            context['p'] = 'yes'
            context['form'] = Signup(data)
        if valid:
            user_ = User(email=email, pwd=pwd, first_name=fname, last_name=lname)
            user_.save()
            request.session['email'] = email
            request.session.modified = True
            return HttpResponseRedirect('index')
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(context, request))


def menu(request, kind_):
    context = {
        'antiques': Antiques.objects.filter(type=kind_)
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def add_favorite(request, name):
    if 'email' in request.session and request.session['email'] != "logout":
        email = request.session.get('email')
        user_ = User.objects.get(email=email)
        antique = Antiques.objects.get(name=name)
        fav = Favorites(user_id=user_, antique_id=antique)
        fav.save()
        return HttpResponseRedirect('../index')
    else:
        return HttpResponseRedirect('../login')


def logout(request):
    request.session['email'] = "logout"
    request.session.modified = True
    return HttpResponseRedirect('index')


def check_user(request):
    if 'email' in request.session and request.session['email'] != "logout":
        return HttpResponseRedirect('user')
    else:
        return HttpResponseRedirect('login')


def user(request):
    if 'email' in request.session and request.session['email'] != "logout":
        user_id = User.objects.get(email=request.session['email'])
        favorite = set()
        for f in Favorites.objects.filter(user_id=user_id).select_related("antique_id"):
            favorite.add(f.antique_id)
        context = {
            'antiques': favorite,
            'heart': 'no',
            'email': request.session['email']
        }
        template = loader.get_template('user.html')
        return HttpResponse(template.render(context, request))
    else:
        # return HttpResponseRedirect('login')
        template = loader.get_template('user.html')
        return HttpResponse(template.render())


def filter_(request):
    if request.GET.getlist('year[]'):
        dates = request.GET.getlist('year[]')
        antiques = []
        uncertain = []
        for d in dates:
            for a in Antiques.objects.filter(year__contains=d):
                antiques.append(a)
            if int(d) >= 1000:
                century = str(int(d[:2]) + 1) + 'th century'
            else:
                century = str(int(d[:1]) + 1) + 'th century'
            for a in Antiques.objects.filter(year__contains=century):
                if a not in antiques and a not in uncertain:
                    uncertain.append(a)
        context = {
            'antiques': antiques,
            'uncertain': uncertain
        }
    elif request.GET.getlist("type[]"):
        kind_ = request.GET.getlist("type[]")
        antiques = []
        for k in kind_:
            for a in Antiques.objects.filter(type=k):
                antiques.append(a)
        context = {
            'antiques': antiques
        }
    elif request.GET['search']:
        print('test_search')
        value = request.GET['search']

        context = {
            'antiques': Antiques.objects.filter(name__icontains=value) | Antiques.objects.filter(
                description__icontains=value) | Antiques.objects.filter(creator__icontains=value),
        }
    context['range'] = create_range()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def search(request):
    print('test search')
    value = request.GET['search']
    context = {
        'antiques': Antiques.objects.filter(name__contains=value) | Antiques.objects.filter(
            description__contains=value) | Antiques.objects.filter(creator__contains=value),
        'range': create_range()
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
