rows = open('IMDbnames_f.csv',encoding='utf-8').read().split('\n')
print('количество записей в документе')
i=0
for person in rows:
    i +=1
print(i)
print('Первые 10 актеров')
for person in rows [0:10]:
    name=person.split('#')[1]
    print(name)
print('сколько человек с фамилией Brando')
n=0
for person in rows:
    name=person.split('#')[1]
    last_name= name.split()[-1]
    if last_name=='Brando':
        n +=1
print(n)
print('Сколько человек умерли по причине "natural causes"')
d=0
for person in rows:
    death=person.split('#')[5]
    death_reason= death.lower().split(",")[0]
    if death_reason=='natural causes':
        d +=1
print(d)
print('Чей рост больше 200 см  и они живы)))')
i=0
for person in rows:
    name=person.split('#')[1]
    heigh=person.split('#')[2]
    live=person.split('#')[4]
    if heigh>'200' and live=='':
        i +=1
        t=(40 - len(name))
        print("%3d)"%(i),t*'.'+"%s" % (name))
print('Самый высокий человек')
i='0'
for person in rows:
    heigh=person.split('#')[2]
    if heigh>'200' and heigh<'300' and heigh>i :
        name=person.split('#')[1]
        i=heigh
print(name)
print('Самая часто встречающаяся фамилия')
ln_list=[]
for person in rows:
    name=person.split('#')[1]
    last_name= name.split()[-1]
    ln_list.append(last_name)
##print(ln_list)
d={}
for ln in ln_list:
    d[ln] = d[ln] + 1 if d.get(ln, None) else 1
most_frequent = sorted(d.items(), key=lambda t: t[1])[-1][0]

print(most_frequent)
