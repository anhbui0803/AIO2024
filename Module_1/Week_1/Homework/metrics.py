def validate_input(name, val):
    if not isinstance(val, int):
        return f"{name} must be int"
    if val <= 0:
        return "tp and fp and fn must be greater than zero"
    return None


def calc_f1_score(tp, fp, fn):
    for name, val in [("tp", tp), ("fp", fp), ("fn", fn)]:
        error_msg = validate_input(name, val)
        if error_msg is not None:
            print(error_msg)
            return 0

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = (2 * precision * recall) / (precision + recall)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")
    return f1_score


if __name__ == "__main__":
    # calc_f1_score(tp=2, fp=3, fn=4)
    # calc_f1_score(tp="a", fp=2, fn=5)
    # calc_f1_score(tp=2.5, fp=10, fn=3)
    # calc_f1_score(tp=6, fp=0, fn=2)
    assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
    print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))  # 0.31
