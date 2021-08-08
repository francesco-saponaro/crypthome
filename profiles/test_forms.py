from django.test import TestCase

from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_only_fields_in_form_metaclass_showing(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))
