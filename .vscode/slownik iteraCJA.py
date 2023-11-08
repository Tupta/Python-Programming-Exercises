spam = {'color': 'czerwony', 'age': '42', 'wzrost':'wysoki','imie':'Stefan'}
print("użycie spam.keys() powoduje że poniżej masz klucze:")
for y in spam.keys():
    print(y)
print()
print("użycie spam.values() powoduje że poniżej masz wartości:")
for j in spam.values():
    print(j)
print()

print("użycie spam.items() powoduje poniżej masz elementy tj klucz+wartość:")
for d in spam.items():
    print(d)

spam = {'kolor': 'redczerwony', 'wiek': "42"}
spam.keys()
dict_keys=(['kolor', 'wiek'])
list(spam.keys())

x = 'stefan'

print(f'probujemy zastosowania efki {x} a moze cos jescze sie stanie: {spam.keys()}')

d = x * 5
print(d)