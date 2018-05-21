# token token konim kalamato ba space mani ham bede
import io
import operator
import re


def load_text(text_path):
    text = io.open(text_path, 'r', encoding="utf-8")
    result = ""
    for line in text.readlines():
        result += line + "\n"
    return result


def replace_space_with_nimspace(text):
    text = text.replace(" ها ", "ها ")
    text = text.replace(" های ", "های ")
    text = text.replace(" می ", " می‌")
    text = text.replace(" نمی ", " نمی‌")
    text = text.replace("\n", " . ")
    text = text.replace("\r", " . ")
    # todo fix ای
    # if re.match(r".*[^،.!] ای .*", text) and not re.match(r".*[،.!] ای .*", text):
    #     text.replace(" ای", "‌ای")
    # if "دستگاه" in text:
    #     print(text[text.index("دستگاه") - 5:text.index("دستگاه") + 15])
    return text


def save_word_repeat(sorted_list):
    bw = open("word_repeat", "w", encoding="utf8")
    for wordTuple in sorted_list:
        bw.write(wordTuple[0] + " " + str(wordTuple[1]) + "\n")
    bw.close()


def text2token(text):
    raw_word_repeat = {}
    for word in text.split(" "):
        raw_word_repeat[word] = raw_word_repeat.get(word, 0) + 1
    if "" in raw_word_repeat.keys():
        del raw_word_repeat[""]
    return raw_word_repeat


def remove_extras_from_token(word_repeat_dic):
    root_word_repeat = {}
    # ps = PersianStemmer()
    for word in word_repeat_dic.keys():
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

        root_word_repeat[root_word] = root_word_repeat.get(root_word, 0) + word_repeat_dic[word]
    return root_word_repeat


# text = load_text("../../../resource/raw_data/ghalibaf.txt")

def do_all_to_text(text):
    text_nimspace_ok = replace_space_with_nimspace(text)
    word_repeat = text2token(text_nimspace_ok)
    word_repeat_no_extra = remove_extras_from_token(word_repeat)
    return [text_nimspace_ok, word_repeat_no_extra]


def do_all_to_text2(text):
    text_nimspace_ok = replace_space_with_nimspace(text)
    word_repeat = text2token(text_nimspace_ok)
    word_repeat_no_extra = remove_extras_from_token(word_repeat)
    return [text_nimspace_ok.split("."), word_repeat_no_extra]


if __name__ == "__main__":
    text = load_text("../../../resource/raw_data/ghalibaf.txt")
    text_nimspace_ok = replace_space_with_nimspace(text)
    word_repeat = text2token(text_nimspace_ok)
    word_repeat_no_extra = remove_extras_from_token(word_repeat)
    print(text)
    print(text_nimspace_ok)
    # print([f for f in word_repeat if "." in f])
    print(word_repeat)
    print(word_repeat_no_extra)
    sorted_x = sorted(word_repeat_no_extra.items(), key=operator.itemgetter(1))
    save_word_repeat(sorted_x)
