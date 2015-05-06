# -*- coding utf-8 -*-

"""
By: Real Limoges
Last Updated : 5/6/15

Sets up charts with common formatting

"""

#Standard Libraries
import matplotlib.pyplot as plt
import matplotlib

#User Made Modules
import global_var_list

#Global Variables
bar_colors = global_var_list.bar_colors

def setup_stacked_chart(df, width = 0.3):
	#Sets up a stacked bar chart

	fig = plt.figure(figsize = (12,9), facecolor = 'white', frameon = False)
	ax = fig.add_subplot(111)
	cols = df.columns.tolist()

	#Loops through the list of columns backwards so legend and bars are in the same order
	for item in range( len(cols)-1, -1, -1):
		if item == 0:
			plt.bar(df.index.values, df[cols[item]], width = width,
					color = bar_colors[item], linewidth = 0)
		else:
			plt.bar(df.index.values, df[cols[item]], width = width,
					color = bar_colors[item], bottom = df[cols[item-1]],
					linewidth = 0)

	#Cleans up the legend and frame
	leg = ax.legend(labels = cols[::-1], fontsize = 'medium')
	leg.get_frame().set_linewidth(0.0)
	for s in ['top','right', 'left', 'bottom']:
		ax.spines[s].set_visible(False)
	plt.tick_params(axis = 'y', which = 'both', right = 'off')
	plt.tick_params(axis = 'x', which = 'both', top = 'off', bottom = 'off')

	#Formats the y-axis to have commas for thousands
	ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

	return fig, ax