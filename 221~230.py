#221
def print_reverse(str):
    print(str[::-1])
#print_reverse('python')

#222
def print_score(List):
    print(sum(List))
    print(sum(List)/len(List))
#print_score([4,5,9])

##223
def print_even(List):
    for var in range(len(List)):
        if List[var]%2 ==0:
            print(List[var])
#print_even([1,3,2,10,12,11,15,22,30,31])

#224
def print_keys(my_dic):
    print(my_dic.keys())
#print_keys({'이름': '권기한', '나이':'40', '성별': 0})

#225
def put_key(key):
    my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
    print(my_dict[key])
#put_key("10/26")

#227
def print_5xn(str,str_len):
    index =0
    print(len(str)/str_len)
    
    #문자열의 길이가 원하는 길이와 나누어떨어질시 생기는 의미없는 반복 제거
    count=0
    if len(str)%str_len == 0:
        count = 1
    
    for var in range(int(len(str)/str_len)+1-count):
        index = index + str_len
        print(str[index-str_len:index])
        
    print(f'count: {count}')
#print_5xn("1234567890",5)  

#228
def calc_monthly_salary(annual_income):
    return annual_income-annual_income%10
#print(calc_monthly_salary(2203211))





        