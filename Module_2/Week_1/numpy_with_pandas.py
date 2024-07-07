import pandas as pd
import numpy as np
from icecream import ic


df = pd.read_csv("Module_2\\Week_1\\advertising.csv")
data = df.to_numpy()  # (200, 4) -> TV, Radio, Newspaper, Sales

tv = data[:, 0]
radio = data[:, 1]
newspaper = data[:, 2]
sales = data[:, 3]

# Cau 15 -> C
print("------------------- Cau 15 ---------------------")
sales_max_index = np.argmax(sales)

ic(sales_max_index)
ic(sales[sales_max_index])

# Cau 16 -> B
print("------------------- Cau 16 ---------------------")
tv_avg = np.mean(tv)

ic(tv_avg)

# Cau 17 -> A
print("------------------- Cau 17 ---------------------")
sales_ge_20_index = np.nonzero(sales >= 20.0)  # This returns a tuple

ic(len(sales_ge_20_index[0]))

# Cau 18 -> B
print("------------------- Cau 18 ---------------------")
sales_ge_15_index = np.nonzero(sales >= 15)
radio_ge_15_avg = np.mean(radio[sales_ge_15_index])

ic(radio_ge_15_avg)

# Cau 19 -> C
print("------------------- Cau 19 ---------------------")
newspaper_avg = np.mean(newspaper)
data_where_newspaper_gt_avg = data[newspaper > newspaper_avg]
sales_where_newspaper_gt_avg_sum = np.sum(data_where_newspaper_gt_avg[:, 3])

ic(sales_where_newspaper_gt_avg_sum)

# Cau 20 -> C
print("------------------- Cau 20 ---------------------")
sales_avg = np.mean(sales)
scores = np.full(sales.shape, fill_value="Good", dtype="U10")
scores[sales == sales_avg] = "Average"
scores[sales < sales_avg] = "Bad"

ic(scores[7:10])
ic(sales_avg)
ic(sales[7:10])

# Cau 21 -> C
print("------------------- Cau 21 ---------------------")
sales_diff = np.abs(sales - sales_avg)
sales_nearest_avg = sales[np.argmin(sales_diff)]
scores[sales > sales_nearest_avg] = "Good"
scores[sales == sales_nearest_avg] = "Average"
scores[sales < sales_nearest_avg] = "Bad"

ic(scores[7:10])
ic(sales_nearest_avg)
ic(sales[7:10])
