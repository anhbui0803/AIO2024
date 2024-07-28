# Download dataset: !gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq
import pandas as pd
import numpy as np
from icecream import ic
import matplotlib.pyplot as plt
import seaborn as sns


def correlation(x: pd.Series, y: pd.Series):
    return x.corr(y)


if __name__ == '__main__':
    data = pd.read_csv("advertising.csv")  # 200 samples

    # Cau 5 -> B
    print("------------------- Cau 5 ---------------------")
    x = data["TV"]
    y = data["Radio"]
    corr_xy = correlation(x, y)
    ic(f"Correlation between TV and Sales: {np.round(corr_xy, 2)}")

    # Cau 6 -> D
    print("------------------- Cau 6 ---------------------")
    features = ["TV", "Radio", "Newspaper"]

    for feature_1 in features:
        for feature_2 in features:
            corr_val = correlation(data[feature_1], data[feature_2])
            ic(
                f"Correlation between {feature_1} and "
                f"{feature_2}: {np.round(corr_val, 2)}"
            )

    # Cau 7 -> C
    print("------------------- Cau 7 ---------------------")
    x = data["Radio"]
    y = data["Newspaper"]
    ic(np.corrcoef(x, y))

    # Cau 8 -> D
    print("------------------- Cau 8 ---------------------")
    ic(data.corr())

    # Cau 9 ->
    print("------------------- Cau 9 ---------------------")
    data_corr = data.corr()
    sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=0.5)
    plt.show()
