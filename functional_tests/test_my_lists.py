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
