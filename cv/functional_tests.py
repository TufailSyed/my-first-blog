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
        
        #time.sleep(0.5)
        
        find_user = self.browser.find_element_by_css_selector('p.top-menu').text
        #print(find_user)
        self.assertIn('Hello TestUser (Log out)', find_user)

    def test_can_sign_out(self):
        self.browser.get('http://127.0.0.1:8000/')
        find_login = self.browser.find_element_by_xpath("//a[@href='/accounts/login/']").click()
        
        inputbox_username = self.browser.find_element_by_id('id_username').send_keys('TestUser')
        inputbox_password = self.browser.find_element_by_id('id_password').send_keys('TestUser')
        click_login = self.browser.find_element_by_id('login_button').click()
        signed_in_menu = self.browser.find_element_by_class_name('top-menu')

        find_logout = self.browser.find_element_by_xpath("//a[@href='/accounts/logout/']").click()
        
        find_login_button = self.browser.find_element_by_xpath("//a[@href='/accounts/login/']").text
        signed_out_menu = self.browser.find_element_by_class_name('top-menu')

        self.assertNotEqual(signed_in_menu, signed_out_menu)

    def test_can_add_a_comment(self):
        self.browser.get('http://127.0.0.1:8000/')
        find_post = self.browser.find_element_by_xpath("//a[@href='/post/10/']").click()
        find_comment_button = self.browser.find_element_by_xpath("//a[@href='/post/10/comment/']").click()
        
        inputbox_author = self.browser.find_element_by_id('id_author').send_keys('Tufail')
        inputbox_text = self.browser.find_element_by_id('id_text').send_keys('Pls Work')
        find_send_button = self.browser.find_element_by_id('send_button').click()
        
        #time.sleep(0.5)
        
        find_comment_author = self.browser.find_element_by_class_name('comment_author').text
        find_comment_text = self.browser.find_element_by_css_selector('.comment').text
        #print(find_comment_text)
        self.assertIn('Tufail', find_comment_author)
        self.assertIn('Pls Work', find_comment_text)

    def test_can_make_a_blog_post(self):
        self.browser.get('http://127.0.0.1:8000/')
        find_login = self.browser.find_element_by_xpath("//a[@href='/accounts/login/']").click()
        
        inputbox_username = self.browser.find_element_by_id('id_username').send_keys('TestUser')
        inputbox_password = self.browser.find_element_by_id('id_password').send_keys('TestUser')
        click_login = self.browser.find_element_by_id('login_button').click()

        find_new_blog_button = self.browser.find_element_by_xpath("//a[@href='/post/new/']").click()

        inputbox_title = self.browser.find_element_by_id('id_title').send_keys('Test Blog')
        inputbox_text = self.browser.find_element_by_id('id_text').send_keys('This actually works')
        find_save_button = self.browser.find_element_by_id('save_button').click()

        find_publish_button = self.browser.find_element_by_id('publish_button').click()

        find_post_title = self.browser.find_element_by_id('post_title').text
        find_post_description = self.browser.find_element_by_id('post_description').text
        find_post_text = self.browser.find_element_by_id('post_text').text

        self.assertIn('Test Blog', find_post_title)
        self.assertIn('Enter description of post here', find_post_description)
        self.assertIn('This actually works', find_post_text)

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