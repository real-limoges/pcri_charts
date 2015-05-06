# -*- coding utf-8 -*-

"""
By : Real Limoges
Last Updated : 5/6/15

This script creates the data and formatting for the pie charts for the
data description paper
"""

#Standard Libraries
import matplotlib.pyplot as plt
import pandas as pd
import os

#User Made Modules
import setup_chart as cht
import global_var_list

#Global Variables
OPEN_PATH = global_var_list.OPEN_PATH
SAVE_PATH = global_var_list.SAVE_PATH
fontsize = 28

#Turn off SettingWithCopyWarning
pd.options.mode.chained_assignment = None

def fund_NVCA(fig):
	#Creates a subplot for distribution of NVCA for funds; displayed as a pie chart

	df = pd.read_csv(os.path.join(OPEN_PATH, 'fund_view.csv'), header = 0)

	#Clean data - overwrites data
	df = df[['FUND_ID', 'NVCA']]
	df = df.dropna()

	#Variable for aggregation purposes
	df['ONES'] = 1

	df = df.groupby(['NVCA'])
	df = df.agg({'ONES' : {'name' : 'sum'}})
	df = remove_outliers(df, 'ONES')

	ax = cht.build_pie_subplot(df, fig, 122)
	ax.set_title("Fund Breakdown by Industry (%)\n", fontsize = fontsize)

def fund_region(fig):
	#Creates a subplot for distribution of region for funds; displayed as a pie chart

	df = pd.read_csv(os.path.join(OPEN_PATH, 'fund_view.csv'), header = 0)

	#Clean data - overwrites data
	df = df[["FUND_ID", "REGION_ID"]]
	df = df.dropna()
	df["REGION_ID"].replace(global_var_list.region_replace, inplace = True)
	
	#Variable for aggregation purposes
	df['ONES'] = 1

	df = df.groupby(['REGION_ID'])
	df = df.agg({'ONES': {'name' : 'sum'}})
	df = remove_outliers(df, 'ONES')

	ax = cht.build_pie_subplot(df, fig, 111)
	ax.set_title("Fund Breakdown by Region (%)\n", fontsize = fontsize)


def remove_outliers(df, col):
	#Removes outliers (less than 2% of data) and adds 1-sum back to "Other"

	df[col] = df[col] / float(sum(df[col]))
	df = df[df[col] >= 0.02]

	remainder = 1 - sum(df[col])
	df.loc["Other", col] += remainder

	return df

def build_charts():
	fig = plt.figure(figsize = (20,9), facecolor = 'white')
	fund_NVCA(fig)
	fund_region(fig)
	plt.savefig(os.path.join(SAVE_PATH, 'fund_pie_charts.png'), bbox_inches = 'tight')