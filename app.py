from nltk.corpus import wordnet
import sys
from translate import Translator

q = "cat"
lang = "eng"
if len(sys.argv) > 1:
    q = sys.argv[1]
if len(sys.argv) > 2:
    lang = sys.argv[2]


translator = Translator(to_lang="jpn", from_lang=lang)
translation = translator.translate(q)
print("日本語", translation)

translator = Translator(to_lang="en", from_lang=lang)
translation = translator.translate(q)
print("英語", translation)
engword = translation

translator = Translator(to_lang="fr", from_lang=lang)
translation = translator.translate(q)
print("フランス語", translation)

translator = Translator(to_lang="de", from_lang=lang)
translation = translator.translate(q)
print("ドイツ語", translation)

translator = Translator(to_lang="la", from_lang=lang)
translation = translator.translate(q)
print("ラテン語", translation)

translator = Translator(to_lang="el", from_lang=lang)
translation = translator.translate(q)
print("ギリシャ語", translation)


translator = Translator(to_lang="ru", from_lang=lang)
translation = translator.translate(q)
print("ロシア語", translation)

translator = Translator(to_lang="ko", from_lang=lang)
translation = translator.translate(q)
print("韓国語", translation)

translator = Translator(to_lang="zh", from_lang=lang)
translation = translator.translate(q)
print("中国語", translation)

synonyms = []
antonyms = []
hyponyms = []
hypernyms = []
defines = []
examples = []

print("q", q)
print("lang", lang)

for syn in wordnet.synsets(engword):
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
