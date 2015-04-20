import langid
import re
import nltk

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

class Converter(object):

    def __init__(self, path, _codec='utf-8', _password='', _maxpages=0, _caching=True):
        self.rsrcmgr = PDFResourceManager()
        self.codec = _codec
        self.password = _password
        self.maxpages = _maxpages
        self.caching = _caching
        self.path = path
        self.laparams = LAParams()
        self.pagenos = set()

    def __convert(self, device):
        interpreter = PDFPageInterpreter(self.rsrcmgr, device)
        fp = file(self.path, 'rb')
        for page in PDFPage.get_pages(fp, self.pagenos, maxpages=self.maxpages, password=self.password,
                                      caching=self.caching, check_extractable=True):
            interpreter.process_page(page)

        text = self.retstr.getvalue()
        self.retstr.close()
        return text

    def __post_process(self, text):
        text = text.replace('\n', ' ').replace('\r', '')
        text = re.sub(r'[^\x00-\x7f]',r' ',text)
        text = re.sub("\s+"," ",text)

        clean_text = ""

        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        for sentence in sent_detector.tokenize(text.strip()):
            classify_results = langid.classify(sentence)
            lang = classify_results[0]
            prob = classify_results[1]
            if (lang == 'en' and prob > 0.999):
                clean_text+=sentence + " "

        return clean_text

    def to_html(self):
        self.retstr = StringIO()
        device = HTMLConverter(self.rsrcmgr, self.retstr, codec=self.codec, laparams=self.laparams)
        return self.__convert(device)

    def to_text(self, post_process=True):
        self.retstr = StringIO()
        device = TextConverter(self.rsrcmgr, self.retstr, codec=self.codec, laparams=self.laparams)
        text = self.__convert(device)

        if(post_process):
            text = self.__post_process(text)

        return text