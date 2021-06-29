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
    files = {join(dirname(__file__),"Spectrum_Legacy_wstep_bmw.csv"):{},
              }
    df = parse_files(files)

    print(files)
    #%% PLOT

    plot(df, xval='broadening_max_width', yval='calculation_time', title="Legacy Voigt BMW(CO)")


    return


if __name__ == '__main__':
    test_plot_experiment_results_sample()
