class Stock:
    def __init__(self, company, code, PER, PBR, income):
        self.company = company
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.income = income

    def set_name(self, company):
        self.company = company
    def set_code(self, code):
        self.code = code
    def set_PER(self, PER):
        self.PER = PER
    def set_PBR(self, PBR):
        self.PBR = PBR
    def print_name(self):
        print("회사명:",self.company)
        print("코드명:",self.code)
    

samsung_stock = Stock('samsung', '005930', 15.79, 1.33, 2.83)
hyundai_stock = Stock('hyundai', '005380', 8.70, 0.35, 4.27)
LG_stock = Stock('LG', '066570', 317.34, 0.69, 1.37)

portpolio = [samsung_stock, hyundai_stock, LG_stock]
for var in range(len(portpolio)):
    print('company:',portpolio[var].company)
    print('code:',portpolio[var].code)
    print('PER:',portpolio[var].PER)
    print()