import os

from unittest import TestCase

class ConstitutentCounterTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(ConstitutentCounterTestCase, self).__init__(*args, **kwargs)
        self.resource_base = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./test_corpora"))