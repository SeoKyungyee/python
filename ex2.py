import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
        
hat = pd.read_csv('ch4-1.csv') # hat 변수에 데이터셋 입력
print(hat.head(), end="\n\n") # 위에서부터 5개 데이터 확인

#바차트 그리기
plt.figure(figsize=(15, 10))
plt.bar(hat['hatchery'], hat['chick'], color = ('red','orange','yellow','green','blue','navy','purple'))

plt.title('hatchery statistics')
plt.xlabel('hatchery')
plt.ylabel('chick count')

addtext(hat['hatchery'], hat['chick'])
plt.show()

# 파이차트 그리기
pct = hat['chick']/hat['chick'].sum()
col7 = sns.color_palette('Pastel2', 7)

plt.figure(figsize=(10, 10))
plt.pie(pct, labels = hat['hatchery'], autopct='%.1f%%', colors=col7, counterclock=False)

plt.show()