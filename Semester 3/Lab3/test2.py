import random
from prettytable import PrettyTable




class tochka:
    def __init__(self, b1, b2, ch1,ch2):
        self.b1 = b1
        self.b2 = b2
        self.ch1 = ch1
        self.ch2 = ch2




def binary_to_gray(n):
    binary = int(n, 2)
    binary ^= (binary >> 1)
    return bin(binary)[2:]


def BinToGray(n):
   n = int(n, 2)
   n ^= (n >> 1)
   return bin(n)[2:]


m = 32
numtochek=int(input("Введите количество точек"))

table_1 = PrettyTable()
table_1.field_names = ["Номер", "БКГх1", "БКГх2","l1","l2"]

list=[]

for i in range(1, numtochek + 1):
    bkg1 = bin(random.randint(0, 2 ** m - 1))[2:].zfill(
        m)
    bkg2 = bin(random.randint(0, 2 ** m - 1))[2:].zfill(m)
    bkg1 = binary_to_gray(bkg1)
    bkg2 = binary_to_gray(bkg2)
    l1 = BinToGray(bkg1)
    l2 = BinToGray(bkg2)





    list.append(tochka(bkg1, bkg2,l1,l2))
    table_1.add_row([i, bkg1, bkg2, l1, l2])

print(table_1)