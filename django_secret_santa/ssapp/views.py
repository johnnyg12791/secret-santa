from django.template import RequestContext, loader

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Family, Person, Gifts


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


#Of the members in this family, gets the 
def family(request, family_id):
    response = "You are looking at the family %s"
    #family_name = Family.objects.get(id=family_id).name
    people_in_family = Person.objects.filter(family=family_id)

    gift_tuples = Gifts.objects.filter(gifter__in=people_in_family)

    gifter_giftee_family = {}
    for gift_tuple in gift_tuples:
        gifter = gift_tuple.gifter.name
        giftee = gift_tuple.giftee.name
        gifter_giftee_family[gifter] = (giftee, gift_tuple.giftee.family.family_name)
        
    #Get all people in the Family
    #Get gifters in Gifts
    #John Gold, you have ____ from Family ___

    #{Giftner -> (Giftee, Family), Gifter2 -> (Giftee2, Family)}
    context = {'gifters_dict':gifter_giftee_family}
    return render(request, 'ssapp/family.html', context)
    #return HttpResponse(response % family_id)

def person(request, person_id):
    response = "You are looking at the person %s"
    return HttpResponse(response % person_id)


def detail(request):
    response = "Thanks for DETAILED all this information"
    return HttpResponse(response)

def setup(request):
    context = {}
    #update the DB
    return HttpResponseRedirect(reverse('ssapp:detail'))
    #p = get_object_or_404()

def thanks(request):
    response = "Thanks for all this information"
    return HttpResponse(response)