import nltk

class Terms(object):

    def __init__(self, text):

        tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)

        tree = nltk.ne_chunk(pos_tags)

        self.keywords = {}

        for t in tree.subtrees():
            key = t.label()
            children = t.leaves()

            lbl = ""

            for child in children:
                lbl = lbl + " " + child[0]

            if not key in self.keywords:
                self.keywords[key] = []

            if not lbl in self.keywords[key]:
                self.keywords[key].append(lbl)

    def get_geographical_entites(self):
        return self.keywords["GPE"]

    def get_named_entities(self):
        return self.keywords["PERSON"]

    def get_organization_entites(self):
        return self.keywords["ORGANIZATION"]