WITH_ADDITIONAL_VARIABLE = 0
WITHOUT_ADDITIONAL_VARIABLE = 1

foo = input("Введите первое число:")
bar = input("Введите второе число:")
variant = int(input("0 - с доп переменной; 1 - без доп переменной: "))
if(variant == WITH_ADDITIONAL_VARIABLE): 
    temp = foo; foo = bar; bar = temp
    print("foo: {0}, bar: {1}".format(foo, bar))
elif(variant == WITHOUT_ADDITIONAL_VARIABLE):
    foo, bar = bar, foo
    print("foo: {0}, bar: {1}".format(foo, bar))
else:
    pass
