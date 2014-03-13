from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		return {'name': 'Kirvy'}
