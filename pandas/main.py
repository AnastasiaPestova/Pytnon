import pandas as pd

fieldnames = ['id', 'name', 'height',
               'birth', 'death', 'death_reason','spouses',
               'divorces', 'spouses_with_children',
               'children']
df= pd.read_csv('IMDbnames_f.csv',
                sep = '#',
               names = fieldnames)

print('Количество людей, у которых детей больше чем супругов')
sc = sum(df['children'] > df['spouses'])
    #df.query('children > spouses ').shape[0]
print(int(sc))

print('самая часто встречающуюся комбинацию супруги-дети в %')
c=df.shape[0]
comb = df.groupby(['spouses','children']).size().reset_index(name='counts').sort_values(by = ['counts'],ascending = False )
print (comb.loc[0,'counts']/c*100)

print ('top-3 причин смерти, которым соответствует самый большой средний рост людей')
rez = df.groupby(['death_reason']).mean().sort_values(by = ['height', 'death_reason'],ascending = [False,False] ).index.tolist()
print("\n".join(map(str, rez[0:3])))


print ('top-3 причин смерти, которым соответствует самый большой средний рост людей и их было больше 10')
rez = df.groupby(['death_reason']).mean('height').sort_values(by = ['death_reason'],ascending = False )
rez1 = df.groupby(['death_reason']).size().reset_index(name='counts').sort_values(by = ['death_reason'],ascending = False )
rez2=pd.merge(rez, rez1, on=('death_reason'))
rez3=rez2[(rez2['counts']>10)].sort_values(by = 'height',ascending = False)
rez4=rez3.iloc[0:3,0].tolist()
print("\n".join(map(str, rez4)))

print ('Средний рост людей с заданной фамилией')
#s_n=input()
s_n = 'Brown'
df['second_name'] = df['name'].str.split(' ').str[-1]
rez = df.groupby(['second_name']).mean('height')
rez1 = rez.loc[s_n,'height']
print(rez1)

df.drop(['second_name'], axis = 1, inplace= True )

print ('Вывести процент пропусков для переменной, которая содержит максимальное количество пропусков')
c = df.shape[0]
id_nan = df['id'].isna().sum()
id_nan_pc = id_nan/c*100
name_nan = df['name'].isna().sum()
name_nan_pc = name_nan/c*100
height_nan = df['height'].isna().sum()
height_nan_pc = height_nan/c*100
birth_nan = df['birth'].isna().sum()
birth_nan_pc = birth_nan/c*100
death_nan = df['death'].isna().sum()
death_nan_pc = death_nan/c*100
death_reason_nan = df['death_reason'].isna().sum()
death_reason_nan_pc = death_reason_nan/c*100
spouses_nan = df['spouses'].isna().sum()
spouses_nan_pc = spouses_nan/c*100
divorces_nan = df['divorces'].isna().sum()
divorces_nan_pc = divorces_nan/c*100
spouses_with_children_nan = df['spouses_with_children'].isna().sum()
spouses_with_children_nan_pc = spouses_with_children_nan/c*100
children_nan = df['children'].isna().sum()
children_nan_pc = children_nan/c*100
rez = [id_nan_pc, name_nan_pc, height_nan_pc, birth_nan_pc, death_nan_pc, death_reason_nan_pc, spouses_nan_pc, divorces_nan_pc, spouses_with_children_nan_pc, children_nan_pc]
print(max(rez))

print ('Вывести имя первого по списку человека, который родился раньше всех, если учитывать только год рождения')
df['year'] = df['birth'].str.split('-').str[0].str.split(' ').str[0]
rez = df.reset_index().sort_values(by = ['year'],ascending = True).set_index('index').iloc[0,1]
print (rez)

df.drop(['year'], axis = 1, inplace= True )

print ('число детей, которому соответствует максимальный средний возраст людей в годах')
df['year_birth'] = df['birth'].str.split('-').str[0].str.split(' ').str[0]
df['year_death'] = df['death'].str.split('-').str[0].str.split(' ').str[0]
df['age'] = pd.to_numeric(df['year_death'], errors='coerce') - pd.to_numeric(df['year_birth'], errors='coerce')
rez = df.groupby(['children']).mean().sort_values(by = ['age'],ascending = False ).index.tolist()
print(rez[0])
