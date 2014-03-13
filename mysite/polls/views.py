from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Choice


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		""" 
		Return the lat five published polls (not including those set to be
		published in the future).
		"""
		return Poll.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Exclude any polls that aren't published yet.
		"""
		return Poll.objects.filter(pub_date__lte=timezone.now())
	
class ResultView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the poll voting from.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice!!!"
		})
	else:
		selected_choice.vote += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after succesfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button.
	return HttpResponseRedirect(reverse('polls:results', args =(p.id,)))
	

# Create your views here.
