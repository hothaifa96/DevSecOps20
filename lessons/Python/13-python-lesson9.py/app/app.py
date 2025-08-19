from config.config import *
from eran_bank import *

# print(password)
#
# print(get_date())

acc1 = CheckingAccount('roman', 1233, [], 15000)
acc1.__balance = 120_000
acc1.set_balance(120000)
print(acc1.get_balance())