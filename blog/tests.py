from django.test import TestCase
from blog.models import Public_CV
from django.utils import timezone

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home.html')

class Public_CVTest(TestCase):

    def test_public_cv_page_uses_template(self):
        response = self.client.get('/public_cvs_list/')
        self.assertTemplateUsed(response, 'blog/public_cvs_list.html')
   
    def test_public_cv_edit_uses_template(self):
        response = self.client.get('/public_cv/new/')
        self.assertTemplateUsed(response, 'blog/public_cv_edit.html')

    def test_public_cv_save(self):
        cv = Public_CV()
        cv.title = "Test CV"
        cv.name = "Jack Black"
        cv.email = "test@mail.com"
        cv.phone = "12345678910"
        cv.address = "123 fake street"
        cv.education = "good school"
        cv.work_experience = "best company"
        cv.interests = "games"
        cv.save()
        
        self.assertEqual(cv.title, "Test CV")
        self.assertEqual(cv.name, "Jack Black")
        self.assertEqual(cv.email, "test@mail.com")
        self.assertEqual(cv.phone, "12345678910")
        self.assertEqual(cv.address, "123 fake street")
        self.assertEqual(cv.education, "good school")
        self.assertEqual(cv.work_experience, "best company")
        self.assertEqual(cv.interests, "games")

    