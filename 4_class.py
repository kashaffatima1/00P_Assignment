# 4. Class Variables and Class Methods

class Bank:
    bank_name = "KF Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
print(b1.bank_name)
Bank.change_bank_name("ABC Bank") 
print(b1.bank_name)  
