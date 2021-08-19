import random

class Account:
    deposit_count =0 
    
    
    def __init__(self, bank, account_holder, balance ):
        self.bank = bank
        self.account_holder = account_holder
        self.account_num = self.make_random_account_num()
        self.balance = balance 
        self.log_inout =[]

    def print_information(self):
        print(f'bank: {self.bank}\naccount_holder: {self.account_holder}\naccount_num: {self.account_num}\nbalance: {self.balance}')
    
    def deposit(self, money):
        Account.deposit_count +=1
        if Account.deposit_count%5 ==0:
            self.balance = self.balance*1.01
        self.balance += money 
        self.log_inout.append(f'입금된 돈은:{money}')
        print('잔액:', self.balance)  
    
    def withdraw(self, want):
        if want> self.balance:
            print("잔액이 부족합니다(balance 값 유지)")
            
            return
        self.balance -= want
        self.log_inout.append(f'출금된 돈은:{want}')
        print('잔액:', self.balance)

    def make_random_account_num(self):
        account_num = ''
        for var in range(11):
            account_num = account_num + str(int(random.random()*10))
        return account_num




   
#계좌 개설, 계좌 정보 출력
account1 = Account('SC', '진수', 10000)
account2 = Account('SC', '수진', 1000000)
account3 = Account('SC', '허수', 12000000)
account4 = Account('SC', '닌수', 100000000)
account5 = Account('SC', '진국', 10000)

account_list = [account1,account2,account3,account4,account5]

for var in range(len(account_list)):
    if account_list[var].balance >= 1000000:
        account_list[var].print_information()
    print()
account_list[0].deposit(1000)
account_list[0].deposit(10)
account_list[0].withdraw(33)
account_list[4].withdraw(10000)
account_list[4].withdraw(12)
print(account_list[0].log_inout)
print(account_list[4].log_inout)