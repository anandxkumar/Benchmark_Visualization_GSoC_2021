
from radis import SpectrumFactory
import numpy as np


# Computation parameters
wmin = 2000 
wmax = 2500
T = 300.0 #K
p = 1 #bar
broadening_max_width= 2
wstep = 0.01

#%%Declaring range of broadening max width
bmw_array = np.arange(20, 1020, 20)


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

sf.fetch_databank('hitemp')


#%% Init Database

my_folder = r"/home/pipebomb/Desktop/_Benchmark_LDM (Voigt Updated)/Broadening Max Width vs Calculation Time/"
sf.init_database(my_folder)
cond = sf.get_conditions()
name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(cond['total_lines'])+"_"+sf.params['broadening_method']

#%% Optimization
sf.params['optimization'] = 'simple'
sf.params['broadening_method'] = 'fft' 

#%% Running Benchmark

for i in bmw_array:
    print("bmw: ", i)
    
    broadening_max_width= i
    sf._broadening_max_width = broadening_max_width
    sf.params.broadening_max_width = broadening_max_width
    wavenum_min = sf.input.wavenum_min
    wavenum_max = sf.input.wavenum_max
    sf.params.wavenum_min_calc = wavenum_min - broadening_max_width / 2
    sf.params.wavenum_max_calc = wavenum_max + broadening_max_width / 2
    
    try:
        s_ldm = sf.eq_spectrum(T, name=name)
    except:
        pass

#%% Optimization
sf.params['optimization'] = 'simple'
sf.params['broadening_method'] = 'voigt' 

cond = sf.get_conditions()
name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(cond['total_lines'])+"_"+sf.params['broadening_method']


#%% Running Benchmark

for i in bmw_array:
    print("bmw: ", i)
    
    broadening_max_width= i
    sf._broadening_max_width = broadening_max_width
    sf.params.broadening_max_width = broadening_max_width
    wavenum_min = sf.input.wavenum_min
    wavenum_max = sf.input.wavenum_max
    sf.params.wavenum_min_calc = wavenum_min - broadening_max_width / 2
    sf.params.wavenum_max_calc = wavenum_max + broadening_max_width / 2
    
    try:
        s_ldm = sf.eq_spectrum(T, name=name)
    except:
        pass