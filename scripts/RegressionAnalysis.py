# for regression analysis

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble.partial_dependence import plot_partial_dependence
import numpy as np
import datetime
import ast
import matplotlib.pyplot as plt

data_df = pd.read_csv(r'D:\Work\2018Q3\20181012-itocraffections\feature_sum_20181012125603.csv')
data_df.head(3)
data_df = data_df[(data_df.ito < 100) & (data_df.pv_cr > 0.5)]
data_df = data_df.fillna(0)

features = ['mean', 'std', 'cv', 'mapd_mean', 'mapd_std', 'vlt_mean', 'vlt_std', 'autopo_row_ratio',
            'autopo_units_ratio', 'autopo_money_ratio', 'fill_ratio', 'vltgap_mean', 'vltgap_std', 'order_cnt']
X = data_df[features]
Y1 = data_df['ito']
Y2 = data_df['pv_cr']

ito = GradientBoostingRegressor()
ito.fit(X, Y1)
zip(X.columns, ito.feature_importances_)
fea = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
fig, axs = plot_partial_dependence(ito, X, fea, features, n_cols=3, grid_resolution=50)
plt.subplots_adjust(bottom=0.05, top=0.95)  # overlap the title

cr = GradientBoostingRegressor()
cr.fit(X, Y2)
zip(X.columns, cr.feature_importances_)
fea = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
fig, axs = plot_partial_dependence(cr, X, fea, features, n_cols=3, grid_resolution=50)
plt.subplots_adjust(bottom=0.05, top=0.95)