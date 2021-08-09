from radis import plot_diff, SpectrumFactory
import numpy as np


# Computation paramete
wmin = 2000
wmax = 3900
wstep = 0.005
T = 3000.0 #K
p = 1 #bar
broadening_max_width=10

N_lines = np.arange(2000, 92000, 2000)

#%% Calculate CO Spectrum
sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax, 
              pressure=p,
              wstep=wstep,
              broadening_max_width=broadening_max_width, 
              molecule="CO",
              cutoff=0, # 1e-27,
              verbose=0,
              )
              
my_folder = r"/home/pipebomb/Desktop/Spectrum_Legacy_n_lines_vs_calc_time/"
sf.init_database(my_folder, autoretrieve=False)
          
for i in N_lines:

    sf.load_databank('HITEMP-CO')
    print(sf.df0)
    
    Ntarget = i
    sf.df0 = sf.df0[0:Ntarget]
    N = len(sf.df0)
    print(N)
    #print(sf.df0)
    
    sf.params['optimization'] = None
    sf.params['broadening_method'] = 'voigt'
    
    my_folder = r"/home/pipebomb/Desktop/Spectrum_Legacy_n_lines_vs_calc_time/"
    sf.init_database(my_folder, autoretrieve=False)
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)
    
    s_none = sf.eq_spectrum(T, name = name)
