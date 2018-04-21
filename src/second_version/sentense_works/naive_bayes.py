from second_version.word_works.tokenizer import do_all_to_text
from second_version.word_works.normalizer import normalize_and_stem_text
from second_version.word_works.stop_word_deleter import delete_stop_words


def naive_bayes_classify(sentence: str, bags_of_words: dict, alpha: bool):
    owner_prob = {}
    owner_total_word_count = {x: sum(bags_of_words[x].values()) for x in bags_of_words}
    for bag_owner in bags_of_words.keys():
        prob_of_bag_of_words = get_prob_in_bag(sentence, bags_of_words[bag_owner], alpha)
        prob_of_this_bag = owner_total_word_count[bag_owner] / sum(owner_total_word_count.values())
        owner_prob[bag_owner] = prob_of_bag_of_words * prob_of_this_bag
    print(owner_total_word_count)
    print({x: len(bags_of_words[x]) for x in bags_of_words})
    print(owner_prob)
    return owner_prob


def get_prob_in_bag(sentence: str, bag_of_words: dict, alpha: bool):
    probability = 1
    d = len(bag_of_words)
    if alpha:
        alpha = 1
    else:
        alpha = 0
    for word in sentence.split(" "):
        probability *= ((bag_of_words.get(word, 0) + alpha) / (sum(bag_of_words.values()) + d))
        # print(word)
        # print(probability)
    return probability


def get_root_of_sentence(sentence: str):
    result1 = do_all_to_text(sentence)
    result2 = normalize_and_stem_text(result1)
    result3 = delete_stop_words(result2)
    return result3[0]


if __name__ == "__main__":
    bags_of_words = {}
    bags_of_words["ali"] = {"hi": 1, "hello": 2}
    bags_of_words["hassan"] = {"bojoo": 20, "holoo": 500}
    input_sentence = input("your sentence:\n")
    naive_bayes_classify(get_root_of_sentence(input_sentence), bags_of_words, True)
