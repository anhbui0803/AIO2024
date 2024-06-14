from icecream import ic
file_path = "Module_1\\Week_2\\Homework\\data.txt"
# gdown.download(url, file_path)


def count_word(file_path):
    file = open(file_path, "r")
    word_list = file.read()
    counter = {}

    for word in word_list.split():
        word = word.lower()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    file.close()
    return counter


if __name__ == "__main__":
    res = count_word(file_path)
    assert res["who"] == 3
    print(res["man"])  # 6
