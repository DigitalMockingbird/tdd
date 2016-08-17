from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

        def setUp(self):
           self.browser = webdriver.Firefox()
           self.browser.implicitly_wait(3)

        def tearDown(self):
            self.browser.quit()

        def check_for_row_in_list_table(self, row_text):
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])

        def test_can_start_a_list_and_retrieve_it_later(self):
            # User has about about a cool online to-do app. They go to check the homepage.
            self.browser.get('http://localhost:8000')

            # They notice the title and the header mentions to-do lists.
            self.assertIn('To-Do', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)

            # They're invited to do a to-do list right away
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )

            # They type "Buy peacock feathers" into the text box (they're a fly-fisher).
            inputbox.send_keys('Buy peacock feathers')

            # When they hit enter the page updates, and now lists
            # "1: Buy peacock feathers" as an item of the to-do list
            inputbox.send_keys(Keys.ENTER)

            rows = self.browser.find_elements_by_tag_name('tr')

            # There is another text box inviting them to add another item.
            # They enter "Use peacock feathers to make a fly" (they're very methodical)
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Use peacock feather to make a fly')
            inputbox.send_keys(Keys.ENTER)

            # The page updates again, and now shows both items on their list
            self.check_for_row_in_list_table('1: Buy peacock feathers')
            self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

            # The person wonders if the site will retain the information. They see
            # the site has generated a unique url for them -- there is some explanatory
            # text for the effect.
            self.fail('Finish the test')

            # They visit the url and the to-do list is still there


            # Satisfied, they go back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
