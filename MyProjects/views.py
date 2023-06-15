from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import InputForm
from service.models import Contact
from service.models import Profession
from news.models import MyNews
from PaginationApp.models import UserInfo
from django.core.paginator import Paginator

def home(request):
    newsdata=MyNews.objects.all()
    servicedata=Profession.objects.all()
    data={
        'servicedata':servicedata,
        'newsdata':newsdata,
    }
    return render(request, 'index.html',data)


def aboutus(request):

    return render(request, 'about.html')

def news_details(request,newsid):
    newsdata=MyNews.objects.get(id=newsid)
    data={
        'newsdetaildata':newsdata,
    }
    return render(request, 'newsdetail.html',data)

def contact(request):
    try:
        if request.method == 'POST':
            post=Contact()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            post.subject = request.POST.get('subject')
            post.message = request.POST.get('message')
            post.save()
            return render(request, 'contact.html')
    except:
        pass
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def gallerysingle(request):
    return render(request, 'gallery-single.html')


def gallery(request):
    return render(request, 'gallery.html')

def user_information(request):
    userdata=UserInfo.objects.all()
    p = Paginator(userdata, 2)
    page_number = request.GET.get('page')
    try:
         # returns the desired page object
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    data={
        'userdata':page_obj,
    }
    return render(request, 'userinfo.html',data)

def userformGet(request):
    try:
        name = request.GET['name']
        email = request.GET['email']
        subject = request.GET['subject']
        msg = request.GET['message']
        print(name)
        print(email)
        print(subject)
        print(msg)
    except:
        pass
    return render(request, 'userformGet.html')


def userformPost(request):
    data = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            msg = request.POST.get('message')
            data = {

                'name': name,
                'email': email,
                'subject': subject,
            }

            return HttpResponseRedirect('/')
    except:
        pass
    return render(request, 'userformPost.html', data)


def djangoInputForm(request):
    fn = InputForm()
    data = {'form': fn}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            msg = request.POST.get('message')
            data = {
                'form': fn,
                'name': name,
                'email': email,
                'subject': subject,
            }

            return HttpResponseRedirect('/')
    except:
        pass
    return render(request, 'Inputform.html', data)


def calculator(request):
    c = ''
    try:
        if request.method == 'POST':
            value1 = eval(request.POST.get('val-1'))
            value2 = eval(request.POST.get('val-2'))
            oprator = request.POST.get('opr')
            if oprator == '+':
                c = value1+value2
            elif oprator == '-':
                c = value1-value2
            elif oprator == 'x':
                c = value1*value2
            elif oprator == '/':
                c = value1/value2
            else:
                c = 'Invalid Oprator'

    except Exception as ec:
        print(ec)
    print(c)
    return render(request, "calculator.html", {'c': c})

# Handle blank form
def evenoddblankinput(request):
    output = ''

    if request.method == 'POST':
        if request.POST.get('val-1')=='':
            return render(request, 'evenOdd.html', {'error': True})
        else:
            val = eval(request.POST.get('val-1'))
            if val % 2 == 0:
                output = 'EVEN'
            else:
                output = 'ODD'

    print(output)

    return render(request, 'evenOdd.html', {'output': output})

def evenodd(request):
    output = ''
    try:
        if request.method == 'POST':
            val = eval(request.POST.get('val-1'))
            if val % 2 == 0:
                output = 'EVEN'
            else:
                output = 'ODD'
    except:
        pass
    return render(request, 'evenOdd.html', {'output': output})


def marksheet(request):
    percentage = ''
    data = {}
    try:
        if request.method == 'POST':
            hindi = eval(request.POST.get('hindi'))
            english = eval(request.POST.get('english'))
            math = eval(request.POST.get('mathematics'))
            phy = eval(request.POST.get('physics'))
            chemty = eval(request.POST.get('chemistry'))
            tot = hindi+english+math+phy+chemty
            percentage = (tot/500)*100
            hindim = hindi
            data = {
                'hindi': hindi,
                'english': english,
                'math': math,
                'physics': phy,
                'chemistry': chemty,
                'parcentage': percentage
            }
    except Exception as ec:
        print(ec)

    print(percentage)
    print(data)
    return render(request, 'marksheet.html', data)

# def yourmarksheet(re)


def goals_by_timeframe(request, timeframe):
    if timeframe == 'daily':
        goals = '<h1>Daily Goals</h1>'
    elif timeframe == 'weekly':
        goals = '<h1>Weekly Goals</h1>'
    elif timeframe == 'monthly':
        goals = '<h1>Monthly Goals</h1>'
    else:
        return HttpResponse('<h1>No Goals Found</h1>')
    return HttpResponse(goals)


def success(request):
    data = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            msg = request.POST.get('message')

            return HttpResponse(f'Hi {name} Thanks for contact us We will touch with you shortly...')
    except:
        pass
    return render(request, 'userformPost.html', data)
