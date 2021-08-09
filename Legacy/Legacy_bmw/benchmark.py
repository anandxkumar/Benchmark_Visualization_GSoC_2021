from radis import SpectrumFactory
import astropy.units as u
import numpy as np

# Computation parameters
wmin = 2.3 
wmax = 8.0
T = 300.0 #K
p = 1 #bar
broadening_max_width= 1

#%%Declaring range of bmw array
bmw_array = np.arange(1, 10, 1)


sf = SpectrumFactory(wavelength_min=wmin * u.um, wavelength_max=wmax * u.um, 
                  pressure=p,
                  broadening_max_width=broadening_max_width, 
                  molecule="CO",
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


#%% Init Database

my_folder = r"/home/pipebomb/Desktop/Spectrum_Legacy_wstep_bmw/"
sf.init_database(my_folder)
cond = sf.get_conditions()
name = cond['molecule'] + "_"+str(round(cond['wavenum_min']))+"_"+str(round(cond['wavenum_max']))+"_"+str(cond['total_lines'])



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
        s_none = sf.eq_spectrum(T, name=name)
        #s_none.plot("radiance_noslit", wunit="nm")
    except:
        pass

