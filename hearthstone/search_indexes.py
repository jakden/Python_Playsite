import datetime
from haystack import indexes
from hearthstone.models import CardViewer
from . import views


class CardViewerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    #author = indexes.CharField(model_attr='user')
    

    #card = indexes.EdgeNgramField(model_attr='card')

    def get_model(self):
        return CardViewer
        

    #def index_queryset(self, using=None):
       # """Used when the entire index for model is updated."""
        #return self.get_model().objects.all()
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

