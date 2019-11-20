from django.test import TestCase
from django.urls import reverse,resolve
from .views import home


class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url=reverse('home')
		print(str(url))
		response=self.client.get(url)
		self.assertEquals(response.status_code,200)

	def test_home_url_resolve_home_view(self):
		view=resolve('/')
		print(str(view))
		self.assertEquals(view.func, home)

