#211
def put_you_print(인삿말):
    print(인삿말)
#put_you_print('put some dirt')

#212
def 곱셈(a,b):
   print(a*b)
#곱셈(20,4)

#215
def print_with_smile(str):
    print(str + ':D')
#print_with_smile('super happy')

#217
def print_30(price):
    print(price*30/100+price)
#print_30(100)

#218
def sum(a,b):
    print(a+b)
#sum(10,42) 

#219
def print_arithmetic_operation(a, b):
    print('{a} + {b} = {c}'.format(a=a, b=b, c=a+b))
    print('{a} - {b} = {c}'.format(a=a, b=b, c=a-b))
    print('{a} * {b} = {c}'.format(a=a, b=b, c=a*b))
    print('{a} / {b} = {c}'.format(a=a, b=b, c=a/b))
#print_arithmetic_operation(1,2)

def compare_best(a,b,c,d,e,f,g):
    user = list((a,b,c,d,e,f,g))

    supreme_value=user[0]
    for var in range(len(user)-1):
        if user[var+1]>supreme_value:
            supreme_value=user[var+1]
    print(supreme_value)

#compare_best(67,66,40,32,1,49,67)