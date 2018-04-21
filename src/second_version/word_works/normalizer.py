# jam ha va ... ro yeki konim
import operator

import polyglot
from PersianStemmer import PersianStemmer
from polyglot.text import Text, Word

from second_version.word_works.tokenizer import do_all_to_text

def save_normalized_word_repeat(sorted_list):
    bw = open("normalized_word_repeat", "w", encoding="utf8")
    for wordTuple in sorted_list:
        bw.write(wordTuple[0] + " " + str(wordTuple[1]) + "\n")
    bw.close()
def normalize_and_stem_text(tokenizered):
    word_repeat = tokenizered[1]
    text = tokenizered[0]
    before_after = {k: None for k in word_repeat.keys()}
    ps = PersianStemmer()
    for item in before_after.keys():
        before_after[item] = ps.run(item)
        # if before_after[item] != item:
        #     print(item + "-> " + before_after[item])
    for item in before_after.keys():
        text = text.replace(item, before_after[item])

    word_normalized_result = {}
    for item in before_after.keys():
        word_normalized_result[before_after[item]] = word_normalized_result.get(before_after[item], 0) + word_repeat[
            item]
    return [text, word_normalized_result]

if __name__ == "__main__":
    tokenizered = do_all_to_text("../../../resource/raw_data/ghalibaf.txt")
    normalized_text = normalize_and_stem_text(tokenizered)
    print(tokenizered[0])
    print(tokenizered[1])
    print(normalized_text[1])
    sorted_x = sorted(normalized_text[1].items(), key=operator.itemgetter(1))
    save_normalized_word_repeat(sorted_x)
