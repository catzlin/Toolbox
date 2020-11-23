# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for Toolbox Project
"""

from os.path import split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', 200)


def plot_numerical_features(numerical_features):
    """ plot all the numerical features
    """

    for numerical_feature in numerical_features:

        fig, ax =plt.subplots(1,3,figsize=(20,8))
        ax[0].set_title(f"Distribution of: {numerical_feature}")
        sns.histplot(data = numerical_data[numerical_feature], kde=True, ax=ax[0])
        ax[1].set_title(f"Boxplot of: {numerical_feature}")
        sns.boxplot(numerical_data[numerical_feature], ax=ax[1])
        ax[2].set_title(f"Gaussianity of: {numerical_feature}")
        qqplot(numerical_data[numerical_feature],line='s',ax=ax[2])
        fig.show()


#if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
 #   import Toolbox
