##print("hello world")

##print("Mary's cosmetics")

##print('신씨가 소리질렀다. "도둑이야"')

##print('"C:\Windows"')

##print("안녕하세요. \n만나서\t\t반갑습니다.")##\n은 한줄 띄우기 \t는 지정갯수만큼 공백추가

##print("첫번째", '두번째')

##print("naver;kakao;sk;samsung")

##print("naver/kakao/sk/samsung")

##print("first",end="\n");print("second")##print의 end옵션 설정법

##print(5/3)##숫자를 그대로 문자열로 바꾸어 출력하는 python

##삼성전자 = 50000
##print(삼성전자*10)##한글변수를 써도 되는python

##시가총액=298
##현재가=50000
##PER=15.79
##print(시가총액, type(시가총액))
##print(현재가, type(현재가))
##print(PER, type(PER))

#s="hello"
#t="python"
#print(s+"! "+t+" merge variable")

##print(2+2*3)

##a = 128
##print(type("132"))

##num_str ="720"
##num_int = int(num_str)
##print(1,type(num_int))

##num =100
##string_num = str(num)
##print(string_num, type(string_num))

##string = "15.79"
##string_to_float = float(string)
##print(string_to_float, type(string_to_float))

##year = "2020"
##year_int = int(year)
##print(year_int,year_int-1,year_int-2)

##per_month=48584
##total = per_month*36
##print("총 금액은 : "+ str(total))

##letters = 'python'
##print("first: " + letters[0] + "  third: " + letters[2])

##license_plate = "24가 2210"
##print(license_plate[-4:])

##string = "홀짝홀짝홀짝"
##print(string[0],string[2],string[4])

#string = "PYTHON"
#sliced = string[::-1]
#print(sliced)

#phone_number = "010-1111-2222"
#replaced = phone_number.replace('-',' ')
#print(replaced)

#replaced2 = replaced.replace(' ','')
#print(replaced2)

##url = "http://sharebook.kr"
##splited = url.split('.') ##splited is list
##print(splited)

#lang = 'python'
#lang[0] = 'P'
#print(lang)

##string = 'abcdfe2a354a32a'
##string = string.replace('a','A')
##print(string)

##string = 'abcd'
##string.replace('b','B')##클래스 내의 함수를 쓴것일뿐 return값을 받는 이가 없다.
##print(string)

##a = '3'
##b = '4'
##print(a+b)

##print("Hi"*3)

##print('-'*80)

##t1 = 'python'
##t2 = 'java'
##print((t1+' '+t2+' ')*4)


#name1 = "김민수"
#age1 = 10
#name2 = "이철희"
#age2 = 13
#print(f"이름: {name1} 나이: {age1}")
#print(f"이름: {name2} 나이: {age2}")

#상장주식수 = "5,969,782,550"
#상장주식수 = 상장주식수.replace(",","")
#intstock = int(상장주식수)
#print(intstock, type(intstock))

#data = "    삼성전자     "
#data1 = data.strip()
#print(data1)

#ticker = "BTC_krw"
#ticker_low = ticker.upper()
#print(ticker_low)

#file_name = "list.xls"
#print(file_name.endswith(('xlsx','xls')))

#file_name = "2020_보고서.xlsx"
#print(file_name.startswith(('2020','10')))

#a = "hello world"
#print(a.split(" "), type(a.split(" ")))

#data = "     1234     "
#print(data.strip(),"end")

#movie_rank = ['닥터 스트레인지','스플릿','럭키']
#movie_rank.append("배트맨")
#movie_rank.insert(1, "슈퍼맨")
#del movie_rank[3]
#del movie_rank[3]
#print(movie_rank)

#willdel = 4
#del willdel
#print(willdel)

#lang1 = ["C","C++","JAVA"]
#lang2 = ["Python","Go","C#"]
#langs = lang1 + lang2
#print(langs)

#nums = [1,2,3,4,5,6,7]
#print("max: "+str(max(nums)))
#print("min: "+str(min(nums)))

#nums =[1,2,3,4,5]
#print(sum(nums))

#cook = ["피자", "김밥", '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', '쏘세지', '라면', '팥빙수', '김치전', ]
#print(len(cook))

#nums = [1,2,3,4,5]
#nums_mean = sum(nums)/len(nums)
#print(nums_mean)

#price = ['20180728', 100, 130, 140, 150, 160, 170]
#print(price[1:])

#nums = [1,2,3,4,5,6,7,8,9,10]
#odd_nums = nums[::2]
#print(odd_nums)

#nums = [1,2,3,4,5,6,7,8,9,10]
#even_nums = nums[1::2]
#print(even_nums)

#nums = [1,2,3,4,5]
#nums_reverse = nums[::-1]
#print(nums_reverse)

#interest = ["삼전", "LG전자", "Naver"]
#print(interest[::2])

#interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#print("\n".join(interest))

#string = "삼성전자/LG전자/Naver"
#interest = string.split("/")
#print(interest, type(interest))

#data = [2,4,3,1,5,10,9]
#sorted_data = sorted(data)
#print(sorted_data)

#my_variable = ()
#print(my_variable, type(my_variable))

#movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
#print(movie_rank)

#only_one = (1,)
#print(only_one, type(only_one))

#t = (1,2,3) #tuple은 원소(element)의 값을 변경할 수 없습니다.
#t[0]='a'

#t = 1,2,3,4
#print(t)

#interest = ['삼성전자','LG전자', 'SK Hynix']
#interest_tuple = tuple(interest)
#print(interest_tuple, type(interest_tuple))

#temp = ('apple','banana','cake')
#a,b,c = temp
#print(a,b,c)

#list= range(2,100,2)
#tuple_even = tuple(list)
#print(tuple_even)

#scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#*valid_score, _, _ = scores
#print(valid_score)

#scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#_,*essen,_ = scores
#print(essen, type(essen))

#temp = {}
#print(type(temp))

#temp = {'메로나': 1000, '폴라포':1200, '빵빠레':1800}
#print(temp, type(temp))

#ice = {'메로나' : 1000, '폴로포' : 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
#print("메로나 가격:",ice['메로나'])

#ice = {'메로나' : 1000, '폴로포' : 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
#ice['메로나']= 1300#리스트 요소 바꾸듯 딕셔너리 다루자
#print('메로나 가격:',ice['메로나'])

#inventory = {'메로나': [300,20], '비비빅' : [400,3], '죠스바': [250, 100]} 
#inventory['월드콘'] =[500, 7]
#icecream_name = list(inventory.values())
#print(icecream_name, type(icecream_name))

#icecream = {'탱크보이' : 1200, '폴라포' : 1200, '빵빠레' : 1800, '월드콘' : 1500, '메로나' : 1000}
#total_value = sum(icecream.values())
#print(total_value)

#icecream = {'탱크보이' : 1200, '폴라포' : 1200, '빵빠레' : 1800, '월드콘' : 1500, '메로나': 1000}
#new_product = {'팥빙수' : 2700, '아맛나' :1000}
#icecream.update(new_product)
#print(icecream)

keys = ('apple', 'pear', 'peach')
vals = (300,250, 400)