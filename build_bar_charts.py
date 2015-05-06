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

def yearly_investment_types():
	#Creates a stacked bar chart of yearly investment types by year

	df = pd.read_csv(os.path.join(OPEN_PATH, 'investment_view.csv'), header = 0)

	#Clean up investment type data - overwrites original
	df = df[['DATE', 'INVESTMENT_CATEGORY']]

	df['DATE'] = df['DATE'].apply(str)
	df['DATE'] = df['DATE'].apply(lambda x : int( x[:4] ))
	df = df[ df.DATE >= 1980 ]
	df = df[ df.DATE <= 2015 ]

	#Removes Other and Second category
	for s in ['OTHER', 'SECOND']:
		df = df[ df.INVESTMENT_CATEGORY != s ]

	#Makes investment categories more readable
	df['INVESTMENT_CATEGORY'].replace(global_var_list.fund_type_replace, inplace = True)

	df = pd.crosstab(df.DATE, [df.INVESTMENT_CATEGORY],
					 rownames = ['DATE'], colnames = ['INVESTMENT_CATEGORY'])
	fig, ax = cht.setup_stacked_chart(df)

	#Formatting for chart
	ax.set_title("Number of Investments per Year\n", fontsize = fontsize)
	plt.xlim([1990, 2013])

	plt.savefig(os.path.join(SAVE_PATH, 'yearly_investment_types.png'), 
				bbox_inches = 'tight')

def build_charts():
	fund_vintage()
	yearly_investment_types()