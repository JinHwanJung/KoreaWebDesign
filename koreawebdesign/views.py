from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import KWD
from .forms import SearchForm


# Create your views here.

def kwdListView(request, page):
    title_object = None
    if page == '1':
        title_object = KWD.objects.all()[:2]
    object_list = KWD.objects.all()[2:]
    pag = Paginator(object_list, 28)
    range = pag.page_range
    page_obj = pag.page(page)
    return render(request, 'koreawebdesign/kwd_list.html',{
        'title_object':title_object,
        'object_list':page_obj.object_list,
        'page_obj': page_obj,
        'range':range,
    })

def index(request):
    return kwdListView(request, '1')

class KWDDetailView(DetailView):
    model = KWD

class KwdTeggedObjectList(TaggedObjectList):
    model = KWD
    template_name = "tagging/tagging_kwd_list.html"
    paginate_by = 28

class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'koreawebdesign/search.html'

    def form_valid(self, form):
        search_word = '%s' % self.request.POST['search_word']
        kwd_list = KWD.objects.filter(
            Q(title__icontains=search_word) |
            Q(content__icontains=search_word)
        ).distinct()
        context = {}
        context['form'] = form
        context['search_word'] = search_word
        context['object_list'] = kwd_list
        return render(self.request, self.template_name, context)