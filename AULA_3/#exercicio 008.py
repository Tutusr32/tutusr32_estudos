#crie um conversor de medidas de M para Km, Hm, Cm e MM

n1 = float(input('Digite uma distância em metros:'))

print(f'''
 M:{n1}m
 Km:{n1 / 1000}km
 Hm:{n1 / 100}hm
 Cm:{n1 * 100}cm
 Mm:{n1 * 1000}mm
''')
