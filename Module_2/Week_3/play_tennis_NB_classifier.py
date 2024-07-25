import numpy as np
from icecream import ic


# 4.1
def create_train_data():
    data = [
        ["Sunny", "Hot", "High", "Weak", "no"],
        ["Sunny", "Hot", "High", "Strong", "no"],
        ["Overcast", "Hot", "High", "Weak", "yes"],
        ["Rain", "Mild", "High", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Strong", "no"],
        ["Overcast", "Cool", "Normal", "Strong", "yes"],
        ["Overcast", "Mild", "High", "Weak", "no"],
        ["Sunny", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Mild", "Normal", "Weak", "yes"]
    ]
    return np.array(data)


# 4.2
def compute_prior_prob(train_data):
    y_unique = ["no", "yes"]
    prior_prob = np.zeros(len(y_unique))

    prior_prob[0] = np.sum(train_data[:, -1] == "no") / len(train_data)
    prior_prob[1] = np.sum(train_data[:, -1] == "yes") / len(train_data)

    return prior_prob


# 4.3
def compute_conditional_prob(train_data):
    y_unique = ["no", "yes"]
    conditional_prob = []
    list_x_name = []
    y = train_data[:, -1]

    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_prob = []

        for val in x_unique:
            val_probs = []

            for label in y_unique:
                cnt_label = np.sum(y == label)
                cnt_val_given_label = np.sum(
                    (y == label) & (train_data[:, i] == val)
                )
                val_prob = cnt_val_given_label / cnt_label
                val_probs.append(val_prob)

            x_conditional_prob.append(val_probs)

        conditional_prob.append(x_conditional_prob)

    return conditional_prob, list_x_name


# 4.4
def get_index_from_val(feature_name, list_features):
    return np.nonzero(list_features == feature_name)[0][0]


# 4.5
def train_naive_bayes(train_data):
    # Step 1: Calculate prior prob
    prior_prob = compute_prior_prob(train_data)

    # Step 2: Calculate conditional prob
    conditional_prob, list_x_name = compute_conditional_prob(
        train_data
    )

    return prior_prob, conditional_prob, list_x_name


# 4.6
def prediction_play_tennis(X, prior_prob, conditional_prob, list_x_name):
    x1 = get_index_from_val(X[0], list_x_name[0])
    x2 = get_index_from_val(X[1], list_x_name[1])
    x3 = get_index_from_val(X[2], list_x_name[2])
    x4 = get_index_from_val(X[3], list_x_name[3])

    prob_no = conditional_prob[0][x1][0] * \
        conditional_prob[1][x2][0] * \
        conditional_prob[2][x3][0] * \
        conditional_prob[3][x4][0] * \
        prior_prob[0]

    prob_yes = conditional_prob[0][x1][1] * \
        conditional_prob[1][x2][1] * \
        conditional_prob[2][x3][1] * \
        conditional_prob[3][x4][1] * \
        prior_prob[1]

    ic(prob_no, prob_yes)
    if prob_no > prob_yes:
        return 0

    return 1


if __name__ == '__main__':
    train_data = create_train_data()

    # Cau 14 -> A
    print("------------------- Cau 14 ---------------------")
    prior_prob = compute_prior_prob(train_data)
    ic(prior_prob)

    # Cau 15 -> B
    print("------------------- Cau 15 ---------------------")
    conditional_prob, list_x_name = compute_conditional_prob(
        train_data
    )
    ic(conditional_prob)

    # Cau 16 -> C
    print("------------------- Cau 16 ---------------------")
    outlook = list_x_name[0]
    i1 = get_index_from_val("Overcast", outlook)
    i2 = get_index_from_val("Rain", outlook)
    i3 = get_index_from_val("Sunny", outlook)
    ic(i1, i2, i3)

    # Cau 17 -> D
    print("------------------- Cau 17 ---------------------")
    sunny_index = get_index_from_val("Sunny", list_x_name[0])
    print("P(Outlook = Sunny | Yes) = ",
          np.round(conditional_prob[0][sunny_index][1], 2))

    # Cau 18 -> A
    print("------------------- Cau 18 ---------------------")
    print("P(Outlook = Sunny | No) = ",
          np.round(conditional_prob[0][sunny_index][0], 2))

    # Cau 19 -> A
    print("------------------- Cau 19 ---------------------")
    X = ["Sunny", "Cool", "High", "Strong"]
    pred = prediction_play_tennis(X, prior_prob, conditional_prob, list_x_name)

    if pred:
        print("Ad should go!")
    else:
        print("Ad should not go!")
