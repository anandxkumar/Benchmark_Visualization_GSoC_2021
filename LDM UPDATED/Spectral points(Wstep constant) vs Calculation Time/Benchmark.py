
from radis import plot_diff, SpectrumFactory
import numpy as np
import math


# Computation parameters
wmin = 2000
wmax = 10000
wstep = 0.01
T = 300 #K
p = 1 #bar
broadening_max_width=300

wmax_array = np.arange(4000, 18000, 2000)

for i in wmax_array:
    print(i)
    wmax = i
    
    #%% Calculate CO, 60000 lines
    sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax, 
                      pressure=p,
                      wstep=wstep,
                      broadening_max_width=broadening_max_width, 
                      molecule="CO",
                      cutoff=0, # 1e-27,
                      verbose=0,
                      )
    
    

    sf.load_databank('HITEMP-CO')
    #print(sf.df0)
    
    N = len(sf.df0)

    
    sf.params['optimization'] = 'simple'
    sf.params['broadening_method'] = 'fft'
    
    my_folder = r"/home/pipebomb/Desktop/_Benchmark_LDM (Voigt Updated)/Spectral Range (Lines constant) vs Calculation Time/"
    sf.init_database(my_folder, autoretrieve=False)
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)+"_"+sf.params['broadening_method']
    
    s_ldm = sf.eq_spectrum(T, name = name)
    
    #%% voigt
    sf.params['optimization'] = 'simple'
    sf.params['broadening_method'] = 'voigt'
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)+"_"+sf.params['broadening_method']
    
    s_ldm = sf.eq_spectrum(T, name = name)
