from second_version.word_works.tokenizer import do_all_to_text, load_text
from second_version.word_works.normalizer import normalize_and_stem_text
from second_version.sentense_works.naive_bayes import naive_bayes_classify, get_root_of_sentence
from second_version.word_works.stop_word_deleter import delete_stop_words
import io


def generate_train():
    # resi = io.open("reisi_all_train.txt", encoding="utf8")
    yaroo_text = load_text("reisi_all_train.txt")
    yaroo_tokeni = do_all_to_text(yaroo_text)
    yaroo_normali = normalize_and_stem_text(yaroo_tokeni)
    yaroo_cleani = delete_stop_words(yaroo_normali)
    # print(yaroo_normali[0])
    reisi = [i for i in yaroo_normali[0].split(" . ") if len(i) > 2]
    print(len(reisi))

    yaroo_text = load_text("rouhani_all_train.txt")
    yaroo_tokeni = do_all_to_text(yaroo_text)
    yaroo_normali = normalize_and_stem_text(yaroo_tokeni)
    yaroo_cleani = delete_stop_words(yaroo_normali)
    rouhani = [i for i in yaroo_normali[0].split(" . ") if len(i) > 2]
    print(len(rouhani))
    txt = ""
    for i in range(min(len(rouhani), len(reisi))):
        txt += "-1 'rouhani | " + rouhani[i] + "\n"
        txt += "1 'reisi | " + reisi[i] + "\n"
    print(txt)
    f = open("vowpal_train.vw", "w", encoding="utf8")
    f.write(txt)
    f.close()


def generate_test():
    # resi = io.open("reisi_all_train.txt", encoding="utf8")
    yaroo_text = load_text("reisi_all_test.txt")
    yaroo_tokeni = do_all_to_text(yaroo_text)
    yaroo_normali = normalize_and_stem_text(yaroo_tokeni)
    yaroo_cleani = delete_stop_words(yaroo_normali)
    # print(yaroo_normali[0])
    reisi = [i for i in yaroo_tokeni[0].split(" . ") if len(i) > 2]
    print(len(reisi))

    yaroo_text = load_text("rouhani_all_test.txt")
    yaroo_tokeni = do_all_to_text(yaroo_text)
    yaroo_normali = normalize_and_stem_text(yaroo_tokeni)
    yaroo_cleani = delete_stop_words(yaroo_normali)
    rouhani = [i for i in yaroo_tokeni[0].split(" . ") if len(i) > 2]
    print(len(rouhani))
    txt = ""
    for i in range(min(len(rouhani), len(reisi))):
        txt += "-1 'rouhani | " + rouhani[i] + "\n"
        txt += "1 'reisi | " + reisi[i] + "\n"
    print(txt)
    f = open("vowpal_test.vw", "w", encoding="utf8")
    f.write(txt)
    f.close()


if __name__ == "__main__":
    generate_train()
    generate_test()
