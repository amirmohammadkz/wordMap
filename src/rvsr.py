import operator

from second_version.word_works.tokenizer import do_all_to_text, load_text
from step1_word_repeat import saveWordRepeatForWordCloud, create_word_cloud,create_word_cloud


def createAandB(a, b):
    sum_a_b = a
    print(sum_a_b)
    for word in b.keys():
        sum_a_b[word] = sum_a_b.get(word, 0) - b[word]
    a_more = {x: sum_a_b[x] for x in sum_a_b.keys() if sum_a_b[x] > 0}
    b_more = {x: -sum_a_b[x] for x in sum_a_b.keys() if sum_a_b[x] < 0}
    return [a_more, b_more]


if __name__ == "__main__":
    rouhani = load_text("../resource/raw_data/rouhani_all.txt")
    rouhani = do_all_to_text(rouhani)
    reisi = load_text("../resource/raw_data/reisi_all.txt")
    reisi = do_all_to_text(reisi)
    result = createAandB(rouhani[1], reisi[1])
    sorted_rouhani = sorted(result[0].items(), key=operator.itemgetter(1))
    sorted_reisi = sorted(result[1].items(), key=operator.itemgetter(1))
    print(sorted_reisi)
    print(sorted_rouhani)
    saveWordRepeatForWordCloud(sorted_rouhani)
    create_word_cloud("rouhani_more.png")
    saveWordRepeatForWordCloud(sorted_reisi)
    create_word_cloud("reisi_more.png")
