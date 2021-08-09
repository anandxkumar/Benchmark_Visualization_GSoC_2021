from radis import SpectrumFactory
import numpy as np

#%% CO Benchmark

# Computation parameters
wmin = 8000
wmax = 10000
T = 3000.0 #K
p = 0.1 #bar
broadening_max_width=10

#%%Declaring range of wstep array
wstep_array = np.arange(0.1, 0.003, -0.001)


sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax, 
                  pressure=p,
                  broadening_max_width=broadening_max_width, 
                  molecule="CO",
                  cutoff=0, # 1e-27,
                  verbose=2,

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

#%% Optimization
sf.params['optimization'] = None
sf.params['broadening_method'] = 'voigt'

my_folder = r"/home/pipebomb/Desktop/Spectrum_Legacy_wstep/"
sf.init_database(my_folder)

cond = sf.get_conditions()
name = cond['molecule'] + "_"+str(wmin)+"_"+str(wmax)

for i in wstep_array:
    print("wstep: ", i)

    sf.wstep = i
    sf.params.wstep = i
    try:
        s_none = sf.eq_spectrum(T, name = name)
    except:
        pass
        
#%% NO benchmark

# Computation parameters
wmin = 200
wmax = 2000
T = 300.0 #K
p = 1 #bar
broadening_max_width=10

#%%Declaring range of wstep array
wstep_array = np.arange(0.1, 0.01, -0.001)


sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax , 
                  pressure=p,
                  broadening_max_width=broadening_max_width, 
                  molecule="NO",
                  cutoff=0, # 1e-27,
                  verbose=3,

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

#%% Optimization
sf.params['optimization'] = None
sf.params['broadening_method'] = 'voigt'

sf.init_database(my_folder)

for i in wstep_array:
    print("wstep: ", i)

    sf.wstep = i
    sf.params.wstep = i
    try:
        s_none = sf.eq_spectrum(T, name = name)
    except:
        pass



