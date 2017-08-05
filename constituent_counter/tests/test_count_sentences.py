#!/usr/bin/env python3

import os
import unittest

from constituent_counter.ConstituentCounter import ConstituentCounter
from constituent_counter.tests import ConstitutentCounterTestCase


class CountSentencesTestCase(ConstitutentCounterTestCase):
    def __init__(self, *args, **kwargs):
        super(CountSentencesTestCase, self).__init__(*args, **kwargs)
        self.sent_base = os.path.join(self.resource_base, "sents")

    def test_count_sentences(self):
        # Each tree in ./test_corpora/sents/multiple_trees.txt has 1 S
        files = [os.path.join(self.sent_base, "multiple_trees.txt")]
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_sentences(), 3)

    def test_count_sentences_two_files(self):
        # Each tree in ./test_corpora/sents/*.txt has 1 S
        files = (os.path.join(self.sent_base, f) for f in ("multiple_trees.txt", "test_second.txt"))
        counter = ConstituentCounter(files)
        self.assertEqual(counter.count_sentences(), 4)

if __name__ == "__main__":
    unittest.main()