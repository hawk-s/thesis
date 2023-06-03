from N_fctn_load_excel import load_excel_to_dataframe

df = load_excel_to_dataframe('M_main_dataset.xlsx')
#print(df)

#print(df.columns)

df_copy_1 = df.copy()

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
#print(correlation_matrix)

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


#print(df.columns)

# Assuming 'df' is your DataFrame
columns = ['link', 'experience', 'contributions', 'comments', 'artifacts', 'coins',
           'residence_additional_info', 'real_net_monetary_index', 'finds_rate',
           'coins_rate', 'detector_expensive_dummy', 'localities_rate']

correlation_matrix = df[columns].corr()

#print(correlation_matrix)

import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5,  vmin=-1, vmax=1)
plt.title('Correlation Matrix')
#plt.show()

















#ANALYSIS FOR COINS RATE (according to the correlation matrix):

df_copy_1 = subset_non_none_values(df_copy_1,column='real_net_monetary_index')
#print(df)

df_copy_1 = subset_non_none_values(df_copy_1,column='coins_rate') 
#print(df)

modelc1 = ols_analysis(df_copy_1, target_col='coins_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion'] )
#print(modelc1)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             coins_rate   R-squared:                       0.001
Model:                            OLS   Adj. R-squared:                 -0.000
Method:                 Least Squares   F-statistic:                    0.6073
Date:                Sat, 03 Jun 2023   Prob (F-statistic):              0.610
Time:                        15:43:47   Log-Likelihood:                 4416.3
No. Observations:                2765   AIC:                            -8825.
Df Residuals:                    2761   BIC:                            -8801.
Df Model:                           3
Covariance Type:            nonrobust
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.0781      0.079      0.987      0.324      -0.077       0.233
real_net_monetary_index     0.0113      0.013      0.852      0.394      -0.015       0.037
men_proportion             -0.1707      0.152     -1.120      0.263      -0.469       0.128
65+_proportion             -0.0048      0.067     -0.071      0.943      -0.136       0.127
==============================================================================
Omnibus:                     5462.790   Durbin-Watson:                   2.016
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          9323371.638
Skew:                          15.762   Prob(JB):                         0.00
Kurtosis:                     285.723   Cond. No.                         278.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''



modelc2 = ols_analysis(df_copy_1, target_col='coins_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion', 'link', 'detector_expensive_dummy'] )
#print(modelc2)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             coins_rate   R-squared:                       0.018
Model:                            OLS   Adj. R-squared:                  0.017
Method:                 Least Squares   F-statistic:                     10.32
Date:                Sat, 03 Jun 2023   Prob (F-statistic):           8.04e-10
Time:                        15:43:47   Log-Likelihood:                 4441.0
No. Observations:                2765   AIC:                            -8870.
Df Residuals:                    2759   BIC:                            -8834.
Df Model:                           5
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                        0.0564      0.079      0.719      0.472      -0.098       0.210
real_net_monetary_index      0.0104      0.013      0.797      0.425      -0.015       0.036
men_proportion              -0.1250      0.151     -0.826      0.409      -0.422       0.172
65+_proportion              -0.0120      0.067     -0.181      0.857      -0.142       0.118
link                         0.0233      0.005      4.562      0.000       0.013       0.033
detector_expensive_dummy     0.0336      0.007      5.110      0.000       0.021       0.047
==============================================================================
Omnibus:                     5439.616   Durbin-Watson:                   2.008
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          9277299.939
Skew:                          15.604   Prob(JB):                         0.00
Kurtosis:                     285.050   Cond. No.                         279.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''


modelc3 = ols_analysis(df_copy_1, target_col='coins_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion', 'link', 'detector_expensive_dummy', 'contributions', 'comments'] )
#print(modelc3)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             coins_rate   R-squared:                       0.019
Model:                            OLS   Adj. R-squared:                  0.017
Method:                 Least Squares   F-statistic:                     7.806
Date:                Sat, 03 Jun 2023   Prob (F-statistic):           2.19e-09
Time:                        15:43:47   Log-Likelihood:                 4442.5
No. Observations:                2765   AIC:                            -8869.
Df Residuals:                    2757   BIC:                            -8822.
Df Model:                           7
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                        0.0544      0.079      0.693      0.488      -0.100       0.208
real_net_monetary_index      0.0094      0.013      0.721      0.471      -0.016       0.035
men_proportion              -0.1191      0.151     -0.787      0.431      -0.416       0.178
65+_proportion              -0.0126      0.067     -0.190      0.849      -0.143       0.118
link                         0.0223      0.005      4.330      0.000       0.012       0.032
detector_expensive_dummy     0.0327      0.007      4.922      0.000       0.020       0.046
contributions             2.206e-05   3.41e-05      0.647      0.518   -4.48e-05    8.89e-05
comments                  1.647e-06   1.44e-06      1.145      0.252   -1.17e-06    4.47e-06
==============================================================================
Omnibus:                     5439.473   Durbin-Watson:                   2.011
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          9262287.770
Skew:                          15.604   Prob(JB):                         0.00
Kurtosis:                     284.819   Cond. No.                     1.36e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.36e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
'''




















#ANALYSIS FOR ARTIF RATE BUT ACCORDING TO THE CORRELATION MATRIX:
model_corr_1 = ols_analysis(df, target_col='finds_rate', feature_cols=['real_net_monetary_index','men_proportion', '65+_proportion', 'detector_expensive_dummy', 'link', 'residence_additional_info'] )
#print(model_corr_1)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

'''
                            OLS Regression Results
==============================================================================
Dep. Variable:             finds_rate   R-squared:                       0.014
Model:                            OLS   Adj. R-squared:                  0.013
Method:                 Least Squares   F-statistic:                     8.879
Date:                Sat, 03 Jun 2023   Prob (F-statistic):           1.22e-09
Time:                        15:58:51   Log-Likelihood:                 3818.1
No. Observations:                3651   AIC:                            -7622.
Df Residuals:                    3644   BIC:                            -7579.
Df Model:                           6
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0530      0.117      0.452      0.651      -0.177       0.283
real_net_monetary_index      -0.0108      0.020     -0.540      0.590      -0.050       0.028
men_proportion               -0.0410      0.227     -0.181      0.857      -0.486       0.404
65+_proportion               -0.0498      0.100     -0.498      0.618      -0.246       0.146
detector_expensive_dummy      0.0419      0.011      3.892      0.000       0.021       0.063
link                          0.0320      0.008      3.882      0.000       0.016       0.048
residence_additional_info     0.0813      0.019      4.350      0.000       0.045       0.118
==============================================================================
Omnibus:                     5101.564   Durbin-Watson:                   2.017
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1014449.397
Skew:                           8.306   Prob(JB):                         0.00
Kurtosis:                      82.954   Cond. No.                         273.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''


#so the models so far nothing special...
#now, create models for real net monetary index filled with 1 if None... but what with the people that does not have any submitted find/coin... I suggest to again split the analysis
#and do it for 0s filled (i.e. for all the people) and then remove those artifs and coins Na's---

