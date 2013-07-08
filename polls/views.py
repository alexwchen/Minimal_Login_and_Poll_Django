from polls.models import Poll, Choice
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from django.utils import timezone


"""
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]

    return render_to_response(
    'polls/index.html',
    {
        'latest_poll_list':latest_poll_list
    })

"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    """
    Return the last five published polls (not including those set to be
    published in the future).
    """
    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

"""
def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response(
    'polls/detail.html',
    {
        'poll':poll
    })
"""
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


"""
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
"""
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

@csrf_protect
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
