from django.http import Http404

from django.http import HttpResponse
from .models import CardViewer
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
# Create your views here.



def index(request):
	card_list = CardViewer.objects.all()
	template = loader.get_template('hearthstone/index.html')
	context = RequestContext(request, {
        'card_list': card_list,}) 
	#output = Card.objects.all()
	#return HttpResponse(output)
	return HttpResponse(template.render(context))

#def card_name(request, card_name):
	#return HttpResponse("Card name %s.")
def detail(request, card):
	try:
		card = CardViewer.objects.get(pk=card)
	except Card.DoesNotExist:
		raise Http404('Card does not exist')
	return render(request, 'hearthstone/detail.html', {'card': card})

def search_cards(request):
	card = SearchQuerySet().autocomplete(content_autorequest.POST.get('search_text', ''))
	return render_to_response('search.html', {'card': card})