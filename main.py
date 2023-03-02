import random
from VirtualUser import VirtualUser

# vypis nahodnyho uzivatele (muze i zeny)
user = VirtualUser(sex = random.randint(0, 1), minage=18, maxage=80)
VirtualName = user.DataPrint()
print(f"Random virtual user: {VirtualName}")