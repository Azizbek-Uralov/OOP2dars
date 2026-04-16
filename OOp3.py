import random

class MenuItem:
    def __init__(self, nomi, turi):
        self.nomi = nomi
        self.turi = turi
        if self.turi == "ichimlik":
            self.miqdor = 20
        else:
            self.miqdor = 10

    def restock(self):
        if self.turi == "ichimlik":
            self.miqdor = 20
        else:
            self.miqdor = 10
        print(f"--- [OMBOR]: {self.nomi} zaxirasi to'ldirildi (Max: {self.miqdor} ta) ---")

    def serve(self):
        self.miqdor -= 1
        print(f"[XIZMAT]: Bitta {self.nomi} berildi. (Qoldi: {self.miqdor} ta)")
        if self.miqdor == 0:
            self.restock()

class Customer:
    def __init__(self, name, item):
        self.name = name
        self.item = item 
        self.__balance = 100 
        self.total_bought = 0 
        
        self.variants = {
            "kichik": 10,
            "o'rta": 20,
            "katta": 30,
            "": 0
        }

    def top_up(self):
        self.__balance += 50
        print(f"[HAMYON]: {self.name} balansni 50 ga to'ldirdi. Yangi balans: {self.__balance}")

    def buy(self):
        size = random.choice(list(self.variants.keys()))
        price = self.variants[size]

        if size == "":
            print(f"[REJA]: {self.name} {self.item.nomi} olmoqchi edi, lekin fikridan qaytdi.")
            return True

        if self.__balance >= price:
            self.__balance -= price
            self.item.serve()
            self.total_bought += 1
            print(f"[XARID]: {self.name} {size} {self.item.nomi} sotib oldi. Puli qoldi: {self.__balance}")
            return True
        else:
            print(f"[STOP]: {self.name}da {size} {self.item.nomi} uchun pul yetarli emas!")
            return False
kofe = MenuItem("Kofe", "ichimlik")
tort = MenuItem("Tort", "shirinlik")
mijozlar = [
    Customer("Ali", kofe),
    Customer("Vali", tort)
]

print("======= KAFE ISH BOSHLADI =======")

while True:
    xaridor = random.choice(mijozlar)

    natija = xaridor.buy()
    
    if not natija:
        print(f"\n>>> {xaridor.name}ning puli tugadi va kafedan chiqib ketdi.")
        break

print("\n======= NATIJALAR =======")
for m in mijozlar:
    print(f"{m.name} jami {m.total_bought} ta mahsulot sotib oldi.")

if mijozlar[0].total_bought > mijozlar[1].total_bought:
    print(f"G'olib: {mijozlar[0].name}!")
elif mijozlar[1].total_bought > mijozlar[0].total_bought:
    print(f"G'olib: {mijozlar[1].name}!")
else:
    print("Durang!")