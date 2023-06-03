from N_fctn_load_excel import load_excel_to_dataframe

df = load_excel_to_dataframe('M_main_dataset.xlsx')
#print(df)

#print(df.columns)



#subset the dataframe to non none values in the real index column:
from N_fctn_subset_non_none import subset_non_none_values

df = subset_non_none_values(df,column='real_net_monetary_index')
#print(df)

df = subset_non_none_values(df,column='finds_rate') 
#print(df)

from N_fctn_OLS import ols_analysis
model1 = ols_analysis(df, target_col='finds_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion'] )

#print(model1)
'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             finds_rate   R-squared:                       0.000
Model:                            OLS   Adj. R-squared:                 -0.001
Method:                 Least Squares   F-statistic:                    0.1454
Date:                Fri, 02 Jun 2023   Prob (F-statistic):              0.933
Time:                        14:01:27   Log-Likelihood:                 3791.8
No. Observations:                3651   AIC:                            -7576.
Df Residuals:                    3647   BIC:                            -7551.
Df Model:                           3
Covariance Type:            nonrobust
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.0856      0.118      0.726      0.468      -0.146       0.317
real_net_monetary_index    -0.0049      0.020     -0.244      0.807      -0.044       0.034
men_proportion             -0.1174      0.228     -0.515      0.607      -0.565       0.330
65+_proportion             -0.0431      0.101     -0.429      0.668      -0.240       0.154
==============================================================================
Omnibus:                     5168.521   Durbin-Watson:                   2.013
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1079542.865
Skew:                           8.501   Prob(JB):                         0.00
Kurtosis:                      85.507   Cond. No.                         273.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''



model2 = ols_analysis(df, target_col='finds_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion', 'detector_expensive_dummy'] )
#print(model2)

#better, significant:):
'''                            OLS Regression Results
==============================================================================
Dep. Variable:             finds_rate   R-squared:                       0.005
Model:                            OLS   Adj. R-squared:                  0.003
Method:                 Least Squares   F-statistic:                     4.139
Date:                Thu, 01 Jun 2023   Prob (F-statistic):            0.00239
Time:                        20:05:55   Log-Likelihood:                 3799.8
No. Observations:                3651   AIC:                            -7590.
Df Residuals:                    3646   BIC:                            -7559.
Df Model:                           4
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                        0.0737      0.118      0.626      0.531      -0.157       0.304
real_net_monetary_index     -0.0066      0.020     -0.331      0.741      -0.046       0.033
men_proportion              -0.0905      0.228     -0.397      0.691      -0.537       0.356
65+_proportion              -0.0452      0.100     -0.450      0.653      -0.242       0.152
detector_expensive_dummy     0.0433      0.011      4.015      0.000       0.022       0.064
==============================================================================
Omnibus:                     5153.420   Durbin-Watson:                   2.013
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1067572.795
Skew:                           8.455   Prob(JB):                         0.00
Kurtosis:                      85.047   Cond. No.                         273.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.'''

model3 = ols_analysis(df, target_col='finds_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion', 'detector_expensive_dummy','localities_rate'] )
#print(model3)

#tak nic no:):
'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             finds_rate   R-squared:                       0.005
Model:                            OLS   Adj. R-squared:                  0.003
Method:                 Least Squares   F-statistic:                     3.446
Date:                Fri, 02 Jun 2023   Prob (F-statistic):            0.00414
Time:                        14:04:20   Log-Likelihood:                 3800.2
No. Observations:                3651   AIC:                            -7588.
Df Residuals:                    3645   BIC:                            -7551.
Df Model:                           5
Covariance Type:            nonrobust
============================================================================================      
                               coef    std err          t      P>|t|      [0.025      0.975]      
--------------------------------------------------------------------------------------------      
const                        0.0657      0.118      0.556      0.578      -0.166       0.297      
real_net_monetary_index     -0.0110      0.021     -0.532      0.595      -0.052       0.030      
men_proportion              -0.0690      0.229     -0.301      0.763      -0.518       0.380      
65+_proportion              -0.0437      0.100     -0.435      0.664      -0.241       0.153      
detector_expensive_dummy     0.0432      0.011      4.006      0.000       0.022       0.064      
localities_rate              6.8943      8.394      0.821      0.412      -9.564      23.352      
==============================================================================
Omnibus:                     5152.768   Durbin-Watson:                   2.014
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1066991.724
Skew:                           8.453   Prob(JB):                         0.00
Kurtosis:                      85.025   Cond. No.                     8.96e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.       
[2] The condition number is large, 8.96e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
'''

#correlation_matrix = df[['real_net_monetary_index','men_proportion', '65+_proportion', 'detector_expensive_dummy','localities_rate']].corr()
#print(correlation_matrix)
##I dont think there is multicollinearity, see:
'''
                          real_net_monetary_index  men_proportion  65+_proportion  detector_expensive_dummy  localities_rate
real_net_monetary_index                  1.000000        0.125307       -0.197997                  0.017191         0.252678
men_proportion                           0.125307        1.000000       -0.192306                 -0.028418        -0.076486
65+_proportion                          -0.197997       -0.192306        1.000000                  0.006766        -0.048912
detector_expensive_dummy                 0.017191       -0.028418        0.006766                  1.000000         0.018067
localities_rate                          0.252678       -0.076486       -0.048912                  0.018067         1.000000
'''



df['localities_rate'] = df['localities_rate']*100
from E_fctn_display_unique_values import display_unique_values
#print(display_unique_values(df, 'localities_rate'))
#probably transfer it to squared km... i.e. times 100...



#so, with the square kms:
model4 = ols_analysis(df, target_col='finds_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion', 'detector_expensive_dummy','localities_rate'])
#print(model4)
'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             finds_rate   R-squared:                       0.005
Model:                            OLS   Adj. R-squared:                  0.003
Method:                 Least Squares   F-statistic:                     3.446
Date:                Fri, 02 Jun 2023   Prob (F-statistic):            0.00414
Time:                        17:51:55   Log-Likelihood:                 3800.2
No. Observations:                3651   AIC:                            -7588.
Df Residuals:                    3645   BIC:                            -7551.
Df Model:                           5
Covariance Type:            nonrobust
============================================================================================       
                               coef    std err          t      P>|t|      [0.025      0.975]       
--------------------------------------------------------------------------------------------       
const                        0.0657      0.118      0.556      0.578      -0.166       0.297       
real_net_monetary_index     -0.0110      0.021     -0.532      0.595      -0.052       0.030       
men_proportion              -0.0690      0.229     -0.301      0.763      -0.518       0.380       
65+_proportion              -0.0437      0.100     -0.435      0.664      -0.241       0.153       
detector_expensive_dummy     0.0432      0.011      4.006      0.000       0.022       0.064       
localities_rate              0.0689      0.084      0.821      0.412      -0.096       0.234       
==============================================================================
Omnibus:                     5152.768   Durbin-Watson:                   2.014
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1066991.724
Skew:                           8.453   Prob(JB):                         0.00
Kurtosis:                      85.025   Cond. No.                         275.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified. 
'''


# Display the correlation matrix
correlation_matrix = df[['finds_rate','real_net_monetary_index','men_proportion', '65+_proportion', 'detector_expensive_dummy','localities_rate']].corr()
print(correlation_matrix)

#output:
'''
                          finds_rate  real_net_monetary_index  men_proportion  65+_proportion  detector_expensive_dummy  localities_rate
finds_rate                  1.000000                -0.003782       -0.007828       -0.004851                  0.066426         0.013718
real_net_monetary_index    -0.003782                 1.000000        0.125307       -0.197997                  0.017191         0.252678
men_proportion             -0.007828                 0.125307        1.000000       -0.192306                 -0.028418        -0.076486
65+_proportion             -0.004851                -0.197997       -0.192306        1.000000                  0.006766        -0.048912
detector_expensive_dummy    0.066426                 0.017191       -0.028418        0.006766                  1.000000         0.018067
localities_rate             0.013718                 0.252678       -0.076486       -0.048912                  0.018067         1.000000
'''

#model, just try the localities rate a net net_monetary...:

model_try1 = ols_analysis(df, target_col='real_net_monetary_index', feature_cols=['localities_rate'])
#print(model_try1)
'''
                               OLS Regression Results
===================================================================================
Dep. Variable:     real_net_monetary_index   R-squared:                       0.064
Model:                                 OLS   Adj. R-squared:                  0.064
Method:                      Least Squares   F-statistic:                     248.9
Date:                     Sat, 03 Jun 2023   Prob (F-statistic):           2.75e-54
Time:                             11:51:32   Log-Likelihood:                 4525.0
No. Observations:                     3651   AIC:                            -9046.
Df Residuals:                         3649   BIC:                            -9034.
Df Model:                                1
Covariance Type:                 nonrobust
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               0.9761      0.002    508.781      0.000       0.972       0.980
localities_rate     1.0430      0.066     15.775      0.000       0.913       1.173
==============================================================================
Omnibus:                      119.621   Durbin-Watson:                   0.018
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              111.649
Skew:                           0.380   Prob(JB):                     5.70e-25
Kurtosis:                       2.604   Cond. No.                         57.0
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
#so, now, the data sampling chapterr