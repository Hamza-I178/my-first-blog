from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home.html')

class Public_CVTest(TestCase):

    def test_public_cv_page_uses_template(self):
        response = self.client.get('/public_cvs_list/')
        self.assertTemplateUsed(response, 'blog/public_cvs_list.html')
    
    def test_public_cv_detail_uses_template(self):
        response = self.client.get('/public_cv/1/')
        self.assertTemplateUsed(response, 'blog/public_cvs_detail.html')
   
    def test_public_cv_edit_uses_template(self):
        response = self.client.get('/public_cv/new/')
        self.assertTemplateUsed(response, 'blog/public_cv_edit.html')

    