


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):
        print('end role')


    def who(self):
        print("이름:{}, 나이:{}, 성별:{}".format(self.name, self.age, self.sex))
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
  


areum = Human('범수', 21, '남')
areum.who()
areum.setInfo('벙수아님',22,'여')
Human.who(areum)
del areum