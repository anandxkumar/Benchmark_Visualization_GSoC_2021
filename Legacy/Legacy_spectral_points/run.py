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
    files = {join(dirname(__file__),"Spectral_points_legacy.csv"):{},
              }
    df = parse_files(files)

    print(files)
    #%% PLOT

    plot(df, xval='spectral_points', yval='calculation_time', title="Legacy_Spectral_Point",
        color_mapper='lines_calculated', size='broadening_max_width')


    return


if __name__ == '__main__':
    test_plot_experiment_results_sample()
