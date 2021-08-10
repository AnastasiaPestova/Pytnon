import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df= pd.read_csv('DogsofZurich.csv')
mpl.style.use('fivethirtyeight')
w = df[df['GESCHLECHT']=='w']['GESCHLECHT'].value_counts()
ww = df[(df['GESCHLECHT']=='w') & (df['GESCHLECHT_HUND']== 'w')]['GESCHLECHT'].value_counts()
wm = df[(df['GESCHLECHT']=='w') & (df['GESCHLECHT_HUND']== 'm')]['GESCHLECHT'].value_counts()
m = df[df['GESCHLECHT']=='m']['GESCHLECHT'].value_counts()
mw = df[(df['GESCHLECHT']=='m') & (df['GESCHLECHT_HUND']== 'w')]['GESCHLECHT'].value_counts()
mm = df[(df['GESCHLECHT']=='m') & (df['GESCHLECHT_HUND']== 'm')]['GESCHLECHT'].value_counts()
print(w, '\n', ww, '\n', wm,'\n',m, '\n',mw, '\n', mm)
ww_pc=ww/w*100
wm_pc=wm/w*100
mw_pc=mw/m*100
mm_pc=mm/m*100

width = 0.6

fig, ax = plt.subplots()

ax.bar('woman-woman', ww_pc,ec='black', width=width,
       label = 'woman-woman')
ax.bar('woman-man', wm_pc,ec='black', width=width,
       label = 'woman-man')
ax.bar('man-woman', mw_pc,ec='black', width=width,
       label = 'man-woman')
ax.bar('man-man', mm_pc,ec='black', width=width,
       label = 'man-man')

ax.set_xticks(['woman-woman','woman-man','man-woman','man-man'])
ax.set_xticklabels(['woman-woman','woman-man','man-woman','man-man'], rotation = 20)
ax.legend()
plt.yticks(range (0,110,10))

plt.title("Gender - dog's gender in per cent")
plt.show()


age=df['ALTER'].value_counts().sort_index()
plt.bar(x = age.index,
        height  = age,
        ec = 'black')
plt.xticks(rotation=20, ha='right')
plt.title("Number of dogs in different " '\n' "age groups of owners")
plt.show()


