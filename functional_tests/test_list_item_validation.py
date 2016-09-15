# from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    # @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and tried to submit an empty list.
        # She hits Enter on the empty input box

        # The home page refreshes, and thee is an error message saying that list items
        # cannot be blank

        # She tries again with some text for the item, which it works

        # Perversely, she now decides to submit a second blank list item

        # She recieves a similar warning on the list page

        # And she can correct it by filling in some text in
        self.fail('Write me!')
