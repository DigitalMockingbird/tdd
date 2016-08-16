from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

        def setUp(self):
           self.browser = webdriver.Firefox()
           self.browser.implicitly_wait(3)

        def tearDown(self):
            self.browser.quit()

        def test_can_start_a_list_and_retrieve_it_later(self):
            # User has about about a cool online to-do app.
            # They go to check the homepage.
            self.browser.get('http://localhost:8000')

            # They notice the title and the header mentions to-do lists.
            self.assertIn('To-Do', self.browser.title)
            self.fail('Finish the test')

            # They're invited to do a to-do list right away
            

            # They type "Buy peacock feathers" into the text box (they're a fly-fisher).


            # When they hit enter the page updates, and now lists
            # "1: Buy peacock feathers" as an item of the to-do list


            # There is another text box inviting them to add another item.
            # They enter "Use peacock feathers to make a fly" (they're very methodical)


            # The page updates again, and now shows both items on their list


            # The person wonders if the site will retain the information. They see
            # the site has generated a unique url for them -- there is some explanatory
            # text for the effect.


            # They visit the url and the to-do list is still there


            # Satisfied, they go back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
