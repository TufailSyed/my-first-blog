from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import post_list, post_detail
from .models import Post
from .forms import PostForm

class PostListTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')
        print(found.url_name)  
        self.assertEqual(found.func, post_list)  

    def test_post_list_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

class PostDetailTest(TestCase):

    def test_root_url_resolves_to_post_detail_view(self):
        banter = resolve('/post/1/')
        print(banter.url_name)  
        self.assertEqual(banter.func, post_detail)
