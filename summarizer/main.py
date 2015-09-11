from parsers.pdf import converters
from feature_extraction.terms import Terms
from summarization.summarizers import GenericSummarizer

converter = converters.Converter("/Users/Kosta/PycharmProjects/pdf-sumy/CanadianHousingStarts_Apr2015.pdf")

text = converter.to_text()
html = converter.to_html()

terms = Terms(text)
sum = GenericSummarizer(num_sentences = 15, correction_ratio = 0.6)

print "--------Summary sentences"

for sentence in sum.summarize_html(html):
    print ("\n* " + sentence)

print "\n------Geographical Entities"
for geo in terms.get_geographical_entites():
    print geo

print "\n------Named Entities"
for ent in terms.get_named_entities():
    print ent

print "\n------Organizations"
for org in terms.get_organization_entites():
    print org
