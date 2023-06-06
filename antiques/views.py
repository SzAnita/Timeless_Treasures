import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from .forms import *
from .models import *
from .serializers import *


class AntiquesView(viewsets.ModelViewSet):
    queryset = Antiques.objects.all()
    serializer_class = AntiquesSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FavoritesView(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()


class CollectionsView(viewsets.ModelViewSet):
    serializer_class = CollectionsSerializer
    queryset = Collections.objects.all()


class AntiquesCollectionsView(viewsets.ModelViewSet):
    serializer_class = AntiquesCollectionsSerializer
    queryset = AntiquesCollections.objects.all()


def create_range():
    r = [x for x in range(9, 19)]
    return r


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


def user(request, collection_='favorites'):
    print(collection_)
    if 'email' in request.session and request.session['email'] != "logout":
        user_id = User.objects.get(email=request.session['email'])
        antiques = set()
        userpage = 'yes'
        if collection_ == 'favorites':
            for f in Favorites.objects.filter(user_id=user_id).select_related("antique_id"):
                antiques.add(f.antique_id)
        else:
            userpage = 'no'
            for c in AntiquesCollections.objects.filter(user_id=user_id, collection_id=Collections.objects.get(name=collection_)).select_related('antique_id'):
                antiques.add(c.antique_id)
        collections = set()
        for c in Collections.objects.filter(user_id=user_id):
            collections.add(c.name)
        context = {
            'antiques': antiques,
            'heart': 'no',
            'email': request.session['email'],
            'collections': collections,
            'user': userpage
        }
        template = loader.get_template('user.html')
        return HttpResponse(template.render(context, request))
    else:
        # return HttpResponseRedirect('login')
        template = loader.get_template('user.html')
        context = {
            'user': 'yes'
        }
        return HttpResponse(template.render(context, request))


def filter_(request):
    if request.GET.getlist('year[]'):
        dates = request.GET.getlist('year[]')
        antiques = []
        uncertain = []
        for d in dates:
            for a in Antiques.objects.filter(year__contains=d+'th century') | Antiques.objects.filter(year__startswith=str(int(d)-1)):
                antiques.append(a)
        context = {
            'antiques': antiques
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
        value = request.GET['search']

        context = {
            'antiques': Antiques.objects.filter(name__icontains=value) | Antiques.objects.filter(
                description__icontains=value) | Antiques.objects.filter(creator__icontains=value),
        }
    context['range'] = create_range()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def add_to_collection(request, antique):
    user_ = User.objects.get(email=request.session['email'])
    coll = AntiquesCollections(user_id=user_, antique_id=Antiques.objects.get(name=antique),
                               collection_id=Collections.objects.get(name=request.GET['coll']))
    coll.save()
    return HttpResponseRedirect('../index')


def get_coll(request):
    if 'email' in request.session and request.session['email'] != 'logout':
        user_ = User.objects.get(email=request.session['email'])
        response = [request.GET['antique']]
        collections = []
        for c in Collections.objects.filter(user_id=user_).values_list('name'):
            print(c)
            collections.append(c)
        response.append(collections)
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponseRedirect('login')


def update_coll(request):
    user_ = User.objects.get(email=request.session['email'])
    coll = Collections(user_id=user_, name=request.GET['name'])
    coll.save()
    return HttpResponse('done')
