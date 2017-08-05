#!/usr/bin/env python3

import os
import nltk_tgrep as tgrep
from nltk import SExprTokenizer
from nltk.tree import ParentedTree

class ConstituentCounter(object):
    def __init__(self, files, _dir=None):
        self.files = files
        self._tokenizer = SExprTokenizer()
        self.abs_path_to_dir = _dir

        # list comprehension isn't really working here... weird. Maybe because `self._parse_trees`
        # is side-effectful.
        self.trees = []
        for file in self.files:
            trees = self._parse_trees(file)
            for tree in trees:
                self.trees.append(tree)

    @classmethod
    def from_directory(cls, _dir):
        abs_path_to_dir = os.path.abspath(_dir)
        files = [
            os.path.join(abs_path_to_dir, f) for f in os.listdir(abs_path_to_dir)
            if os.path.isfile(os.path.join(abs_path_to_dir, f))
        ]
        return ConstituentCounter(files, abs_path_to_dir)

    def _parse_trees(self, file):
        with open(file, 'r') as f:
            lines = ''.join(map(str.strip, f.readlines()))

        s_expressions = self._tokenizer.tokenize(lines)
        trees = [ParentedTree.fromstring(s_expr) for s_expr in s_expressions]
        return trees

    def _count(self, tgrep_pattern):
        # Sums the number of nodes matching a tgrep pattern in each tree.
        return sum(len(tgrep.tgrep_nodes(tree, tgrep_pattern)) for tree in self.trees)

    def _count_filter(self, tgrep_pattern, filt):
        # Applies a filter to all the nodes matching a tgrep pattern in a tree and counts those matching the filter.
        # All matches from each tree is summed and returned.
        return sum(sum(1 for _ in filter(filt, tgrep.tgrep_nodes(tree, tgrep_pattern))) for tree in self.trees)

    def count_sentences(self):
        # Count all clauses
        return self._count("S")

    def count_noun_phrases(self):
        # Count all noun phrases
        return self._count("NP")

    def count_verb_phrases(self):
        # Count all verb prases
        return self._count("VP")

    def count_ditransitive_verbs(self):
        # Find all verbs with two noun-phrase siblings as children.
        # To prevent false-positives, we filter on those whose
        # only constituents are a verb and the two noun phrase children (hence length three)
        return self._count_filter("VP < (NP $ NP)", lambda t: len(t) == 3)

    def count_intransitive_verbs(self):
        # Find verb phrases whose subtrees are of length one (length one because the verb
        # is a subtree)
        return self._count_filter("VP", lambda x: len(list(x.subtrees())) == 1)
