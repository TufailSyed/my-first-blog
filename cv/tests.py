from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from cv.views import cv
from .models import TestModel, CV
from .forms import CVForm 

class CvTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        match = resolve('/cv/')
        print(match.url_name)  
        self.assertEqual(match.func, cv)
        
    def test_cv_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

#class TestModelTest(TestCase):

#    def test_saving_and_retrieving_TestModels(self):
#        first_TestModel = TestModel()
#        first_TestModel.text = 'The first (ever) list TestModel'
#        first_TestModel.save()

#        second_TestModel = TestModel()
#        second_TestModel.text = 'TestModel the second'
#        second_TestModel.save()

#        saved_TestModels = TestModel.objects.all()
 #       self.assertEqual(saved_TestModels.count(), 2)

  #      first_saved_TestModel = saved_TestModels[0]
   #     second_saved_TestModel = saved_TestModels[1]
    #    self.assertEqual(first_saved_TestModel.text, 'The first (ever) list TestModel')
     #   self.assertEqual(second_saved_TestModel.text, 'TestModel the second')

#    def test_can_save_a_POST_request(self):
#        response = self.client.post('/cv/', data={'TestModel_text': 'A new list TestModel'})

 #       self.assertEqual(TestModel.objects.count(), 1)
  #      new_TestModel = TestModel.objects.first()
   #     self.assertEqual(new_TestModel.text, 'A new list TestModel')

#    def test_only_saves_TestModels_when_necessary(self):
    #    self.client.get('/cv/')
     #   self.assertEqual(TestModel.objects.count(), 0)

#    def test_redirects_after_post(self):
#        response = self.client.post('/cv/', data={'TestModel_text': 'A new list TestModel'})
        
 #       self.assertEqual(response.status_code, 302)
  #      self.assertEqual(response['location'], '/cv/')

#    def test_displays_all_list_TestModels(self):
 #       TestModel.objects.create(text='TestModel 1')
  #      TestModel.objects.create(text='TestModel 2')

   #     response = self.client.get('/cv/')

#        self.assertIn('TestModel 1', response.content.decode())
 #       self.assertIn('TestModel 2', response.content.decode())

class CVFormTest(TestCase):

    def test_form_save_handles_saving_to_a_list(self):
        CVs = CV.objects.create()
        form = CVForm(data={'title': 'banter', 'text': 'do me'})
        new_item = form.save()
        self.assertEqual(new_item.title, 'banter')
        self.assertEqual(new_item.text, 'do me')
