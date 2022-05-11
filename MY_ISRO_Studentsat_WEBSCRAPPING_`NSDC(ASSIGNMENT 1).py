#!/usr/bin/env python
# coding: utf-8

# In[68]:


# WEB SCRAPPING WEBSITE OF ISRO 


# In[69]:


pip install bs4


# In[70]:


pip install requests


# In[71]:


from bs4 import BeautifulSoup


# In[72]:


import requests


# In[73]:


url = "https://www.isro.gov.in/spacecraft/list-of-university-academic-institute-satellites"


# In[74]:


Website_Allow = requests.get(url)


# In[75]:


Website_Allow


# In[76]:


soup=BeautifulSoup(Website_Allow.text)


# In[77]:


soup


# In[78]:


Mission=soup.select(".views-field-title a")


# In[79]:


Mission


# In[80]:


Missions_List=[]


# In[81]:


for i in Mission:
    Missions_List.append(i.text)


# In[82]:


Missions_List


# In[83]:


Date=soup.select(".date-display-single")


# In[84]:


Date


# In[85]:


Date_of_launch=[]


# In[86]:


for j in Date:
    Date_of_launch.append(j.text)


# In[87]:


Date_of_launch


# In[88]:


Launcher=soup.select("td.views-field-field-launch-vehicle a")


# In[89]:


Launcher


# In[90]:


Launcher_vehicle=[]


# In[91]:


for k in Launcher:
    Launcher_vehicle.append(k.text.strip('\n'))


# In[92]:


Launcher_vehicle


# In[93]:


Loadmass=soup.select("td.views-field-field-mass")


# In[94]:


Loadmass


# In[95]:


Mission_Loadmass=[]


# In[96]:


for l in Loadmass:
    Mission_Loadmass.append(l.text.strip('\n'))


# In[97]:


Mission_Loadmass


# In[98]:


import pandas as pd


# In[99]:


Missions_Dataset=pd.DataFrame(Missions_List,columns=["Mission_Names"])


# In[100]:


Missions_Dataset


# In[101]:


Missions_Dataset["Launcher"]=Launcher_vehicle


# In[102]:


Missions_Dataset["Loadmass"]=Mission_Loadmass


# In[103]:


Missions_Dataset


# In[104]:


Missions_Dataset["Date"]=Date_of_launch


# In[105]:


Missions_Dataset


# In[106]:


Missions_Dataset1=Missions_Dataset


# In[107]:


Missions_Dataset1


# In[108]:


Missions_Dataset.to_csv("My_ISR0_studentsat_webscrapping.csv")


# In[109]:


Missions_Dataset.isnull().sum()


# In[110]:


if __name__=='__main__':
    Missions_Dataset1=pd.read_csv("My_ISR0_studentsat_webscrapping.csv")
    print(Missions_Dataset1)
    print(type( Missions_Dataset1))
Missions_Dataset1['Date']=Missions_Dataset1['Date'].str.replace(r'\W',"")      
print(Missions_Dataset1)
        


# In[111]:


Missions_Dataset1


# In[112]:


Missions_Dataset1.Launcher.unique()


# In[113]:


order=['PSLV-C52/EOS-04 Mission', 'PSLV-C51/Amazonia-1', 'PSLV-C44',
       'PSLV-C38 / Cartosat-2 Series Satellite', 'PSLV-C35 / SCATSAT-1',
       'PSLV-C34 / CARTOSAT-2 Series Satellite',
       'PSLV-C18/Megha-Tropiques', 'PSLV-C15/CARTOSAT-2B',
       'PSLV-C12 / RISAT-2']


# In[114]:


order


# In[115]:


from sklearn.preprocessing import OrdinalEncoder


# In[116]:


ord_enc=OrdinalEncoder(categories=[order])


# In[117]:


ord_enc.fit(Missions_Dataset1[["Launcher"]])


# In[118]:


Missions_Dataset1["Launcher"]= ord_enc.transform(Missions_Dataset1[["Launcher"]])


# In[119]:


Missions_Dataset1


# In[120]:


import pandas as pd


# In[121]:


from sklearn.preprocessing import LabelEncoder


# In[122]:


Missions_Dataset1=pd.DataFrame(Missions_Dataset1)


# In[123]:


Missions_Dataset1


# In[124]:


lab_encode=LabelEncoder()


# In[125]:


Missions_Dataset1["Launcher"]=lab_encode.fit_transform(Missions_Dataset1["Launcher"])


# In[126]:


Missions_Dataset1


# In[127]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# In[128]:


col_trans=ColumnTransformer([('encoder',OneHotEncoder(),[4])],remainder='passthrough')


# In[129]:


Missions_Dataset1=np.array(col_trans.fit_transform(Missions_Dataset1),dtype=np.str)


# In[130]:


Missions_Dataset1


# In[131]:


Missions_Dataset2=pd.DataFrame(Missions_Dataset1)


# In[132]:


Missions_Dataset2


# In[133]:


Missions_Dataset1


# In[134]:


Missions_Dataset


# In[ ]:




