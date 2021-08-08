
from radis import plot_diff, SpectrumFactory
import numpy as np
import pandas as pd

'''
# For downloading CH4
from radis.io.hitemp import fetch_hitemp
fetch_hitemp('CH4')
'''

# Computation parameters
wmin = 2000
wmax = 4000
wstep = 0.01
T = 300.0 #K
p = 1 #bar
broadening_max_width=300



sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax, 
                  pressure=p,
                  wstep=wstep,
                  broadening_max_width=broadening_max_width, 
                  molecule="CH4",
                  cutoff=0, # 1e-27,
                  verbose=0,
                  )
                  
N_lines = [1,10, 100, 1000, 10000, 1e5, 1e6, 2e6, 3e6, 4e6, 4398730]

    
my_folder = r"/home/pipebomb/Desktop/_Benchmark_LDM (Voigt Updated)/CH4 Nlines (wL and wG) vs Calculation Time/"
sf.init_database(my_folder, autoretrieve=False)
    
for i in N_lines:
    
    sf.params['optimization'] = 'simple'
    sf.params['broadening_method'] = 'fft'
    
    sf.load_databank('HITEMP-CH4')
    #print(sf.df0)
    
    Ntarget = int(i)
    sf.df0 = sf.df0[0:Ntarget]
    N = len(sf.df0)
    print(N)
    
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)+"_"+sf.params['broadening_method']
    
    s_ldm = sf.eq_spectrum(T, name = name)
    
    #%% Voigt
    sf.params['broadening_method'] = 'voigt'
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)+"_"+sf.params['broadening_method']
    
    s_ldm = sf.eq_spectrum(T, name = name)


# Adding 1+wL*wG column in csv file
import pandas as pd
df =  pd.read_csv(my_folder+"CH4 Nlines (wL and wG) vs Calculation Time.csv")
df["1+wL*wG"] = 1 + df['wL'] * df['wG']

df.to_csv(my_folder+"CH4 Nlines (wL and wG) vs Calculation Time.csv", index = False)


