from nltk.corpus import wordnet
import sys
from translate import Translator

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

translator = Translator(to_lang="jpn", from_lang="en")
translation = translator.translate(engword)
print("日本語", translation)

translator = Translator(to_lang="fr", from_lang="en")
translation = translator.translate(engword)
print("フランス語", translation)

translator = Translator(to_lang="de", from_lang="en")
translation = translator.translate(engword)
print("ドイツ語", translation)

# translator = Translator(to_lang="la", from_lang="en")
# translation = translator.translate(engword)
# print("ラテン語", translation)

translator = Translator(to_lang="el", from_lang="en")
translation = translator.translate(engword)
print("ギリシャ語", translation)


translator = Translator(to_lang="ru", from_lang="en")
translation = translator.translate(engword)
print("ロシア語", translation)

translator = Translator(to_lang="ko", from_lang="en")
translation = translator.translate(engword)
print("韓国語", translation)

translator = Translator(to_lang="zh", from_lang="en")
translation = translator.translate(engword)
print("中国語", translation)