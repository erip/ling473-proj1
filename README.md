# Project 1

## Task

Given a directory containing an annotated corpus, write a program to count the number of syntactic constituent types
that occur.

## Results

The results for the above task were:

| Constituent        | PTB symbol           | Count  |
| ------------- |:-------------:| -----:|
| Sentence      | (S ...) | 4670 |
| Noun Phrase      | (NP ...)      |   13221|
| Verb Phrase | (VP ...)      |    7920|
| Ditransitive Verb Phrase | (VP verb (NP ...) (NP ...)) | 33 |
| Intransitive Verb Phrase  | (VP verb) | 123 |

## Approach

Because each file within the corpus contains some number of s-expressions, I knew I would be able to parse each s-expression into a tree and traverse the tree, counting the tags on the nodes of the trees. For several of these constituent types, the count is a simple check for number of nodes with the appropriate tags. For other tags which actually require attention to syntactic structure, it became necessary to check the subtrees of nodes whose top-level tags matched.

## Tools

For this project, I used two third-party tools to facilitate parsing and traversing the tree structures: nltk and nltk-tgrep.

nltk is a suite of basic natural language processing facilities including stemming, tokenizing, PoS tagging. nltk also includes classes for parsing s-expressions and creating parented tree structures from them. These two classes saved me time from writing my own recursive parser to build the trees.

nltk-tgrep is a pseudo-port of a famous tree parsing tool developed by MIT, tgrep2, which was built for a grep-like API to search for elements in s-expression trees. nltk-tgrep works specifically with nltk's `ParentedTree`s, which I leveraged to parse the s-expressions.

## Testing

Unit tests were written to cover the "tricky" cases (i.e., those where the physical structure of the tree is important) and a general case where only tag-counts are important. These tests can be run from the project root by issuing `./test.sh` and found in the `constitutent_counter/tests/` directory along with example (and often ungrammatical) corpora.

## To do

The API could always be more clean and more tests could always be written, but currently the implementation is both clean and functional enough.
