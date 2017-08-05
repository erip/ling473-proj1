#!/usr/bin/env python3

from constituent_counter import ConstituentCounter

if __name__ == "__main__":
    _dir = "/corpora/LDC/LDC99T42/RAW/parsed/prd/wsj/14"
    counter = ConstituentCounter.from_directory(_dir)
    abs_path = counter.abs_path_to_dir

    count = {
        "sentences": counter.count_sentences,
        "noun phrases": counter.count_noun_phrases,
        "verb phrases": counter.count_verb_phrases,
        "ditransitive verbs": counter.count_ditransitive_verbs,
        "intransitive verbs": counter.count_intransitive_verbs
    }

    for to_count, f in count.items():
        print("There are {0} {1} in {2}".format(f(), to_count, abs_path))