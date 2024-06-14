from icecream import ic
import numpy as np


def levenshtein(source, target):
    dp = np.full((len(source) + 1, len(target) + 1), 0)

    # Insert distance
    for i in range(len(source) + 1):
        dp[i][0] = i

    # Delete distance
    for j in range(len(target) + 1):
        dp[0][j] = j

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            sub_cost = 0
            if source[i - 1] != target[j - 1]:
                sub_cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # delete cost
                           dp[i][j - 1] + 1,  # insert cost
                           dp[i - 1][j - 1] + sub_cost)  # sub_cost

    return dp[len(source)][len(target)]


if __name__ == "__main__":
    assert levenshtein("hi", "hello") == 4
    print(levenshtein("hola", "hello"))  # 3
