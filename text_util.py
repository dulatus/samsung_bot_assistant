# -*- coding: utf-8 -*-
import nltk
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
def pos_tag(tokens):
    """
    Use NLTK's currently recommended part of speech tagger to
    tag the given list of tokens.
 
        >>> from nltk.tag import pos_tag # doctest: +SKIP
        >>> from nltk.tokenize import word_tokenize # doctest: +SKIP
        >>> pos_tag(word_tokenize("John's big idea isn't all that bad.")) # doctest: +SKIP
        [('John', 'NNP'), ("'s", 'POS'), ('big', 'JJ'), ('idea', 'NN'), ('is',
        'VBZ'), ("n't", 'RB'), ('all', 'DT'), ('that', 'DT'), ('bad', 'JJ'),
        ('.', '.')]
 
    :param tokens: Sequence of tokens to be tagged
    :type tokens: list(str)
    :return: The tagged tokens
    :rtype: list(tuple(str, str))
    """
    tagger = load(_POS_TAGGER)
    return tagger.tag(tokens)
def	text_proc(sentence)
		tokens =  word_tokenize(sentence)
		tagged = pos_tag(tokens)
		print(tokens)

