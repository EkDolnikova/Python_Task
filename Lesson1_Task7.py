# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за
# проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# a = int(input("Введите номер билета из 6 цифр:"))
a = [int(i) for i in input("Введите номер билета из 6 цифр:")]
if sum(a[:3]) == sum(a[3:]):
    print("Счастливый:) ")
else:
    print("Несчастливый:( ")