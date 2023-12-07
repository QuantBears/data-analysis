# Predicting Changes in Stock Price with Machine Learning

Predicting stock prices has been a popular topic among computer scientists and data scientists because the prospect of having a continuous passive income stream is simply too tempting to pass up. The motivation behind this project is similar, however seeing as many have tried and failed, a secondary, more realistic goal is to uncover the most predictive features of a stock’s short-term success in hopes that future works can build upon these results to create more predictive models.

## Prerequisites

This project is built using jupyter notebook and Python version 3.9.18 with Anaconda.

Please first install the conda environment by navigating to the project root directory and then running the following code to create the conda environment used for this project:

`conda env create -n QuantBearsDataAnalysis -f conda_env.yml`

`conda activate QuantBearsDataAnalysis`

## Package Details

Below are the most important packages and versions:

- pandas=2.1.0
- numpy=1.25.2
- scikit-learn=1.3.0
- xgboost=2.0.2
- matplotlib=3.8.0
- shap=0.42.1

## Dataset

Due to the size of the dataset, I stored all data in [this Google Drive](https://drive.google.com/drive/folders/1iPDuWqonQ5_Zi0SiZsNlt1j_6vCxjqWq?usp=drive_link), which contains the CSV files.

In order to reproduce results, please download all data in this drive and place them in a "data/" directory in the root directory of this project.

## Repository Structure

`report/` - contains project report PDF.

`figures/` - contains figures generated for EDA and results used in project report.

`results/` - contains hyperparameter search results and scores.

`src/` - contains all jupyter notebooks used to create this project.

## Author

[Nuo Wen Lei](https://nuowenlei.github.io/personal-portfolio/) (nuo_wen_lei@brown.edu)

## License

MIT License
