# import re
 
# def password(haslo):
# 	hasloRegex_liczba = re.compile(r'.{8,}')    #powyzej 8 znakow
# 	hasloRegex_duze = re.compile(r'[A-Z]+')   # conajmniej 1 duza litera
# 	hasloRegex_male = re.compile(r'[a-z]+')    # conajmniej 1 mala litera
# 	hasloRegex_liczby = re.compile(r'[\d]+')     # conajmniej 1 cyfra
# 	if hasloRegex_liczba.search(haslo) and hasloRegex_duze.search(haslo) and hasloRegex_male.search(haslo) and hasloRegex_liczby.search(haslo):
# 		print('MOCNE')
# 	else:
# 		print('SLABE')	
 
import re
 
 
def redundancydept(password):
    expressions = {
        'powyzej 8 znakow': r'.{8,}',
        'conajmniej 1 duza litera': '[A-Z]+',
        'conajmniej 1 mala litera': '[a-z]+',
        'conajmniej 1 cyfra': '\d+'
    }
    for name, expr in expressions.items():
        if not re.search(expr, password):
            return 'aj waj ({})'.format(name)
    return 'takie silne'