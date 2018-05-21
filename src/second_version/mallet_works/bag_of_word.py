from word_map.src.second_version.word_works.tokenizer import load_text, do_all_to_text, do_all_to_text2
from word_map.src.second_version.word_works.normalizer import normalize_and_stem_text, normalize_and_stem_text2
from word_map.src.second_version.word_works.stop_word_deleter import delete_stop_words


def train_once():
    yaroo_bag = {}
    yaroo_list = ["mirsalim", "hashemi_taba", "reisi", "jahangiri", "rouhani", "ghalibaf"]
    for yaroo in yaroo_list:
        yaroo_text = load_text("../../../resource/raw_data/" + yaroo + "_all_train.txt")
        yaroo_tokeni = do_all_to_text2(yaroo_text)
        yaroo_normali = normalize_and_stem_text2(yaroo_tokeni)
        yaroo_cleani = delete_stop_words(yaroo_normali)
        yaroo_bag[yaroo] = yaroo_cleani[0]

    return [yaroo_list, yaroo_bag]


def write_mallet_form(bog):
    i = 0
    bw = open("both.txt", "w", encoding="utf8")

    for name in ['rouhani', 'reisi']:
        for word in bog[name].keys():
            print(word)
            if (len(word) > 1):
                bw.write("instance" + str(i) + " " + name + " word " + word + "\n")
                i += 1
    bw.close()


def write_mallet_form_sentence(sentences):
    i = 0
    bw = open("both.txt", "w", encoding="utf8")

    for name in ['rouhani', 'reisi']:
        for line in sentences[name]:
            print(line)
            if len(line) > 5:
                bw.write("instance" + str(i) + " " + name + " " + line + "\n")
                i += 1
    bw.close()


def write_mallet_form_all():
    i = 0
    bw = open("both.txt", "w", encoding="utf8")

    for name in ['rouhani', 'reisi']:
        yaroo_text = load_text("../../../resource/raw_data/" + name + "_all.txt")
        for word in yaroo_text.split("\n"):
            print(word)
            if (len(word) > 1):
                bw.write("instance" + str(i) + " " + name + " " + word + "\n")
                i += 1
    bw.close()


if __name__ == "__main__":
    trained = train_once()
    print(trained[1]["rouhani"])
    print(trained[1]["reisi"])
    write_mallet_form_sentence({"rouhani": trained[1]['rouhani'], "reisi": trained[1]['reisi']})
    # write_mallet_form(trained[0])
    # write_mallet_form_sentence(trained[1])
    # write_mallet_form_all()
