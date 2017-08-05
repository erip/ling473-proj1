#!/usr/bin/env python3

import os
import unittest

from constituent_counter.ConstituentCounter import ConstituentCounter
from constituent_counter.tests import ConstitutentCounterTestCase

class CountDitransitivesTestCase(ConstitutentCounterTestCase):
    def __init__(self, *args, **kwargs):
        super(CountDitransitivesTestCase, self).__init__(*args, **kwargs)
        self.ditransitive_base = os.path.join(self.resource_base, "ditransitive_verbs")

    def test_count_single_ditransitive(self):
        files = [os.path.join(self.ditransitive_base, "ditransitive1.txt")]
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_ditransitive_verbs(), 1)

    def test_nested_ditransitive(self):
        files = [os.path.join(self.ditransitive_base, "ditransitive2.txt")]
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_ditransitive_verbs(), 2)

    def test_count_tritransitive(self):
        files = [os.path.join(self.ditransitive_base, "ungrammatical_but_parseable.txt")]
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_ditransitive_verbs(), 0)

if __name__ == "__main__":
    unittest.main()