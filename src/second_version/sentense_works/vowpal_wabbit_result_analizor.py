from second_version.word_works.tokenizer import do_all_to_text, load_text
from second_version.word_works.normalizer import normalize_and_stem_text
from second_version.sentense_works.naive_bayes import naive_bayes_classify, get_root_of_sentence
from second_version.word_works.stop_word_deleter import delete_stop_words
import io


def read_result():
    result = load_text("pre.txt")
    return result.split("\n\n")


def precision(dict):
    return dict["TP"] / (dict["TP"] + dict["FP"])


def recall(dict):
    return dict["TP"] / (dict["TP"] + dict["FN"])


if __name__ == "__main__":
    reisi = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}
    rouhani = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}
    predicts = read_result()
    for i in range(len(predicts)):
        if i % 2 == 0:
            if "-" in predicts[i]:
                rouhani["TP"] += 1
                reisi["TN"] += 1
            else:
                rouhani["FN"] += 1
                reisi["FP"] += 1
        else:
            if not ("-" in predicts[i]):
                rouhani["TN"] += 1
                reisi["TP"] += 1
            else:
                rouhani["FP"] += 1
                reisi["FN"] += 1
    print("2 gram logistic loss after1")
    print("reisi: " + str(reisi))
    print("precision: " + str(precision(rouhani)))
    print("recall: " + str(recall(rouhani)))
    print("rouhani: " + str(rouhani))
    print("precision: " + str(precision(rouhani)))
    print("recall: " + str(recall(rouhani)))
