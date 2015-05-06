# -*- coding utf-8 -*-

'''
By: Real Limoges
Last Updated: 5/6/15

This file creates the data and formatting used to create the charts for the
data description paper.

'''

#Standard Libraries
import matplotlib.pyplot as pyplot
import pandas as pd
import os

#User Made Modules
import setup_chart as cht
import global_var_list


#Global Variables
OPEN_PATH = global_var_list.OPEN_PATH
SAVE_PATH = global_var_list.SAVE_PATH
fontsize = 28

def fund_vintage():
	#Creates a stacked bar chart of Fund_Type by vintage year

	df = pd.read_csv(os.path.join(OPEN_PATH, 'fund_view.csv'), header = 0)

	#Cleans up fund vintage data - overwrites original
	df = df[['VINTAGE_YEAR', 'FUND_TYPE']].dropna()
	df = df[ df.VINTAGE_YEAR >= 1980 ]
	df = df[ df.VINTAGE_YEAR <= 2015 ]

	#Removes Growth Equity, Other, and Secondary
	for s in ['GROWTH EQUITY', 'OTHER', 'SECOND']:
		df = df[ df.FUND_TYPE != s]

	#Set Data up for chart
	df = pd.crosstab(df.VINTAGE_YEAR, [df.FUND_TYPE],
					 rownames = ['VINTAGE_YEAR'], colnames = ['FUND_TYPE'])
	fig, ax = cht.setup_stacked_chart(df)

	#Formatting for chart
	ax.set_title("Number of Funds by Vintage Year\n", fontsize = fontsize)
	plt.xlim([1980,2013])

	plt.savefig(os.path.join(SAVE_PATH, 'fund_vintage.png'), bbox_inches = 'tight')


def build_charts():
	fund_vintage()