# -*- coding: utf-8 -*-

import pandas as pd
#import ast
import os
cwd = os.getcwd()
  
# creating a data frame

df = pd.read_csv(cwd + "Legacy_final.csv")


wstep =  df['wstep']
b_m_w = df['broadening_max_width']
N_lines = df['lines_calculated']


complexity = N_lines * b_m_w / wstep

df['complexity'] =  complexity


df.to_csv("Legacy_complexity_vs_calculation_time.csv", index=False)



