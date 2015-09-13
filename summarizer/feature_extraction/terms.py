import nltk

class Terms(object):

    GEOGRAPHICAL_ENTITIES_KEY = "GPE"
    NAMED_ENTITIES_KEY = "PERSON"
    ORGANIZATTION_ENTITES_KEY = "ORGANIZATION"

    def __init__(self, text):

        tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)

        tree = nltk.ne_chunk(pos_tags)

        self.keywords = {}

        for term in tree.subtrees():
            key = term.label()
            children = term.leaves()

            lbl = ""

            for child in children:
                lbl = lbl + " " + child[0]

            if not key in self.keywords:
                self.keywords[key] = []

            if not lbl in self.keywords[key]:
                self.keywords[key].append(lbl)

    def get_geographical_entites(self):
        return self.keywords[self.GEOGRAPHICAL_ENTITIES_KEY]

    def get_named_entities(self):
        return self.keywords[self.NAMED_ENTITIES_KEY]

    def get_organization_entites(self):
        return self.keywords[self.ORGANIZATTION_ENTITES_KEY]