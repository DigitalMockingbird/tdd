from django.contrib.auth import get_user_model

from .base import FunctionalTest

User = get_user_model()


class MyListsTest(FunctionalTest):
    def test_logged_in_users_are_saved_as_my_lists(self):
        # Edith is a logged in user
        self.create_pre_authenticated_session(email='edith@example.com')
        self.browser.refresh()

        # She goes to the home page and starts a list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Reticulate splines\n')
        self.get_item_input_box().send_keys('Immanentize eschaton\n')
        first_list_url = self.browser.current_url

        # She notices a "My Lists" link, for the first time
        self.browser.find_element_by_id('My lists').click()

        # She sees that her list is in there, named according to its first list item
        self.browser.find_element_by_link_text('My lists').click()
        self.assertEqual(self.browser.current_url, first_list_url)

        # She decides to start another list, just to see
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Click cows\n')
        second_list_url = self.browser.current_url

        # Under "my lists", her new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.browser.find_element_by_link_text('Click cows').click()
        self.assertEqual(self.browser.current_url, second_list_url)

        # She logs out. The "My lists" option disappears
        self.browser.find_element_by_id('id_logout').click()
        self.assertEqual(self.browser.find_element_by_link_text('My lists'), [])
