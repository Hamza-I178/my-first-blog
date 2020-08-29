from selenium import webdriver
from django.shortcuts import render
import unittest
import time

class MainTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_check_home(self):
        # I check the websites homepage
        self.browser.get('http://localhost:8000')

        # check the page title and header
        self.assertIn("Hamza's Site", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Hamza's Site", header_text)

    def test_add_cv(self):
        # make a new public cv
        self.browser.get('http://localhost:8000/public_cv/new/')
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Hamza's Site", header_text)

        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.send_keys('Testing 1')

        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Name test')

        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.send_keys('Email test')

        inputbox = self.browser.find_element_by_id('id_phone')
        inputbox.send_keys('Phone test')

        inputbox = self.browser.find_element_by_id('id_address')
        inputbox.send_keys('Address test')

        inputbox = self.browser.find_element_by_id('id_education')
        inputbox.send_keys('Education test')

        inputbox = self.browser.find_element_by_id('id_work_experience')
        inputbox.send_keys('Work test')

        inputbox = self.browser.find_element_by_id('id_interests')
        inputbox.send_keys('Interests test')

        button = self.browser.find_element_by_css_selector('.save')
        button.click()

    def test_check_test_cv_1(self):
        #find the new test cv and click the link to it
        self.browser.get('http://localhost:8000/public_cvs_list')
        test_cv_link = self.browser.find_element_by_partial_link_text("Testing")
        test_cv_link.click()
        time.sleep(1)

        # find the elements and check to see if they're correct
        elements = self.browser.find_elements_by_tag_name('p')
        title = self.browser.find_element_by_tag_name('h2').text
        name = elements[0].text
        email = elements[1].text
        phone = elements[2].text
        address = elements[3].text
        education = elements[4].text
        work = elements[5].text
        interests = elements[6].text

        self.assertIn("Testing 1", title)
        self.assertIn("Name test", name)
        self.assertIn("Email test", email)
        self.assertIn("Phone test", phone)
        self.assertIn("Address test", address)
        self.assertIn("Education test", education)
        self.assertIn("Work test", work)
        self.assertIn("Interests test", interests)

        # sleep used so I can  visually check elements myself for confirmation that test is working
        time.sleep(2)
        
    def test_edit_cv(self):
        #find the new test cv and click the link to it
        self.browser.get('http://localhost:8000/public_cvs_list')
        test_cv_link = self.browser.find_element_by_partial_link_text("Testing")
        test_cv_link.click()
        time.sleep(1)

        links = self.browser.find_elements_by_tag_name('a')
        edit_link = links[-1]
        edit_link.click()

        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.clear()
        inputbox.send_keys('Testing 2')

        # different arbitrary values are used for testing to easily confirm that the edit was successful
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.clear()
        inputbox.send_keys('a')

        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.clear()
        inputbox.send_keys('b')

        inputbox = self.browser.find_element_by_id('id_phone')
        inputbox.clear()
        inputbox.send_keys('c')

        inputbox = self.browser.find_element_by_id('id_address')
        inputbox.clear()
        inputbox.send_keys('d')

        inputbox = self.browser.find_element_by_id('id_education')
        inputbox.clear()
        inputbox.send_keys('e')

        inputbox = self.browser.find_element_by_id('id_work_experience')
        inputbox.clear()
        inputbox.send_keys('f')

        inputbox = self.browser.find_element_by_id('id_interests')
        inputbox.clear()
        inputbox.send_keys('g')

        # sleep used so I can check that fields have been changed
        time.sleep(5)

        button = self.browser.find_element_by_css_selector('.save')
        button.click()
        
        time.sleep(2)

if __name__ == '__main__':  
    unittest.main(warnings='ignore')