def divisible_by_3(num_list):
    var = []
    for num in num_list:
        # Your code here
        # num % 3 == 0 thi var.append(num)
        if num % 3 == 0:
            var.append(num)

    return var


if __name__ == '__main__':
    assert divisible_by_3([3, 9, 4, 5]) == [3, 9]
    print(divisible_by_3([1, 2, 3, 5, 6]))  # [3, 6]
