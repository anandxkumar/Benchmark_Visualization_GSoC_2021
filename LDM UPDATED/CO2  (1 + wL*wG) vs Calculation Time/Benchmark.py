# -*- coding: utf-8 -*-

from radis import plot_diff, SpectrumFactory
import numpy as np
import math



N_lines = [1e1,1e2,1e3, 1e4,1e5, 5e5, 7.5e5, 1e6, 2e6, 3e6, 4e6, 5e6, 6e6,
           7e6, 8e6]

prefix = '/home/pipebomb/Downloads/CO2 Database/'
database=[prefix+'02_500-625_HITEMP2010.par',
          prefix+'02_625-750_HITEMP2010.par',
          prefix+'02_750-1000_HITEMP2010.par',
          prefix+'02_1000-1500_HITEMP2010.par',
          prefix+'02_1500-2000_HITEMP2010.par',
          prefix+'02_2000-2125_HITEMP2010.par',
          prefix+'02_2125-2250_HITEMP2010.par',
          prefix+'02_2250-2500_HITEMP2010.par',
          prefix+'02_2500-3000_HITEMP2010.par',
          prefix+'02_2500-3000_HITEMP2010.par',
          prefix+'02_3000-3250_HITEMP2010.par',
          prefix+'02_3250-3500_HITEMP2010.par',
          prefix+'02_3500-3750_HITEMP2010.par',
          prefix+'02_3750-4000_HITEMP2010.par',]

# Condition Parameters
wmin = 500
wmax = 4000
dv = 0.01
T = 300.0 #K
p = 1 #bar
broadening_max_width=300    # lineshape broadening width, ext​

#%% Calculate Reference 
sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax, 
                  pressure=p,
                  isotope='1,2,3',
                  wstep=dv,
                  broadening_max_width=broadening_max_width, 
                  cutoff=0, # 1e-27,
                  verbose=0,
                  )

my_folder = r"/home/pipebomb/Desktop/_Benchmark_LDM (Voigt Updated)/CO2 Nlines (wL and wG) vs Calculation Time/"
sf.init_database(my_folder, autoretrieve=False)

for i in N_lines:

    sf.load_databank(path=database,
                     format='hitran',
                     parfuncfmt='hapi',
                     include_neighbouring_lines=False)

    Ntarget = int(i)
    sf.df0 = sf.df0[0:Ntarget]
    N = len(sf.df0)
    print(N)
    #print(sf.df0)

    sf.params['optimization'] = 'simple'
    sf.params['broadening_method'] = 'fft'
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)+"_"+sf.params['broadening_method']
    
    s_ldm = sf.eq_spectrum(T, name = name)
    
    #%% Voigt 
    sf.params['optimization'] = 'simple'
    sf.params['broadening_method'] = 'voigt'
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)+"_"+sf.params['broadening_method']
    
    s_ldm = sf.eq_spectrum(T, name = name)
    
# Adding 1+wL*wG column in csv file
import pandas as pd
df =  pd.read_csv(my_folder+"CO2 Nlines (wL and wG) vs Calculation Time.csv")
df["1+wL*wG"] = 1 + df['wL'] * df['wG']

df.to_csv(my_folder+"CO2 Nlines (wL and wG) vs Calculation Time.csv", index = False)

