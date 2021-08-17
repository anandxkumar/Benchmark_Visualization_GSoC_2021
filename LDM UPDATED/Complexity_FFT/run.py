# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:39:26 2021

@author: erwan
"""

from os.path import dirname, join
from xexplorer import parse_files, plot

def test_plot_experiment_results_sample():
    """Sample code to explore experiment data"""

    # %% DATA
    # files (and special reading commands)
    files = {join(dirname(__file__),"_fft.csv"):{},
              }
    df = parse_files(files)
    df.drop(columns=["profiler", "dbpath", "last_modified"], inplace=True)

    print(files)
    #%% PLOT

    plot(df, xval='complexity_final_fft', yval='calculation_time', title="4.675e-08*(1 + wL*wG)*Spectral_Points*log(Spectral_Points) vs Calculation Time",
         size='broadening_max_width')


    return


if __name__ == '__main__':
    test_plot_experiment_results_sample()
