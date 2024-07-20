# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
print("welcome to the Toolkit for Finance T2 2024, hello from tingting wu")  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f"The slice from index 2 through end is {lst[2:]}" )

tuple =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(f'the lice from index -8 through 9 is {tuple[-8:20]}')

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic0['a'])

dic = { ['a', 'b']: 1, 'c': 2,}
dic = { ('a', 'b'): 1, 'c': 2, }

tup = (1, 2, ['a', 'b'])
dic = {tup: 'value'}

tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}

lst_a = ['a']
lst_b = ['b', lst_a]
lst_c = ['b', ['a']]
lst_c[1].append("c")
print(lst_a)

a = 'this is called'
b = 'problem'
b = print
a = f'{a} Parsons {b}'
b(a)

tup = (1, 2, ['a', 'b'])
dic = {tup: 'value'}


import yfinance

start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')


a = "Hi"
if a:
    a("There")

s = {'a', 'c', 'd'}

print('a' in s or 'b' not in s)

print('a'in s or not ('b' in s))

print( not ( 'a' not in s and 'b' in s ))



import pandas as pd

# Part (a)
# Create a pandas series called series_abc with
# index ['a', 'b', 'c'] and values [1, 2, 3]
series_abc = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'])

# Part (b)
# Given the stock price-date dictionary prc_date
# listed below, create a pandas series series_stk
# with the dates as indices and the prices as values.
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
series_stk = pd.Series(data = list(prc_date.keys()),index = list(prc_date.values()))

# Part c
# Given the dictionary
dic = {i:i+1 for i in range(10000)}
# create a Pandas series called series_ones
# with indices from 0 through 9999 and with
# all values equal to 1.
# Do not use a secondary dictionary to create the series in Pandas.
# Instead, specify the data and index arguments directly.
series_ones = pd.Series(data=[1]*10000, index=range(10000))

print(series_abc)
print(series_stk)
print(series_ones)


lst = [1,2]
lst[0] = -99
print( id(lst) )

lst0 = [1, 2]
lst1 = [1, 2]
lst2 = lst0

lst2[0] = -99
print(lst2[0])