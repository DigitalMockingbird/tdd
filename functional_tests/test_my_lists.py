from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands import create_session


class MyListsTest(FunctionalTest):
    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_session.Command.create_pre_authenticated_session(email)
        ## to set a cookie we first need to visit the domain
        ## 404 pages load the quickest
        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/'
        ))

    def test_logged_in_users_are_saved_as_my_lists(self):
        # Edith is a logged in user
        self.create_pre_authenticated_session('edith@example.com')

        # She goes to the home page and starts a list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Reticulate splines')
        self.get_item_input_box().send_keys('Immanentize eschaton')
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
