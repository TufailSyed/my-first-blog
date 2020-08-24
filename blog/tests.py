from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import post_list, post_detail, post_edit, post_draft_list
from .models import Post
from .forms import PostForm

class blog_urls_tests(TestCase):
 
    def test_post_list_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_url_resolves_to_post_detail_view(self):
        banter = resolve('/post/1/')
        #print(banter.url_name)  
        self.assertEqual(banter.func, post_detail)

    def test_post_new_uses_correct_template(self):
        response = resolve('/post/1/edit')
        self.assertEqual(response.func, post_edit)

    def test_drafts_uses_correct_template(self):
        response = resolve('/drafts/')
        self.assertEqual(response.func, post_draft_list)
