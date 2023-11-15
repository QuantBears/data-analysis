import pandas as pd, warnings
warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)

short_term_columns = ['analysts_down', 'analysts_down_percent', 'analysts_up_percent',
       'authors_count', 'capm_alpha_60m', 'coefficient_of_variation_90d',
       'debt_eq', 'div_growth_category', 'div_safety_category',
       'dividends_estimate_fy1_analyst_down',
       'dividends_estimate_fy1_analyst_up',
       'dividends_estimate_fy2_analyst_down',
       'dividends_estimate_fy2_analyst_up',
       'dps_consensus_mean_percent_revisions_down_1_annual_period_fwd',
       'eps_ltg', 'last_price_vs_sma_100d', 'last_price_vs_sma_10d',
       'last_price_vs_sma_200d', 'last_price_vs_sma_50d', 'momentum_12m',
       'momentum_3m', 'momentum_6m', 'momentum_9m', 'pb_ratio',
       'price_return_1y', 'price_return_3m', 'price_return_6m',
       'price_return_9m', 'return_on_net_tangible_assets',
       'return_on_total_capital', 'Future_3-5Y_EPS_without_NRI_Growth_Rate',
       'moment_rank', '5-Day_RSI', '9-Day_RSI', '14-Day_RSI',
       '6-1_Month_Momentum_%', '12-1_Month_Momentum_%', 'ratios_rank',
       'Forward_PE_Ratio', 'EV-to-Forward-EBITDA',
       'Earnings_Yield__Greenblatt__%', 'Volume']


def create_autoreg_features(df, short_term_features, num_days = 2):
	all_days = df.index.get_level_values(0).unique().sort_values()

	new_df = pd.DataFrame()
	for dayIndex in range(num_days, all_days.shape[0]):
		day = all_days[dayIndex]

		newDayDf = df.loc[day]
		newDayDf["date"] = day
		currTickers = newDayDf.index.values
		for prevIndex in range(num_days):
			prevDay = all_days[dayIndex - prevIndex]
			prevDayFeatures = df.loc[prevDay].reindex(currTickers)[short_term_features].add_suffix(f"_prev_{prevIndex + 1}")
			newDayDf = pd.concat([newDayDf, prevDayFeatures], axis = 1)
		
		new_df = pd.concat([new_df, newDayDf.set_index("date", append = True)], axis = 0)

	autoreg_removed_rows = df.loc[all_days[:num_days]].shape[0]

	assert df.shape[0] - new_df.shape[0] == autoreg_removed_rows, "Autoregression removed different amount of rows than expected"
	
	return new_df