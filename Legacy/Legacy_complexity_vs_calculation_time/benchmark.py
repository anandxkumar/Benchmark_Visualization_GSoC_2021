# -*- coding: utf-8 -*-

import pandas as pd
from statsmodels.api import OLS
from sklearn.linear_model import LinearRegression
#import ast

import os
directory = os.getcwd()
  
# creating a data frame

df = pd.read_csv(directory +"/Legacy_final.csv")


wstep =  df['wstep']
b_m_w = df['broadening_max_width']
N_lines = df['lines_calculated']


complexity = N_lines * b_m_w / wstep

df['complexity'] =  complexity

# Getting x and y
x_voigt = df[['complexity']]  # for mulitple columns -> df_voigt[['complexity','lines_calculated']]
y_voigt = df['calculation_time']

# Using OLS to find coerrelation and coefficient of linear regression
model = OLS(y_voigt, x_voigt)
result = model.fit()
print(result.summary())

# or using LinearRegression()

regressor = LinearRegression()
regressor.fit(x_voigt, y_voigt)

# display coefficients
print(regressor.coef_)

# Getting coefficient of multiple linear regression
coeff = regressor.coef_

# Updating Final complexity
complexity_final_voigt = coeff[0]*df['complexity']  # + coeff[1]*df_voigt['lines_calculated'] (if more columns)
df['complexity_final_voigt'] = complexity_final_voigt

# Scatter Plot
df.plot.scatter('complexity_final_voigt', 'calculation_time')


df.to_csv("Legacy_complexity_vs_calculation_time.csv", index=False)



