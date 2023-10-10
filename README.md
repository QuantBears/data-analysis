# data-analysis

## Data Splitting

Splits:

- Train set
- Validation set
- Test set

Since this is a time series dataset and the time offset is 1 week, there is the possibility of data leakage if splitting is random, which means that the model would have some information about the distribution of the data in the future when training.

To prevent this, we can split our dataset accordingly. Suppose I have data from t=0 to t=100 with target offset of t=7. This means that I am using t=0 to predict a value at t=7, and so on. Then I can split my data as such to prevent data leakage given train size = ~60%, val size = ~20%, test size = ~20%:

- Train set
  - X: t=0 to t=53
  - y: t=7 to t=60
- Validation set
  - X: t=54 to t=70
  - y: t=61 to t=77
- Test set:
  - X: t=78 to t=93
  - y: t=85 to t=100

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
