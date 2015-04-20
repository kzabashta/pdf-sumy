__author__ = 'zabashk'

import re

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

class GenericSummarizer(object):

    def __init__(self, num_sentences = 10, correction_ratio = 0.6, lang = "english"):
        self.num_sentences = num_sentences
        self.correction_ratio = correction_ratio
        self.lang = lang

    def __summarize(self, content, parser):
        stemmer = Stemmer(self.lang)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(self.lang)

        total = int(self.num_sentences * self.correction_ratio)
        counter = 0

        summary = []

        for sentence in summarizer(parser.document, self.num_sentences):
            text = str(sentence)
            text = text.replace('\n', ' ').replace('\r', '')
            text = re.sub(r'[^\x00-\x7f]',r' ',text)
            text = re.sub("\s+"," ",text)

            summary.append(text)

            counter = counter + 1

            if counter > total:
                break

        return summary

    def summarize_html(self, content):
        parser = HtmlParser.from_string(content, "", Tokenizer(self.lang))
        return self.__summarize(content, parser)

    def summarize_text(self, content):
        parser = PlaintextParser.from_string(content, Tokenizer(self.lang))
        return self.__summarize(content, parser)