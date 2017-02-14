Summ = int(input('How many want to take the money: '))
Proc = float(input('By what percentage you take money: '))/100
Years = int(input('For how many years: '))

Month = (Summ * Proc * (1 + Proc) * Years) / (12 * ((1 + Proc) * Years - 1))
m = Years * 12
ALL = Month * m

print(Month,"$")
print(ALL, "$")
input("Press enter to continue..")