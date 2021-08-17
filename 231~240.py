#231
def n_pluse_1 (n):
    result = n+1
#print(result)

#232
def make_url(str):
    return 'www.'+"str"+'.com'
#print(make_url('naver'))

#233
def make_list(str):
    return list(str)
#print(make_list('abcd'),type(make_list('abcd')))

#234
def pickup_even(lis):
    result = []
    for var in range(len(lis)):
        if lis[var]%2 ==0:
            result.append(lis[var])
    return result
#print(pickup_even([3,4,5,6,7,8,9,10]))

#235
def convert_int(str):
    return str.replace(',','')
print(convert_int('1,234,567'))

#236부터는 맞추기 문제
 