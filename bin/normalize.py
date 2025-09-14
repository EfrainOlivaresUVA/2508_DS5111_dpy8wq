import pandas


# The Price column in ygainers has the price in a longer string that looks like
# price amount_difference (percentage_difference)
# You need to parse the string to isolate the price
df = pandas.read_csv('ygainers.csv')

print(df[['Price']].head())

df['price'] = df['Price'].apply(lambda x: str(x).split()[0])

print(df[['Price', 'price']].head())


# The wjs version will have the symbol embedded in a longer string
# It usually looks like this "QMMM Holdings Ltd. Cl A (QMMM)"
# this rege can help extract it.

rex = r'\(([A-Z]+)\)$'
import re
df = pandas.read_csv('wsjgainers.csv')
print(df.columns)
print(df[['Unnamed: 0']].head())

df['symbol'] = df['Unnamed: 0'].apply(lambda x: re.findall(rex, x)[0])

print(df[['Unnamed: 0', 'symbol']].head())



