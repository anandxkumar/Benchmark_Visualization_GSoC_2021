import pandas as pd
import numpy as np
from statsmodels.api import OLS
from sklearn.linear_model import LinearRegression
import os

# Reading data from the combined data of fft and FFT
directory = os.getcwd()
df = pd.read_csv(directory + "Combined_Final.csv")

# Getting all fft broadening readings
df_fft = df.loc[df['broadening_method'] == 'fft']

# Computing Complexity of LDM>fft 
df_fft['Complexity_fft'] = (df['wL']*df['wG'] + 1) * df['Spectral Points']*np.log( df['Spectral Points'])

# Getting x and y
x_fft = df_fft[['Complexity_fft']]  # for mulitple columns -> df_fft[['Complexity_fft','lines_calculated']]
y_fft = df_fft['calculation_time']

# Using OLS to find coerrelation and coefficient of multiple linear regression
model = OLS(y_fft, x_fft)
result = model.fit()
print(result.summary())

# or using LinearRegression()

regressor = LinearRegression()
regressor.fit(x_fft, y_fft)

# display coefficients
print(regressor.coef_)

# Getting coefficient of multiple linear regression
coeff = regressor.coef_

# Updating Final complexity
complexity_final_fft = coeff[0]*df_fft['Complexity_fft']  # + coeff[1]*df_fft['lines_calculated'] (if more columns)
df_fft['complexity_final_fft'] = complexity_final_fft

# Scatter Plot
df_fft.plot.scatter('complexity_final_fft', 'calculation_time')

# Saving Updated csv file
df_fft.to_csv(directory + "_fft.csv", index=False)
