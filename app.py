from nltk.corpus import wordnet
import sys
from PyDictionary import PyDictionary

q = "cat"
lang = "eng"
if len(sys.argv) > 1:
    q = sys.argv[1]
if len(sys.argv) > 2:
    lang = sys.argv[2]


synonyms = []
antonyms = []
hyponyms = []
hypernyms = []
defines = []
examples = []

print("q", q)
print("lang", lang)

for syn in wordnet.synsets(q, lang=lang):
    # print(syn)
    defines.append(syn.definition())
    examples.append(syn.examples())
    for l in syn.lemmas():
        # if "_" not in l.name() and "-" not in l.name():
        synonyms.append(l.name())
        for ant in l.antonyms():
            antonyms.append(ant.name())
    for sub in syn.hyponyms():
        for lemma in sub.lemmas():
            hyponyms.append(lemma.name())
    for hyper in syn.hypernyms():
        for lemma in hyper.lemmas():
            hypernyms.append(lemma.name())

print("定義", defines)
print("上位概念", list(set(hypernyms)))
print("類義語", list(set(synonyms)))
print("対義語", list(set(antonyms)))
print("下位概念", list(set(hyponyms)))
print("用例", examples)


synsets = wordnet.synsets(q, lang=lang)
engword = ""
if len(synsets) > 0:
    if len(synsets[0].lemmas()) > 0:
        engword = synsets[0].lemmas()[len(synsets[0].lemmas()) - 1].name()

print("英語", engword)
dictionary = PyDictionary(engword)


print("日本語", dictionary.translateTo('jpn'))
print("フランス語", dictionary.translateTo('fr'))
print("ドイツ語", dictionary.translateTo('de'))
print("ラテン語", dictionary.translateTo('la'))
print("ギリシャ語", dictionary.translateTo('el'))
print("ロシア語", dictionary.translateTo('ru'))
print("韓国語", dictionary.translateTo('ko'))
print("中国語", dictionary.translateTo('zh'))
