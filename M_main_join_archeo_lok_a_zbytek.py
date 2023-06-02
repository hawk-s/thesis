import pandas as pd
from A_fctn_join_dataframes import join_dataframes
from A_fctn_join_two_columns import join_columns
from B_fctn_drop_columns import drop_columns
from B_fctn_rename_columns import rename_columns
import numpy as np
df1 = pd.read_excel('lovci_s_prijmy_bez_archeo_lok.xlsx')
#print(df1.columns)

df1 = drop_columns(df1, ['snatky celkem', 'snatky na 1 000 obyvatel', 'rozvody celkem',
       'rozvody na 1 000 obyvatel', 'rozvody na 100 snatku',
       'prumerny vek matky pri narozeni ditete',
       'prumerny vek matky pri narozeni ditete, prvni dite:',
       'zive narozeni na 1 000 obyvatel', 'potraty celkem',
       'potraty celkem na 100 narozenych',
       'umela preruseni tehotenstvi na 100 narozenych', 'zemreli celkem',
       'zemreli, muzi', 'zemreli, zeny ', 'zemreli na 1 000 obyvatel',
       'pristehovali', 'pristehovali muzi', 'pristehovali zeny',
       'pristehovali 0-14', 'pristehovali 15-64', 'pristehovali 65+',
       'pristehovali na 1 000 obyvatel', 'vystehovali', 'vystehovali muzi',
       'vystehovali zeny', 'vystehovali 0-14', 'vystehovali 15-64',
       'vystehovali 65+', 'vystehovali na 1 000 obyvatel',
       'prirustek stehovanim', 'prirustek stehovanim muzi',
       'prirustek stehovanim zeny', 'prirustek stehovanim 0-14',
       'prirustek stehovanim 15-64', 'prirustek stehovanim 65+',
       'vnitrni stehovani v so pou celkem', 'vnitrni stehovani muzi',
       'vnitrni stehovani zeny', 'prirustek celkovy', 'prirustek prirozeny',
       'prirustek stehovanim.1', 'prirustek na 1 000 obyvatel: celkovy',
       'prirustek na 1 000 obyvatel: prirozeny',
       'prirustek na 1 000 obyvatel: stehovanim'])


from C_fctn_create_dummy import create_dummy_variable
#print(df1['odkaz']) 
df1_copy = df1.copy()
df1_copy = create_dummy_variable(df1_copy,'odkaz', missing_values=['[]'])

print(df1_copy['odkaz'][60:66])
print('++++++++++++++++++++++++++++++++++++++++++++++++++')


df1_copy = drop_columns(df1_copy, ['Unnamed: 0', 'okres_y', 'zeny 65+', 'prumerny vek zeny', 
                   'index stari (65+ / 0 -14 v %) zeny',
                   'index stari (65+ / 0 -14 v %) celkem', 'muzi 0-14',
                   'stav obyvatel 31.12., 0-14', 'stav obyvatel 31.12., 15-64', 'muzi 15-64',
                   'muzi 15-64','prumerny vek muzi', 'index stari (65+ / 0 -14 v %) muzi', 'zeny',
                   'zeny 0-14', 'zeny 15-64','  muzi 65+'])
#print(df1_copy['bydliste_dalsi_info_1'])
df1_copy_c = df1_copy.copy()
df1_copy_c = create_dummy_variable(df1_copy_c, 'bydliste_dalsi_info_1', missing_values=None)


print(df1_copy_c['bydliste_dalsi_info_1'][46:52])
print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')


#print(df1_copy_c.columns)
df1_copy_c = drop_columns(df1_copy_c, ['bydliste_dalsi_info_2', 'bydliste_dalsi_info_3',
       'bydliste_dalsi_info_4', 'bydliste_dalsi_info_5'])


#creating dummy out of nalezy_rate
from C_fctn_create_dummy import create_dummy_variable_specific

dfc = df1_copy_c.copy()
dfc = create_dummy_variable_specific(dfc, 'rate_nalezy', missing_values=[0, None], replace=False) #here I use specific fction to get three values of dummy 0,1, NaN


print(dfc['rate_nalezy'])
print(dfc['rate_nalezy_dummy'])
print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')


#creating dummy out of mince_rate
dfc = create_dummy_variable_specific(dfc, 'rate_mince', missing_values=[0, None], replace=False) 
print(dfc['rate_mince'])
print(dfc['rate_mince_dummy'])
print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')


#print(dfc.head())


#creating sum of the rate_nalezy_dummy and rate_mince_dummy values [NaN, 0, 1, 2]; resulting column is called 'sum_column':
from D_fctn_create_sum_column import create_sum_column

dfc = create_sum_column(dfc,'rate_nalezy_dummy', 'rate_mince_dummy')

#print(dfc)


#just renaming the dummies/columns so that it is clear that it represents the cases when there is no find -
#- NaN, when there is find but no submitted - 0, when there is one of coins or artifacts submitted - 1, if both - 2. 
dfc = rename_columns(dfc, {'sum_column': 'rate_together_dummy'})
#print(dfc)



#creating a dummy containing zeros and 1s only, i.e. if one submitted either coin or artifact it has 1, if not 0:
#since the following specific fction only searches for 0 and NOnes, not for 1s... no matter the argument 'missing_values' it can be removed---
dfc = create_dummy_variable_specific(dfc, 'rate_together_dummy', missing_values=[0, 1, None], replace=False)
#print(dfc)





#renaming the dummy resulting from the previous line of code:
dfc = rename_columns(dfc, {'rate_together_dummy_dummy': 'either_coin_or_artif_submitted_dummy'})
#print(dfc)






#creating dummy out of the sum of the dummies, i.e. 1 in the following dummy indicates that the person submitted both a coin and an artifact...
##the following function takes as an argument the sum_column (origianlly) - renamed to rate_togegther_dummy, 
# i.e. the column containing nans 0s,1s and 2s, and creates a dummy where 1 is when both coin and artifact were submitted---
from D_fctn_subtract_columns import subtract_columns

dfc = subtract_columns(dfc, 'rate_together_dummy', 'either_coin_or_artif_submitted_dummy', result_column='both_coin_and_artif_submitted')
#print(dfc.iloc[12])


print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
print(dfc['rate_together_dummy'])
print(dfc['either_coin_or_artif_submitted_dummy'])
print(dfc['both_coin_and_artif_submitted'])




#creating dummy that indicates if one uploaded at least 1 find or coin (1), or if one did not upload anything (0)
#however we can assume that one created an account since he/she is a metal detectorist...with the intention to participate
#because otherwise one can simply proceed without an account...
dfc = create_dummy_variable(dfc, 'either_coin_or_artif_submitted_dummy', missing_values=None, replace= False)


#renaming the dummy resulting from the previous line of code:
dfc = rename_columns(dfc, {'either_coin_or_artif_submitted_dummy_dummy': 'uploaded_at_least_one_artif_or_coin_dummy'})
#print(dfc)
print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
print(dfc['uploaded_at_least_one_artif_or_coin_dummy'])











#the following prints the unique values in the column, so that one can see how many people did not upload a find...
from E_fctn_display_unique_values import display_unique_values

unique_values_df = display_unique_values(dfc, 'uploaded_at_least_one_artif_or_coin_dummy')
print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
print(unique_values_df)
#output:
'''
++++++++++++++++++++++++++++++++++++++++++++++++++
   Value  Count
0      1   7622
1      0    106
'''



#print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
#print(dfc.columns)




print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
print(display_unique_values(dfc,'pou')) #interesting, cause we can see that we have people from 355 out of 393 POU -> 38,cca 1/10 missing.



#pocty, viz:
'''
++++++++++++++++++++++++++++++++++++++++++++++++++
                     Value  Count
0       Hlavní město Praha    417
1                     Brno    210
2                    Plzeň    115
3                  Olomouc     87
4         České Budějovice     78
..                     ...    ...
350     Teplice nad Metují      1
351                Hranice      1
352                  Hulín      1
353                 Kouřim      1
354  Rokytnice nad Jizerou      1 
'''

#potiz, mame vice zahrnutou prahu, brno atd.. mozna taky ne, protoze to muze reflektovat hustotu zalidneni

print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')









#zbyva vytvorit dummy na detik...
#+ muzi/pocet obyv, 65+/pocet obyv

#a jedem modely...

dfc = rename_columns(dfc, {'stav obyvatel 31.12.': 'number_of_citizens', ' stav obyvatel 31.12., 65+': 'number_of_citizens_65+', 'prumerny vek celkem': 'average_age_all', 'muzi': 'men_number'})


print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
print(dfc.columns)

#create columns indicating the proportion of men in the population
#and the proportion of retired (65+) in the population:

dfc['men_proportion'] = dfc['men_number']/dfc['number_of_citizens']

dfc['65+_proportion'] = dfc['number_of_citizens_65+']/dfc['number_of_citizens']

print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')


#check if it is the case that average age comes hand in hand with proportion of elderly --- and it sure does:
print(dfc['average_age_all'])
print(dfc['65+_proportion'])


#interesting_men_proportion:
#print(dfc['men_proportion'])





#so, we have 899 distinct municipalities:
print(display_unique_values(dfc, 'obec'))
'''
++++++++++++++++++++++++++++++++++++++++++++++++++
                Value  Count
0               Praha    372
1                Brno    210
2               Plzeň    114
3             Olomouc     84
4    České Budějovice     73
..                ...    ...
894           Otradov      1
895            Krouna      1
896            Úvalno      1
897            Krasov      1
898   Ratibořské Hory      1

[899 rows x 2 columns]
'''



#now, the metal detector dummy:

print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')

print(display_unique_values(dfc, 'detektor'))
'''
                    Value  Count
0             Equinox 800    126
1             Equinox 600     90
2                 XP Deus     84
3            Vanquish 540     70
4     Minelab Equinox 800     62
...                   ...    ...
3879                TEJON      1
3880           Zero lp II      1
3881        Rutus proxima      1
3882           Simplex +,      1
3883               XP-250      1

'''



detectors_to_search = pd.DataFrame([
"Manticore",
"CTX 3030",
"GPX 5000",
"Excalibur II",
"Standard MP V2",
"Standard MP V3",
"Spectra V3i",
"GTI 2500",
"Axiom MS2",
"Axiom MS3",
"GPX 6000",
"GPZ 7000",
"SDC 2300",
"ATX",
"SSP-5100",
"UPEX ONE 2",
"GPX 4500",
"Invenio PRO"
])

'''Manticore, CTX 3030, GPX 5000, Excalibur II, Standard MP V2, Standard MP V3, Spectra V3i, GTI 2500, Axiom MS2, Axiom MS3,
GPX 6000, GPZ 7000, SDC 2300, ATX, SSP-5100, UPEX ONE 2, GPX 4500, Invenio PRO'''



#convert the above list to lower and without spaces:
from A_fctn_replace_and_lowercase import replace_special_characters
from E_fctn_remove_spaces import remove_spaces
print(detectors_to_search)

detectors_to_search = replace_special_characters(detectors_to_search, 0)
#print(detectors_to_search)

detectors_to_search = remove_spaces(detectors_to_search, 0)
print(detectors_to_search)
#data on metal detectors and their prices obtained from website lovecpokladu.cz and revisited on heureka.cz and via google search.




#convert the dectors of people to lower and without spaces:
dfc = replace_special_characters(dfc, 'detektor', new_column='detektor_lower' )

#print(dfc['detektor_lower'])



dfc = remove_spaces(dfc, 'detektor_lower')

print(dfc['detektor_lower'])



#create dummy whenever the detector is above 30k czk, i.e. above the average income at about the year 2018:
from E_fctn_check_values_dummy import check_values

dfc = check_values(dfc, detectors_to_search, 'detektor_lower', 'detektor_exp_dummy')

print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
#print(dfc['detektor_exp_dummy'])


print(display_unique_values(dfc, 'detektor_exp_dummy'))
#output:
'''
   Value  Count
0      0   7599
1      1    129'''

#print(dfc)

from F_fctn_save_df_to_json import save_dataframe_to_json

print(dfc.columns)
dfc = rename_columns(dfc, {'profil': 'profile', 'bydliste':'residence', 'detektor': 'detector', 'odkaz': 'link', 'zkusenost': 'experience', 'prispevek': 'contributions',
                          'komentar': 'comments', 'artefakt': 'artifacts', 'mince': 'coins', 'bydliste_j': 'first_residence', 'bydliste_dalsi_info_1': 'residence_additional_info',
                          'okres_x': 'district', 'kraj': 'region', 'mesto': 'city', 'obec': 'municipality', 'orp': 'municipality_with_extended_competence',
                          'pou': 'municipal_office', 'počet_obyvatel__2018': 'population_2018', 'nominální_čistý_peněžní_příjem_': 'nominal_net_monetary_income',
                          'kvartil': 'quartile', 'index_nominálního_čistého_peněž': 'nominal_net_monetary_index',
                          'index_reálného_čistého_peněžníh': 'real_net_monetary_index', 'odevzdano_pocet_nalezy': 'submitted_number_finds',
                          'nalezy_pocet': 'number_finds', 'rate_nalezy': 'finds_rate', 'odevzdano_pocet_mince': 'submitted_number_coins',
                          'mince_pocet': 'number_coins', 'rate_mince': 'coins_rate', 'rok': 'year'})


dfc = rename_columns(dfc, {'rate_nalezy_dummy': 'rate_artifs_dummy', 'rate_mince_dummy': 'rate_coins_dummy', 'detektor_lower': 'detector_lower', 'detektor_exp_dummy': 'detector_expensive_dummy'})
print(dfc.columns)

from N_fctn_load_excel import load_excel_to_dataframe
#save_dataframe_to_json(dfc, 'full_dataset.json')



#save_dataframe_to_excel(dfc, 'full_dataset.xlsx')



#############################################################
#finally join with the archeo localities rates...:) :
#############################################################


archeo_lok_df = load_excel_to_dataframe('summed_areas_pocet_final.xlsx')
#print(archeo_lok_df.columns)


archeo_lok_df = drop_columns(archeo_lok_df, ['Unnamed: 0', 'Unnamed: 0_x', 'kraj_x', 'okres_x', 'orp', 'kraj_y', 'okres_y','Unnamed: 0_y'])



#rename columns:
column_map = {
    'pou': 'municipal_office',
    'obec': 'municipality',
    'vymera_x': 'area_municipality',
    'typ_obce': 'municipality_type',
    'pocet_lokalit': 'number_of_localities_mo',
    'vymera_y': 'area_municipal_office'
}


archeo_lok_df = rename_columns(archeo_lok_df, column_map=column_map)

#print(archeo_lok_df.columns)

archeo_lok_df['localities_rate'] = archeo_lok_df['number_of_localities_mo'] / archeo_lok_df['area_municipal_office']

#print(archeo_lok_df)
#print(max(archeo_lok_df['localities_rate']))

from F_fctn_save_df_to_excel import save_dataframe_to_excel

#save_dataframe_to_excel(archeo_lok_df, 'full_localities_archeo_rate.xlsx')


#musim zase spojit pou a municipality a namergovat to na to:():
              #but first update the municipalities ´, for prague to be the same...
from G_fctn_process_muni_specific import process_municipality

dfc = process_municipality(dfc)



#print(display_unique_values(dfc,'processed_municipality'))

#print(display_unique_values(dfc,'municipality'))
'''                
                Value  Count
0               Praha    417
1                Brno    210
2               Plzeň    114
3             Olomouc     84
4    České Budějovice     73
..                ...    ...
884            Krouna      1
885            Úvalno      1
886            Krasov      1
887            Kladky      1
888         Košařiska      1

[889 rows x 2 columns]
                Value  Count
0               Praha    372
1                Brno    210
2               Plzeň    114
3             Olomouc     84
4    České Budějovice     73
..                ...    ...
894           Otradov      1
895            Krouna      1
896            Úvalno      1
897            Krasov      1
898   Ratibořské Hory      1

[899 rows x 2 columns]
'''



#now, we can join the columns:

archeo_lok_df = join_columns(archeo_lok_df, 'municipal_office', 'municipality', 'municipal_office_municipality')

dfc = join_columns(dfc, 'municipal_office', 'processed_municipality', 'municipal_office_municipality')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(archeo_lok_df)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print(dfc)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


#now wwe save the ddata:

#save_dataframe_to_excel(dfc, 'full_dataset.xlsx')
#save_dataframe_to_excel(archeo_lok_df, 'full_localities_archeo_rate.xlsx')


#now we finallly join the datasets, so that it includes also the archeo localities rates:

join_dataframes('full_dataset.xlsx', 'full_localities_archeo_rate.xlsx', 'M_main_dataset.xlsx', merge_column='municipal_office_municipality')



















#save_dataframe_to_json(dfc, 'full_dataset.json')



