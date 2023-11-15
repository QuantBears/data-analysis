import boto3
import awswrangler as wr
import pandas as pd
import numpy as np
from tqdm import tqdm

accessKeys = pd.read_csv("../quant-bears_accessKeys.csv")
session = boto3.Session(
	aws_access_key_id=accessKeys.loc[0, "Access key ID"],
	aws_secret_access_key=accessKeys.loc[0, "Secret access key"]
)

s3_collection_path = "s3://quant-bears-data-collection/raw-data/"
s3_price_collection_path = "s3://quant-bears-data-collection/raw-resolved-price/"

def load_data():
	data_sources = ["seekingAlpha.seekingAlphaBulkMetrics", "gurufocus"]
	sources_dict = dict((source, wr.s3.list_objects(s3_collection_path + source + "/", boto3_session=session)) for source in data_sources)
	df_dict = {}
	for source in data_sources:
		dfs = []
		print(source)
		for path in tqdm(sources_dict[source]):
			new_df = wr.s3.read_parquet(path, boto3_session=session)
			new_df["date"] = path.split("/")[-1].split(".")[0]
			dfs.append(new_df)

		df_dict[source] = pd.concat(dfs, axis = 0)
	joined_df = pd.concat([df.set_index(["date", "ticker"]) for df in df_dict.values()], axis = 1)
	return joined_df

def load_pred_price(df, days_ahead=5):
	all_dates = df.index.get_level_values(0).unique()
	adjusted_dates = all_dates[:-days_ahead]
	adjusted_df = df.loc[adjusted_dates]

	pred_dates = all_dates[days_ahead:]
	dfs = []
	for i, d in enumerate(tqdm(pred_dates)):
		path = s3_price_collection_path + d + ".parquet"
		new_df = wr.s3.read_parquet(path, boto3_session=session)

		s = df.loc[all_dates[i], "primary_price"]
		intersect_tickers = np.intersect1d(new_df["ticker"].values, s[~s.isna()].index.values)
		new_df = new_df[new_df["ticker"].isin(intersect_tickers)]
		new_df["date"] = all_dates[i]
		dfs.append(new_df)

	price_df = pd.concat(dfs, axis = 0).set_index(["date", "ticker"]).rename({"primary_price": "pred_price"}, axis = 1)
	return adjusted_df.reindex(price_df.index), price_df