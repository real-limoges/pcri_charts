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

def gp_year_founded():
	#Creates a stacked bar chart of gp_type by year_founded

	df = pd.read_csv(os.path.join(OPEN_PATH, 'gp_view.csv'), header = 0)

	#Clean up gp founded data - overwrites original
	df = [['YEAR_FOUNDED', 'GP_TYPE']]
	df = df.dropna()
	df = df[df.YEAR_FOUNDED >= 1980]
	df = df[df.YEAR_FOUNDED <= 2012]

	df = pd.crosstab(df.YEAR_FOUNDED, [df.GP_TYPE],
					 rownames = ['YEAR_FOUNDED'], colnames = ['GP_TYPE'])

	#Drops Other from gp_type
	df = df.drop('OTHER', axis = 1)

	fig, ax = cht.setup_stacked_chart(df)

	#Formatting for chart
	ax.set_title('Number of Private Capital Firms by Year Founded\n', 
				 fontsize = fontsize)
	plt.xlim([1980,2013])

	plt.savefig(os.path.join(SAVE_PATH, 'gp_type.png'), bbox_inches = 'tight')

def cashflow_type_by_year():
	#Creates a stacked bar chart of fund type by vintage year based on cashflow data

	df = pd.read_csv(os.path.join(OPEN_PATH, 'fund_quarterly_cashflow_view.csv'), 
					 header = 0)
	fund_df = pd.read_csv(os.path.join(OPEN_PATH, 'fund_view.csv'), header = 0)

	#Cleans Fund Data to be merged into 
	fund_df = fund_df[['FUND_ID', 'FUND_TYPE', 'VINTAGE_YEAR']]
	fund_df = fund_df[ fund_df.VINTAGE_YEAR >= 1980 ]
	fund_df = fund_df.dropna()

	df = df.dropna()

	#Holder variable for aggregation purposes
	df['ONES'] = 1

	#Groups data to remove; collapsing panel data to cross sectional
	df = df.groupby(['FUND_ID'], as_index = False)
	df = df.agg( {'ONES' : { 'name' : 'mean' } })

	df = pd.merge(left = df, right = fund_df, how = 'inner',
				  left_on = 'FUND_ID', right_on = 'FUND_ID')

	df = pd.crosstab(df.VINTAGE_YEAR, df.FUND_TYPE, 
					 rownames = ['VINTAGE_YEAR'], colnames = ['FUND_TYPE'])

	#Removes Growth Equity, Other, and Second from the dataset
	for col in ['GROWTH EQUITY', 'OTHER', 'SECOND']:
		df = df.drop(col, axis = 1)

	fig, ax = cht.setup_stacked_chart(df)

	#Custom Font Size for this chart
	font = 26

	#Formatting for chart
	ax.set_title("Number of Funds wiht Cashflows\n by Vintage Year\n", fontsize = font)
	plt.xlim([1990, 2013])

	plt.savefig(os.path.join(SAVE_PATH, 'cashflow_type_by_year.png'), 
				bbox_inches = 'tight')

def build_charts():
	fund_vintage()
	yearly_investment_types()
	gp_year_founded()
	cashflow_type_by_year()