# -*- coding: utf-8 -*-

#%% Import dataset

import pandas

tips = pandas.read_csv('data/tips.csv')
tips.head(3)

#%% Show some stats

print(tips.describe())

#%% Show count of sex values

print(tips['sex'].value_counts())

#%% Clean some data

tips['sex'] = tips['sex'].str.title()
tips.loc[tips['sex'].str.contains("F"), 'sex'] = "Female"
tips.loc[tips['sex'].str.contains("M"), 'sex'] = "Male"

#%% Show count of smoker values

print(tips['smoker'].value_counts())

#%%

tips['smoker'] = tips['smoker'].str.replace('"', '')
tips['smoker'] = tips['smoker'].str.replace('”', '')

#%% Plot the data

import seaborn

plot = seaborn.scatterplot(x='total_bill', y='tip', data=tips)

#%% Scatter plot of Sex vs Tip %

tips['tip_percent'] = tips['tip'] / tips['total_bill']
tips['bill_per_person'] = tips['total_bill'] / tips['size']
plot = seaborn.scatterplot(x='total_bill', y='tip_percent', hue='sex', data=tips)

#%% Violin plot of Day vs Tip %

plot = seaborn.violinplot(x='day', y='tip_percent', data=tips)

#%% Find some stats

print(tips[['day', 'tip_percent']].groupby('day').describe())

print(tips[['smoker', 'tip_percent']].groupby('smoker').describe())

print(tips[['sex', 'tip_percent']].groupby('sex').describe())

print(tips[['time', 'tip_percent']].groupby('time').describe())

#%%





