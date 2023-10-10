# data-analysis

## Preprocessing

Steps:

1. Drop all **rows** without a primary price adjustment
   - all rows with NA in primary price
2. Drop all **columns** with >80% of NAs
3. Convert all category columns ("sector", "area") into one-hot columns
4. Use median and zero imputation for **columns** whose stddev after fill has a difference from original stddev of <10%

   - See "fill_median_or_zero_by_thresh" in EDA/2023-10-05/total_eda.ipynb

5. Use Linear Regression or datawig to fill all remaining columns and clip with actual min and max of distribution
   - See [this towardsdatascience article](https://towardsdatascience.com/7-ways-to-handle-missing-values-in-machine-learning-1a6326adf79e#544c) for more details
