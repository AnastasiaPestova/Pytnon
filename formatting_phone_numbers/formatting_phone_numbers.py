out = open('results.txt','w')

for tel in open('num.txt').read().strip().split('\n'):
    tel = tel.strip()
    tel = tel.replace('(','')
    tel = tel.replace(')','')
    tel = tel.replace(' ','')
    tel = tel.replace('-','')
    if len(tel)==12 and '8' not in tel[0]:
        print (tel, file=out)
    elif len(tel)==11 and '8' in tel[0]:
        tel=tel.replace(tel[0],'+7')
        print(tel, file=out)
out.close()
