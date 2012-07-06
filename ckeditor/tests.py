import os
import unittest
from datetime import datetime

from django.conf import settings

from ckeditor import views


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        # Retain original settings.
        self.orig_MEDIA_ROOT = settings.MEDIA_ROOT
        self.orig_CKEDITOR_UPLOAD_PATH = settings.CKEDITOR_UPLOAD_PATH
        self.orig_MEDIA_URL = settings.MEDIA_URL
        self.orig_CKEDITOR_RESTRICT_BY_USER = getattr(settings, \
                'CKEDITOR_RESTRICT_BY_USER', False)

        # Set some test settings.
        settings.MEDIA_ROOT = '/media/root/'
        settings.CKEDITOR_UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT, \
                'uploads')
        settings.MEDIA_URL = '/media/'

        # Create dummy test upload path.
        self.test_path = os.path.join(settings.CKEDITOR_UPLOAD_PATH, \
                'arbitrary', 'path', 'and', 'filename.ext')

        # Create mock user.
        self.mock_user = type('User', (object,), dict(username='test_user', \
                is_superuser=False))

    def tearDown(self):
        # Reset original settings.
        settings.MEDIA_ROOT = self.orig_MEDIA_ROOT
        settings.CKEDITOR_UPLOAD_PATH = self.orig_CKEDITOR_UPLOAD_PATH
        settings.MEDIA_URL = self.orig_MEDIA_URL
        settings.CKEDITOR_RESTRICT_BY_USER = \
                self.orig_CKEDITOR_RESTRICT_BY_USER

