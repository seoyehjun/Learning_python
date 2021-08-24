class 차:
    count =0
    def __init__(self, tire, value=1000):
        self.value = value
        self.tire = tire

    def print_information(self):
        print('바퀴수:', self.tire)
        print('가격:', self.value)

    def print_what1(self):
        print('차')

class 자전차(차):
    def __init__(self,기어, tire_num,value=200):
        super().__init__(tire_num,value)#이건 호출이라서 매개변수 기본설정 안됨 
        count =1
        self.tire_num = tire_num
        self.기어 = 기어
    def print_what2(self):
        print('오버라이드된 메서드')
        print('자전차')
        
    
        

car1 = 자전차('시마노',4)
car1.print_information()


