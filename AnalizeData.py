import pandas as pd
import matplotlib.pyplot as plot

df1 = pd.read_excel('ОАД1.xlsx', sheet_name='Справочник компаний')
df2 = pd.read_excel('ОАД1.xlsx', sheet_name='Результаты опроса о доходах')
df3 = pd.read_excel('ОАД1.xlsx', sheet_name='Информация о доходах')
'''перевод таблиц в датафрейм'''
"""print(len(df1.index))"""
i = 0
'''в эту фукнцию будем передавать таблицу с реальными зарплатами сотрудников'''
companies_green = ['ООО "ШАД-111"', 'ГРИНРУС-АТОМ', 'АО "Зелёная энергия"', 'ОАО "ГРИНТРАНПСОРТ"',
                   'АО "Эко-системы управления на транспорте"', 'ИП Иванов И.Б.',
                   'АО "ПИТС"', 'ООО "КБ-14"']


def f(df):
    sal_for_com = [0] * 10
    i = 0
    while i <= (len(df.index)):
        sal_for_per = 0
        # i это номер первого квартала
        if df['id-компании'].loc[df.index[i]] <= 8:
            for j in range(i, i + 4):
                sal_for_per += df["Сумма оклада за период (до вычета налогов)"].loc[df.index[j]] * (
                            100 - df['Величина налога,%'].loc[df.index[i]]) / 100
            ind = df.index[i]
            if df['id-компании'].loc[ind] == 1:
                sal_for_com[0] += sal_for_per
            if df['id-компании'].loc[ind] == 2:
                sal_for_com[1] += sal_for_per
            if df['id-компании'].loc[ind] == 3:
                sal_for_com[2] += sal_for_per
            if df['id-компании'].loc[ind] == 4:
                sal_for_com[3] += sal_for_per
            if df['id-компании'].loc[ind] == 5:
                sal_for_com[4] += sal_for_per
            if df['id-компании'].loc[ind] == 6:
                sal_for_com[5] += sal_for_per
            if df['id-компании'].loc[ind] == 7:
                sal_for_com[6] += sal_for_per
            if df['id-компании'].loc[ind] == 8:
                sal_for_com[7] += sal_for_per
            if df['id-компании'].loc[ind] == 9:
                sal_for_com[8] += sal_for_per
            if df['id-компании'].loc[ind] == 10:
                sal_for_com[9] += sal_for_per
        if i + 4 + 2 >= len(df.index):
            break
        i += 4
    return sal_for_com


# здесь работаем с таблицей с опросом
def opros_f(df):
    sal_for_com = [0] * 10
    i = 0
    while i < (len(df.index)):
        sal_for_per = 0
        ind = df.index[i]
        if df['Компания'].loc[df.index[i]] in companies_green:
            sal_for_per = df['Годовой доход после вычета налогов'].loc[ind]
            if df['Компания'].loc[df.index[i]] == companies_green[0]:
                sal_for_com[0] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[1]:
                sal_for_com[1] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[2]:
                sal_for_com[2] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[3]:
                sal_for_com[3] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[4]:
                sal_for_com[4] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[5]:
                sal_for_com[5] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[6]:
                sal_for_com[6] += sal_for_per
            if df['Компания'].loc[df.index[i]] == companies_green[7]:
                sal_for_com[7] += sal_for_per
        i += 1
    return sal_for_com


opros_salary = [int(x) for x in opros_f(df2)[:-2] ]
real_salary = [int(x) for x in f(df3)[:-2] ]
print(real_salary)
print(opros_salary)

# average salary
s1 = []
s2 = []
for i in range(len(df1.index)-2):
    s1.append(int(real_salary[i] / df1['Среднесписочная численность'].loc[df1.index[i]]))
    s2.append(int(opros_salary[i] / df1['Среднесписочная численность'].loc[df1.index[i]]))
print(s1)
print(s2)

#средний доход, медианный доход, минимальный и максимальный
plot.figure(figsize=(10,10))
plot.bar(companies_green,s1,label = 'Real_salary',width=0.7,bottom =50,align ='edge')
plot.bar(companies_green,s2,label = 'Opros_salary',width=0.7,bottom =50,align ='edge' )


plot.legend()
plot.show()