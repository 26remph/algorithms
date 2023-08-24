from typing import List


class ATM:

    def __init__(self):
        self.store = [0, 0, 0, 0, 0]
        self.nominal = {
            0: 20,
            1: 50,
            2: 100,
            3: 200,
            4: 500
        }

    def deposit(self, banknotesCount: List[int]) -> None:

        for i in range(len(banknotesCount)):
            self.store[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:

        ind = len(self.store) - 1
        out = [0, 0, 0, 0, 0]

        while amount and ind >= 0:

            if not self.store[ind]:
                ind -= 1
                continue

            nominal = self.nominal[ind]
            col = min(amount // nominal, self.store[ind])
            out[ind] = col
            amount = amount - nominal * col
            ind -= 1

        if amount > 0:
            return [-1]

        for i in range(len(out)):
            if out[i] > self.store[i]:
                return [-1]

        for i in range(len(out)):
            self.store[i] -= out[i]

        return out


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)

atm = ATM()
atm.deposit([250796,638723,691758,845522,938973])
atm.deposit([215317,848628,182949,784609,30472])
print('store', atm.store)
print('out', atm.withdraw(701035245))
print('out', atm.withdraw(109992310))
print('out', atm.withdraw(755819795))
print('out', atm.withdraw(722349970))
atm.deposit([678816,841145,503892,325349,204606])
atm.deposit([604328,586349,680353,733891,136713])
atm.deposit([500950,53467,775875,469508,668335])
atm.deposit([178876,500427,867418,738121,80412])
print('out', atm.withdraw(824714410))
print('out', atm.withdraw(374969115))
print('out', atm.withdraw(351532175))
print('out', atm.withdraw(732076765))
atm.deposit([208564,707512,566329,300547,313109])
print('out', atm.withdraw(774911195))
atm.deposit([742897,902293,512670,863273,105945])
print('out', atm.withdraw(449705540))
atm.deposit([94829,872976,822744,630565,726268])
print('store', atm.store)
print('out', atm.withdraw(981495000))




