from selenium import webdriver
from django.shortcuts import render
import unittest

class MainTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_add_cv(self):
        # I check the websites homepage
        self.browser.get('http://localhost:8000')

        # check the page title and header
        self.assertIn("Hamza's Blog", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Hamza's Blog", header_text)
        
        #self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')