
from radis import SpectrumFactory
import numpy as np
from radis import SpectrumFactory, config, plot_diff


# Computation parameters
wmin = 5000
wmax = 5200
T = 300.0 #K
p = 1 #bar
truncation=300

#%%Declaring range of wstep array
wstep_array = []
for i in [1e-1,1e-2,1e-3]:
    for j in range(0,10):
        wstep_array.append(i-i*j/10)


sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax , 
                  pressure=p,
                  truncation=truncation, 
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

my_folder = r"/home/pipebomb/Desktop/Test_data/"
db = sf.init_database(my_folder)
cond = sf.get_conditions()
name = "fft_mode"


#%% Optimization fft
sf.params['optimization'] = 'simple'
sf.params['broadening_method'] = 'fft'

#%% Running Benchmark
for i in wstep_array:
    print("wstep: ", i)

    sf.wstep = i
    sf.params.wstep = i
    try:
        s_ldm = sf.eq_spectrum(T, name = name)
    except:
        pass

#%% Optimization voigt
config["SPARSE_WAVERANGE"] = False
sf.params['optimization'] = 'simple'
sf.params['broadening_method'] = 'voigt'

cond = sf.get_conditions()
name = "voigt_Sparse_False"


#%% Running Benchmark
for i in wstep_array:
    print("wstep: ", i)

    sf.wstep = i
    sf.params.wstep = i
    try:
        s_ldm = sf.eq_spectrum(T, name = name)
    except:
        pass

#%% Optimization voigt
config["SPARSE_WAVERANGE"] = True
sf.params['optimization'] = 'simple'
sf.params['broadening_method'] = 'voigt'

cond = sf.get_conditions()
name = "voigt_Sparse_True"


#%% Running Benchmark
for i in wstep_array:
    print("wstep: ", i)

    sf.wstep = i
    sf.params.wstep = i
    try:
        s_ldm = sf.eq_spectrum(T, name = name)
    except:
        pass

