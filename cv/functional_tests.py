from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class AdminTest(unittest.TestCase):
    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()
        
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_website(self):  
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Tufail Syed', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Tufail Syed', header_text)

    def test_can_sign_in(self):
        self.browser.get('http://127.0.0.1:8000/')
        find_login = self.browser.find_element_by_xpath("//a[@href='/accounts/login/']").click()
        
        inputbox_username = self.browser.find_element_by_id('id_username').send_keys('TestUser')
        inputbox_password = self.browser.find_element_by_id('id_password').send_keys('TestUser')
        click_login = self.browser.find_element_by_id('login_button').click()
        
        time.sleep(0.5)
        
        find_user = self.browser.find_element_by_css_selector('p.top-menu').text
        #print(find_user)
        self.assertIn('Hello TestUser (Log out)', find_user)

    def test_can_add_a_comment(self):
        self.browser.get('http://127.0.0.1:8000/')
        find_post = self.browser.find_element_by_xpath("//a[@href='/post/10/']").click()
        find_comment_button = self.browser.find_element_by_xpath("//a[@href='/post/10/comment/']").click()
        
        inputbox_author = self.browser.find_element_by_id('id_author').send_keys('Tufail')
        inputbox_text = self.browser.find_element_by_id('id_text').send_keys('Pls Work')
        find_send_button = self.browser.find_element_by_id('send_button').click()
        
        time.sleep(0.5)
        
        find_comment_author = self.browser.find_element_by_class_name('comment_author').text
        find_comment_text = self.browser.find_element_by_css_selector('.comment').text
        #print(find_comment_text)
        self.assertIn('Tufail', find_comment_author)
        self.assertIn('Pls Work', find_comment_text)

    def test_can_get_to_cv_from_blog(self):
        self.browser.get('http://127.0.0.1:8000/')
        find_cv_link = self.browser.find_element_by_xpath("//a[@href='/cv/']").click()
        cv_header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Tufail Syed - Curriculum vitae', cv_header_text)

    def test_can_get_to_blog_from_cv(self):
        self.browser.get('http://127.0.0.1:8000/cv/')
        find_blog_link = self.browser.find_element_by_xpath("//a[@href='/']").click()
        blog_header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Tufail Syed - Blog', blog_header_text)

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 