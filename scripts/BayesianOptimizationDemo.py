import GPy
import GPyOpt
from fbprophet import Prophet

def compute_mape(aux_df):
    return -np.mean(1- (np.abs(aux_df.yhat-aux_df.y)/aux_df.yhat))


def fit_prophet_val(x):
    fs = np.zeros((x.shape[0],1))
    for i in range(x.shape[0]):
        m = Prophet(weekly_seasonality=boolean_dict[x[i,3]],holidays=holidays,changepoint_prior_scale=x[i,0],interval_width=x[i,1],holidays_prior_scale=x[i,2],\
                   daily_seasonality = boolean_dict[x[i,4]],seasonality_prior_scale=x[i,5],yearly_seasonality=boolean_dict[x[i,6]],n_changepoints=x[i,7])
        m.fit(train_df)
        future = m.make_future_dataframe(periods=(test_end_date-train_end_date).days)
        forecast = m.predict(future)
        forecast = forecast[['ds','yhat']]
        aux_df = test_df.merge(forecast,on=['ds'],how='inner')
        #fs[i] = np.log(compute_mape(aux_df))
        fs[i] = compute_mape(aux_df)
        #print aux_df.head()
        #print compute_mape(aux_df)
        #fs[i] = np.sqrt(mean_squared_error(aux_df['y'],aux_df['yhat']))
        #print fs[i] + 1
    return fs

domain       =[{'name': 'changepoint_prior_scale',    'type': 'continuous',      'domain': (0.001,0.5)},
               {'name': 'interval_width',             'type': 'continuous',      'domain': (0.001,1.0)},
               {'name': 'holidays_prior_scale',       'type': 'continuous',      'domain': (8.0,11.0)},
               {'name': 'weekly_seasonality',         'type': 'categorical',     'domain': (1,0)},
               {'name': 'daily_seasonality',          'type': 'categorical',     'domain': (1,0)},
               {'name': 'seasonality_prior_scale',    'type': 'continuous',      'domain': (8.0,12.0)},
               {'name': 'yearly_seasonality',         'type': 'categorical',     'domain': (1,0)},
               {'name': 'n_changepoints',             'type': 'discrete',         'domain': (5,20)}]

opt = GPyOpt.methods.BayesianOptimization(f = fit_prophet_val,            # function to optimize
                                          domain = domain,         # box-constraints of the problem
                                          acquisition_type ='LCB',       # LCB acquisition
                                          acquisition_weight = 0.1 )    # Exploration exploitation

opt.run_optimization(max_iter=20)
opt.plot_convergence()

x_best = opt.X[np.argmin(opt.Y)] #x_best contains optimal hypter parameters found
y_best = opt.Y[np.argmin(opt.Y)]

