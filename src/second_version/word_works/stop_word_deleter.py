from second_version.word_works.tokenizer import load_text


def delete_stop_words(normalized):
    text = normalized[0]
    word_repeat = normalized[1]
    stop_words = read_stop_words()
    word_repeat_no_useless = {}
    for word in word_repeat.keys():
        if word in stop_words:
            text = text.replace(word, "")
        else:
            word_repeat_no_useless[word] = word_repeat.get(word)
    return [text, word_repeat_no_useless]


def read_stop_words():
    f = load_text("../../../resource/utils/stopwords_big.txt")
    res = []
    for line in f.rsplit("\n"):
        res.append(line)
    return res


if __name__ == "__main__":
    test = ["سلام از تو به من می‌رسد. ما چقدر مفصلیم.", {"سلام": 1, "از": 1, "به": 1, "مفصلیم": 1}]
    test_res = delete_stop_words(test)
    print(test_res)
