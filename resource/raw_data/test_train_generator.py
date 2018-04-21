import io
from random import shuffle


def generate(pish=""):
    x = ["mirsalim", "ghalibaf", "hashemi_taba", "jahangiri", "reisi", "rouhani"]
    result = ""

    for namzad in x:
        file = io.open(pish + namzad + "_all.txt", encoding="utf8")
        result = file.read().split(".")[:-1]
        shuffle(result)
        test = result[:int(len(result) / 10)]
        train = result[int(len(result) / 10):]
        print(len(result))
        print(len(train))
        print(len(test))
        bw = open(pish + namzad + "_all_train.txt", "w", encoding="utf8")
        for i in train:
            bw.write(i)
            bw.write("\n")
        bw.close()
        bw = open(pish + namzad + "_all_test.txt", "w", encoding="utf8")
        for i in test:
            bw.write(i)
            bw.write("\n")
        bw.close()


if __name__ == "__main__":
    generate()
