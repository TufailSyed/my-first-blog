from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        self.browser.get('http://localhost:8000')
        self.assertIn('Tufail Syed', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Tufail Syed', header_text)

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 