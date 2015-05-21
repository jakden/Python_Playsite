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

	return HttpResponse(template.render(context))


def detail(request, card):
	try:
		card = CardViewer.objects.get(pk=card)

	except CardViewer.DoesNotExist:

		raise Http404('Card does not exist')

	return render(request, 'hearthstone/detail.html', {'card': card, 'mana': card, 'card_class': card})

