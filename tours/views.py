from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from .forms import PostCommentary, PostResponse
from tours.models import Comment, Application, Tour, Image, Response




def main_page(request):
    content = {}
    template = loader.get_template('tours/main.html')
    return HttpResponse(template.render(content, request))

def advantages(request):
    content = {}
    template = loader.get_template('tours/advantages.html')
    return HttpResponse(template.render(content, request))

def tours(request):
    tours = Tour.objects.all()
    content = {"tours": tours}
    template = loader.get_template('tours/tour.html')
    return HttpResponse(template.render(content, request))

def about(request):
    content = {}
    template = loader.get_template('tours/about.html')
    return HttpResponse(template.render(content, request))

def gallery(request):
    content = {}
    template = loader.get_template('tours/gallery.html')
    return HttpResponse(template.render(content, request))

def contacts(request):
    content = {}
    template = loader.get_template('tours/contacts.html')
    return HttpResponse(template.render(content, request))

def commentaries(request):
    form = PostCommentary
    commentaries = Comment.objects.all()
    content = {'form': form, 'commentaries': commentaries}
    template = loader.get_template('tours/commentaries.html')
    return HttpResponse(template.render(content, request))

def left_comment(request):
    name = request.POST.get('name')
    text = request.POST.get('text')
    form = PostCommentary
    date = timezone.now()
    comment = Comment(name=name, text=text, date=date)
    comment.save()
    commentaries = Comment.objects.all()

    content = {'name': name, 'text': text, 'form': form, 'commentaries': commentaries}
    template = loader.get_template('tours/commentaries.html')
    return HttpResponse(template.render(content, request))

def left_message(request):
    name = request.POST.get('FIO')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    country = request.POST.get('country')
    application = Application(name=name, address=address, phone=phone, country=country)
    application.save()

    content = {}
    template = loader.get_template('tours/main.html')
    return HttpResponse(template.render(content, request))

def proposal(request, arg): 
    proposal = Tour.objects.get(id=arg)
    responses = proposal.responses.all()
    images = proposal.images.all()
    marks = []
    for response in responses:
        marks.append(response.rate)
    try: 
        rank = sum(marks) / len(marks)
        rank = str(rank)[:3]
        if str(rank)[-1] == '0' and len(str(rank)) == 3:
            rank = int(float(rank))
    except:
        rank = 0
    proposal.rating = rank
    proposal.save()
    content = {"proposal": proposal, "responses": responses, "images": images}
    template = loader.get_template('tours/proposal.html')
    return HttpResponse(template.render(content, request))

def add_response(request, arg):
    form = PostResponse
    proposal = Tour.objects.get(id=arg)
    content = {"proposal": proposal, "form": form}
    template = loader.get_template('tours/new_comment.html')
    return HttpResponse(template.render(content, request))

def create_comment(request, arg):
    proposal = Tour.objects.get(id=arg)
    score = request.POST.get('rating')
    name = request.POST.get('user_name')
    text = request.POST.get('user_text')
    proposal.responses.create(user_name=name, user_text=text, rate=score)
    content = {"proposal": proposal}
    template = loader.get_template('tours/proposal.html')
    return redirect(reverse('proposal', args=[arg]))

def category_tour(request, arg):
    tours = Tour.objects.all()
    content = {"tours": tours, "arg": arg}
    template = loader.get_template('tours/category_tour.html')
    return HttpResponse(template.render(content, request))