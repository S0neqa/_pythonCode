frase = input('digite sua frase: ').lower().strip()

ContA = frase.count('a')
Pos = frase.find('a')

ulti = frase.rfind('a')

print(f"""A frase possui {ContA} letras "a";
    a primeira posição em que aparece é {Pos+1};
    e a última é {ulti+1}.""")