from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/base.html')

class MyCVTest(TestCase):

    def test_my_cv_page_uses_template(self):
        response = self.client.get('/my_cv/')
        self.assertTemplateUsed(response, 'blog/my_cv.html')
    