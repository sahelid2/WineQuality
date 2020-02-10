#!/usr/bin/env python
# coding: utf-8

# In[12]:


## Read the data 
import matplotlib
import pandas as pd
data=r"/Volumes/ExtData/Documents/VCU/2nd Sem/Python/data/winequality.csv"
df = pd.read_csv(data, encoding='ISO-8859-1')
df = df.drop(df.columns[0], axis=1)
get_ipython().run_line_magic('matplotlib', 'inline')
#%pylab inline
matplotlib.rcParams['figure.dpi'] = 160
matplotlib.rcParams['figure.figsize'] = (8,6)


# In[13]:


#Activity 1
# Plot with Average Line
import matplotlib.pyplot as plt
import seaborn as sns
# enable inline plots
plt.ion()
df1=df[['fixed acidity', 'volatile acidity', 'citric acid',
       'residual sugar', 'chlorides', 'free sulfur dioxide',
       'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
       'quality']]
num_cols = df1.columns
#num_cols
current_palette = sns.color_palette()
#sns.palplot(current_palette)
fig, axes = plt.subplots(nrows=6, ncols=2,figsize=(18, 21))


for i, ax in enumerate(axes.flat):
    #print(col)
    col = num_cols[i]
    #ax2 = ax.twinx()
    df[col].hist(bins=150, ax=ax,grid=False,color=sns.color_palette("colorblind", 15)[i])
    #average line below
    ax.axvline(x=df[col].mean(),color='black', lw=3)
    ax.set_xlabel(col.capitalize(), size=12)

plt.show()
plt.close();


# In[15]:


#Activity 2
import matplotlib.pyplot as plt
import seaborn as sns

# enable inline plots
plt.ion()
df1=df[['fixed acidity', 'volatile acidity', 'citric acid',
       'residual sugar', 'chlorides', 'free sulfur dioxide',
       'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
       'quality']]
corr_matrix = df1.corr()
plt.figure(figsize=(12, 9))
sns.heatmap(
    corr_matrix,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(10, 200, n=256),
    square=True
)

plt.show()
plt.close();


# In[4]:


#Activity 3
plt.ion()
plt.figure(figsize=(12, 9))
sns.boxplot(x='quality', y='alcohol', data=df1)
plt.xlabel('Quality', fontsize=14, weight='bold')
plt.ylabel('Alchohol', fontsize=14, weight='bold')

plt.show()
plt.close();



# In[5]:


#Activity 4
#Mean alcohol content for each Quality of Wine
df1[['alcohol']].groupby(df1['quality']).mean().add_prefix('mean_')


# In[6]:


#Activity 4
df2=df1[df1['quality']==9]
avg_alcohol_for_best_wine=list(df2['alcohol'].groupby(df1['quality']).mean())[0]
print(f'The average alcohol content for best wine is {avg_alcohol_for_best_wine}.')


# In[7]:


#Activity 5
l=[]
#l.append(list(df[df['wine type']==ty].corr().columns))
for ty in df['wine type'].unique().tolist():
    #print(ty)
    #print(list(df[df['wine type']==ty].corr()['quality']))
    t=list(df[df['wine type']==ty].corr()['quality'])+[ty]
    l.append(t)

#print(l)
df3 = pd.DataFrame(l, columns = list(df[df['wine type']==ty].corr().columns)+['color'])


# In[8]:


df3


# In[16]:



import matplotlib.pyplot as plt
import seaborn as sns
# enable inline plots
plt.ion()
#num_cols
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(17, 9))

k=0
for i, ax in enumerate(axes.flat):

    ty=df['wine type'].unique().tolist()[i]
    #print(ty)
    corr_matrix=df[df['wine type']==ty].corr()
    sns.heatmap(
        corr_matrix,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(10*(k+1), 200*(k+1), n=256),
        #cmap='icefire',
        square=True,
        ax=ax
    )


    ax.set_title(ty)



plt.show()
plt.close();


# In[21]:



import matplotlib.pyplot as plt
import seaborn as sns
# enable inline plots
plt.ion()
#num_cols
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(17, 9))

k=0
for i, ax in enumerate(axes.flat):

    ty=df['wine type'].unique().tolist()[i]
    #print(ty)
    sns.boxplot(x='quality', y='fixed acidity', data=df[df['wine type']==ty],ax=ax)
    ax.set_xlabel('Quality', size=14)
    ax.set_ylabel('Fixed Acidity', size=14)
    ax.set_title(ty, size=16)



plt.show()
plt.close();


# In[ ]:
