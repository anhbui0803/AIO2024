def check_the_number(num):
    num_list = []
    res = ""
    for i in range(1, 5):
        # Your code here
        # append i vao num_list
        num_list.append(i)
    if num in num_list:
        res = "True"
    if num not in num_list:
        res = "False"

    return res


if __name__ == "__main__":
    assert check_the_number(7) == "False"
    print(check_the_number(2))  # True
