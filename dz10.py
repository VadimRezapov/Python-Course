import pandas as pd
import seaborn as sns


def Zadacha1():
    df = pd.read_csv('data.csv', sep=';',encoding='cp1251')
    slice1 = df.loc[2:19, ['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015']]
    print(slice1.max())




def Zadacha2():
    slice2 = df.loc[33:40, ['Субъект РФ', 'Численность студентов, очная форма, человек, 2017']]
    plot = sns.barplot(data=slice2, x='Субъект РФ', y='Численность студентов, очная форма, человек, 2017')
    plot.set_xticklabels(plot.get_xticklabels(),rotation = 90)




def Zadacha3():
    slice3 = df[df['Численность студентов заочная форма, человек, 2019'] < 10000]
    plot = sns.barplot(data=slice3, x='Субъект РФ', y='Численность студентов заочная форма, человек, 2019')
    plot.set_xticklabels(plot.get_xticklabels(),rotation = 90)