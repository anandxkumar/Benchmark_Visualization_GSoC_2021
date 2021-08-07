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
    files = {join(dirname(__file__),"Spectral Range (Lines constant) vs Calculation Time.csv"):{},
              }
    df = parse_files(files)

    print(files)
    #%% PLOT

    plot(df, xval='Spectral Points', yval='calculation_time', title="Spectral points(NLines and Wstep constant) vs Calculation Time",
        color_mapper='broadening_method', size='broadening_max_width', color_mapper_scale=False)


    return


if __name__ == '__main__':
    test_plot_experiment_results_sample()
