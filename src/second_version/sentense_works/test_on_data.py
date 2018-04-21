from second_version.word_works.tokenizer import do_all_to_text, load_text
from second_version.word_works.normalizer import normalize_and_stem_text
from second_version.sentense_works.naive_bayes import naive_bayes_classify, get_root_of_sentence
from second_version.word_works.stop_word_deleter import delete_stop_words
from resource.raw_data.test_train_generator import generate
import operator


def test_once(yaroo_list, yaroo_bag):
    yaroo_test = {}
    for yaroo in yaroo_list:
        print("yaroo:" + yaroo)
        yaroo_test[yaroo] = {}
        file = load_text("../../../resource/raw_data/" + yaroo + "_all_test.txt")
        # sentence = input("your sentence: ")
        for sentence in file.split("\n"):
            if sentence == "":
                continue
            sentence = get_root_of_sentence(sentence)
            print(sentence)
            result = naive_bayes_classify(sentence, yaroo_bag, True)
            print("result:" + str(result))
            final_res = max(result.items(), key=operator.itemgetter(1))[0]
            yaroo_test[yaroo][final_res] = yaroo_test[yaroo].get(final_res, 0) + 1
            print(final_res)
    print(yaroo_test)
    return yaroo_test


def print_accuracy(count_dict):
    for yaroo in count_dict.keys():
        print(yaroo + ":" + str(count_dict[yaroo].get(yaroo, 0) * 100 / sum(count_dict[yaroo].values())))


def train_once():
    yaroo_bag = {}
    yaroo_list = ["mirsalim", "hashemi_taba", "reisi", "jahangiri", "rouhani", "ghalibaf"]
    for yaroo in yaroo_list:
        yaroo_text = load_text("../../../resource/raw_data/" + yaroo + "_all_train.txt")
        yaroo_tokeni = do_all_to_text(yaroo_text)
        yaroo_normali = normalize_and_stem_text(yaroo_tokeni)
        yaroo_cleani = delete_stop_words(yaroo_normali)
        yaroo_bag[yaroo] = yaroo_cleani[1]

    return [yaroo_list, yaroo_bag]


if __name__ == "__main__":
    result = []
    sum_result = {}
    n = 1
    for i in range(10):
        generate("../../../resource/raw_data/")
        res = train_once()
        result.append(test_once(res[0], res[1]))
    for test_case in result:
        for namzad in test_case.keys():
            print(namzad)
            sum_result[namzad] = sum_result.get(namzad, {})
            for choices in test_case[namzad].keys():
                print(test_case[namzad])
                sum_result[namzad][choices] = sum_result[namzad].get(choices, 0) + test_case[namzad][choices]

print(sum_result)
# print("accuracy:")
# print_accuracy(sum_result)
yaroo_list = ["mirsalim", "hashemi_taba", "reisi", "jahangiri", "rouhani", "ghalibaf"]

precision = {}
for yaroo in yaroo_list:
    is_yaroo = sum_result[yaroo].get(yaroo, 0)
    all_yaroo = 0
    for yaroo2 in yaroo_list:
        all_yaroo += sum_result[yaroo2].get(yaroo, 0)
    precision[yaroo] = is_yaroo / all_yaroo
print("precisions:")
for i in precision.keys():
    print(str(i) + ": " + str(precision[i]))

recall = {}
for yaroo in yaroo_list:
    is_yaroo = sum_result[yaroo].get(yaroo, 0)
    all_yaroo = sum(sum_result[yaroo].values())
    recall[yaroo] = is_yaroo / all_yaroo
print("recall:")
for i in recall.keys():
    print(str(i) + ": " + str(recall[i]))
#
