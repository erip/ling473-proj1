#!/usr/bin/env python3

import os
import unittest

from constituent_counter.ConstituentCounter import ConstituentCounter
from constituent_counter.tests import ConstitutentCounterTestCase


class CountIntransitivesTestCase(ConstitutentCounterTestCase):
    def __init__(self, *args, **kwargs):
        super(CountIntransitivesTestCase, self).__init__(*args, **kwargs)
        self.intransitive_base = os.path.join(self.resource_base, "intransitive_verbs")

    def test_count_single_intransitive(self):
        files = [os.path.join(self.intransitive_base, "intransitive1.txt")]
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_intransitive_verbs(), 1)

    def test_not_count_false_single_intransitive(self):
        files = [os.path.join(self.intransitive_base, "intransitive2.txt")]
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_intransitive_verbs(), 0)

if __name__ == "__main__":
    unittest.main()