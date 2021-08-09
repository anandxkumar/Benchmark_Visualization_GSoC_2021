from radis import plot_diff, SpectrumFactory
import numpy as np


# Computation parameters
wmin = 2000
wmax = 4000
wstep = 0.01
T = 3000.0 #K
p = 0.1 #bar
broadening_max_width=10

wmax_array = np.arange(4000, 36000, 2000)


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
    
    sf.warnings.update(
        {
            "MissingSelfBroadeningWarning": "ignore",
            "NegativeEnergiesWarning": "ignore",
            "LinestrengthCutoffWarning": "ignore",
            "HighTemperatureWarning": "ignore",
        }
    )

    
    sf.load_databank('HITEMP-CO')
    #print(sf.df0)
    
    Ntarget = 60000
    sf.df0 = sf.df0[0:Ntarget]
    N = len(sf.df0)
    #print(N)
    #print(sf.df0)
    
    sf.params['optimization'] = None
    sf.params['broadening_method'] = 'voigt'
    
    my_folder = r"/home/pipebomb/Desktop/Spectrum_Legacy_wstep_n_lines/"
    sf.init_database(my_folder, autoretrieve=False)
    
    cond = sf.get_conditions()
    name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(N)
    
    s_none = sf.eq_spectrum(T, name = name)
