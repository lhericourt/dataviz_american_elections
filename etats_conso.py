
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

def agregat(nom):
    
    
    usa = pd.read_csv(nom, sep=';', names= ['date', 'state_name', 'candidate'])

    usa['nb_of_vote'] = 1

    usa_group2 = usa.groupby(['date','state_name','candidate'], as_index = True)['nb_of_vote'].sum()

    usa_group2.to_csv(path = '/Users/havard-macpro/Documents/Telecom_paristech/etats_usa/' + nom, header = True)
    
    return




# In[3]:

print("debut")
agregat('2016-11-08-20-00_Minnesota.txt')
agregat('2016-11-08-20-01_Alabama.txt')
agregat('2016-11-08-20-01_Montana.txt')
agregat('2016-11-08-20-01_Utah.txt')
agregat('2016-11-08-20-02_Caroline_du_Sud.txt')
agregat('2016-11-08-20-02_New_York.txt')
agregat('2016-11-08-20-03_Nouveau_Mexique.txt')
agregat('2016-11-08-20-04_Californie.txt')
agregat('2016-11-08-20-04_Colorado.txt')
agregat('2016-11-08-20-05_Connecticut.txt')
agregat('2016-11-08-20-08_District_de_Columbia.txt')
agregat('2016-11-08-20-08_Kentucky.txt')
agregat('2016-11-08-20-09_Caroline_du_Nord.txt')
agregat('2016-11-08-20-09_Vermont.txt')
agregat('2016-11-08-20-10_Dakota_du_Sud.txt')
agregat('2016-11-08-20-11_Alaska.txt')
agregat('2016-11-08-20-13_Arkansas.txt')
agregat('2016-11-08-20-13_Washington.txt')
agregat('2016-11-08-20-15_Hawai.txt')
agregat('2016-11-08-20-17_Wisconsin.txt')

print("Fini")


# In[10]:




# In[4]:

print("debut")
agregat('2016-11-08-20-19_Georgie.txt')
agregat('2016-11-08-20-22_Ohio.txt')
agregat('2016-11-08-20-24_Missouri.txt')
agregat('2016-11-08-20-24_New_Hampshire.txt')
agregat('2016-11-08-20-24_Virginie.txt')
agregat('2016-11-08-20-27_Iowa.txt')
agregat('2016-11-08-20-28_Delaware.txt')
agregat('2016-11-08-20-29_Arizona.txt')
agregat('2016-11-08-20-31_Louisiane.txt')
agregat('2016-11-08-20-31_Massachusetts.txt')
agregat('2016-11-08-20-31_Texas.txt')
agregat('2016-11-08-20-34_Dakota_du_Nord.txt')
agregat('2016-11-08-20-35_Tennessee.txt')
agregat('2016-11-08-20-36_Wyoming.txt')
agregat('2016-11-08-20-37_Floride.txt')
agregat('2016-11-08-20-37_Illinois.txt')
agregat('2016-11-08-20-40_Nevada.txt')
agregat('2016-11-08-20-41_Idaho.txt')
agregat('2016-11-08-20-41_Pennsylvanie.txt')
agregat('2016-11-08-20-43_Virginie_Occidentale.txt')
agregat('2016-11-08-20-48_Maryland.txt')
agregat('2016-11-08-20-48_Mississippi.txt')
agregat('2016-11-08-20-48_Rhode_Island.txt')
agregat('2016-11-08-20-50_Michigan.txt')
agregat('2016-11-08-20-51_Oklahoma.txt')
agregat('2016-11-08-20-52_Nebraska.txt')
agregat('2016-11-08-20-56_New_Jersey.txt')
agregat('2016-11-08-20-57_Indiana.txt')
agregat('2016-11-08-20-57_Kansas.txt')
agregat('2016-11-08-20-58_Maine.txt')
agregat('2016-11-08-20-59_Oregon.txt')
print("fini")


# In[ ]:




# In[43]:

state_info = pd.read_csv('/Users/havard-macpro/Documents/Telecom_paristech/etats_usa/state_info4.csv', sep=';', names= ['code','state', 'gd_elec', 'votants'])



# In[44]:

state_info


# In[20]:

code_etat = pd.read_csv('/Users/havard-macpro/Documents/Telecom_paristech/etats_usa/codes_etats2.txt', sep=',', names= ['code','state'])


# In[21]:

code_etat.head()


# In[22]:

code_etat


# In[23]:

state_info


# In[24]:

code_etat2 = pd.DataFrame({'key': code_etat['state'],'value': code_etat['code']})


# In[26]:

#code_etat2


# In[38]:

state_info2 = pd.DataFrame({'key': state_info['state'],'value': state_info['gd_elec']})


# In[35]:

state_info2


# In[ ]:




# In[ ]:



