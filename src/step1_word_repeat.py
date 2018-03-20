#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import operator
import wordcloud
import re

from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words


def raw2repeat(path):
    FILENAME = path.split("/")[-1].split(".")[0]
    rawFile = io.open(path, 'r', encoding="utf-8")
    raw_word_repeat = {}

    for line in rawFile.readlines():
        line = line.replace(" ها ", "ها ")
        line = line.replace(" های ", "های ")
        line = line.replace(" می ", " می‌")
        line = line.replace(" نمی ", " نمی‌")
        line = line.replace("\n", "")
        if re.match(r".*[^،.!] ای .*", line) and not re.match(r".*[،.!] ای .*", line):
            line.replace(" ای", "‌ای")
        if "دستگاه" in line:
            print(line[line.index("دستگاه") - 5:line.index("دستگاه") + 15])
        for word in line.split(" "):
            raw_word_repeat[word] = raw_word_repeat.get(word, 0) + 1
    return raw_word_repeat
    # nltk.download()


def loadAllTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadFirstTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat
def loadSecondTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani2.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat
def loadThirdTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi3.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadMirsalimTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/mirsalim3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadRouhaniTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/rouhani3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadHashemi_tabaTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/hashemi_taba3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadJahangiriTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/jahangiri3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadGhalibafTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/ghalibaf3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def loadReisiTexts():
    main_word_repeat = {}
    raw_word_repeats = []
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi2.txt"))
    raw_word_repeats.append(raw2repeat("../resource/raw_data/reisi3.txt"))
    for raw_word_repeat in raw_word_repeats:
        main_word_repeat = {k: raw_word_repeat.get(k, 0) + main_word_repeat.get(k, 0) for k in
                            set(main_word_repeat) | set(raw_word_repeat)}
    return main_word_repeat


def remove_extra_words(raw_dict):
    pruned_itemsـno_rabt = {k: raw_dict.get(k) for k in set(raw_dict) if
                            k not in ["باری", "ولی", "هم", "نیز", "لیکن", "که", "زیرا", "خواه", "پس", "اما", "تا", "چه",
                                      "چون", "نه", "اگر", "پس", "یا", "و"]}
    pruned_itemsـno_rabt_no_ezafi = {k: raw_dict.get(k) for k in set(pruned_itemsـno_rabt) if
                                     k not in [" ", "نیز", "در", "با", "ترین", "تر", "برای", "از", "به", "را"]}
    return pruned_itemsـno_rabt_no_ezafi


def saveWordRepeat(sorted_list):
    bw = open("word_repeat", "w", encoding="utf8")
    for wordTuple in sorted_list:
        bw.write(wordTuple[0] + " " + str(wordTuple[1]) + "\n")
    bw.close()
def saveWordRepeatForWordCloud(sorted_list):
    bw = open("word_repeat_word_cloud", "w", encoding="utf8")
    for wordTuple in sorted_list:
        for i in range(wordTuple[1]):
            bw.write(wordTuple[0] + "\n")
    bw.close()


def create_word_cloud():
    f = open("word_repeat_word_cloud", encoding="utf8")
    text = f.read()

    stopwords = add_stop_words(['نیست'])
    stopwords = add_stop_words(['هست'])
    stopwords = add_stop_words(['می‌کنیم'])
    stopwords = add_stop_words(['کردند'])
    stopwords = add_stop_words(['کنید'])
    stopwords = add_stop_words(['می‌کنند'])
    stopwords = add_stop_words(['کردم'])
    stopwords = add_stop_words(['کردیم'])
    stopwords = add_stop_words(['داریم'])
    stopwords = add_stop_words(['کرده'])
    stopwords = add_stop_words(['کرد'])
    stopwords = add_stop_words(['می‌کند'])
    stopwords = add_stop_words(['می‌کنم'])
    stopwords = add_stop_words(['هستیم'])
    stopwords = add_stop_words(['کردید'])
    stopwords = add_stop_words(['کنیم'])
    stopwords = add_stop_words(['کنند'])
    stopwords = add_stop_words(['باشیم'])
    stopwords = add_stop_words(['کند'])
    stopwords = add_stop_words(['کند'])
    stopwords = add_stop_words(['می‌شود'])
    stopwords = add_stop_words(['می‌شویم'])
    stopwords = add_stop_words(['می‌شوید'])
    # Generate a word cloud image
    wordcloud = PersianWordCloud(
        only_persian=True,
        max_words=300,
        margin=0,
        width=1000,
        height=1000,
        min_font_size=1,
        collocations=False,
        max_font_size=500,
        stopwords=stopwords,
        background_color="black"
    ).generate(text)
    # Display the generated image:
    image = wordcloud.to_image()
    image.show()
    image.save('result.png')
    f.close()

main_word_repeat = loadRouhaniTexts()
# for word in main_word_repeat:
#     if"دستگاهاها" in word:
#         print(word)
root_word_repeat = {}
# ps = PersianStemmer()
for word in main_word_repeat.keys():
    # root_word = ps.run(word)
    root_word = word
    if not re.match(r"[\d*]،[\d*]", root_word):
        root_word = root_word.replace("،", "")
    if not re.match(r"[\d*]\.[\d*]", root_word):
        root_word = root_word.replace(".", "")
    root_word = root_word.replace("؟", "")
    root_word = root_word.replace("؛", "")
    root_word = root_word.replace(":", "")
    # if root_word != word:
    #     print(word + "-> " + root_word)
    # if re.match(r".*اید$",root_word):
    #     print(root_word)

    root_word_repeat[root_word] = root_word_repeat.get(root_word, 0) + main_word_repeat[word]

# for word in root_word_repeat.keys():
#     if "یم" in word:
#         print(word)
pruned_words = remove_extra_words(root_word_repeat)
sorted_x = sorted(pruned_words.items(), key=operator.itemgetter(1))
saveWordRepeat(sorted_x)
saveWordRepeatForWordCloud(sorted_x)
create_word_cloud()
# print(sorted_x)
