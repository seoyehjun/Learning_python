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

data = "     1234     "
print(data.strip(),"end")

