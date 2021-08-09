import pandas as pd
import numpy as np
from statsmodels.api import OLS
from sklearn.linear_model import LinearRegression
import os

# Reading data from the combined data of voigt and voigt
directory = os.getcwd()
df = pd.read_csv(directory + "Combined_Final.csv")

# Getting all voigt broadening readings
df_voigt = df.loc[df['broadening_method'] == 'voigt']

# Computing Complexity of LDM>voigt 
df_voigt['Complexity_voigt'] = (df['wL']*df['wG'] + 1) * df['Spectral Points']*np.log( df['Spectral Points'])

# Getting x and y
x_voigt = df_voigt[['Complexity_voigt', 'lines_calculated']]  # for mulitple columns -> df_voigt[['Complexity_voigt','lines_calculated']]
y_voigt = df_voigt['calculation_time']

# Using OLS to find coerrelation and coefficient of multiple linear regression
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
complexity_final_voigt = coeff[0]*df_voigt['Complexity_voigt'] + (coeff[1]*df_voigt['lines_calculated']) # + coeff[1]*df_voigt['lines_calculated'] (if more columns)
df_voigt['complexity_final_voigt'] = complexity_final_voigt

# Scatter Plot
df_voigt.plot.scatter('complexity_final_voigt', 'calculation_time')

# Saving Updated csv file
df_voigt.to_csv(directory + "_voigt.csv", index=False)
