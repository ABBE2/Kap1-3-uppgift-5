L = input("hur manga liter har du tankat?")
P = input("hur mycket kostar bensinen per liter?")

L1 = float(L)
P1 = float(P)


print("--------------------------")
print("|          KVITTO        |") 
print("|Tankad volym", L1, "liter", " |")
print("|pris per liter", P1, "kr", " |")
print("|Betalt kronor", (P1*L1), "     |")
print("|                        |")
print("|   Tack for besoket och |")
print("|       Valkommen ater!  |")
print("--------------------------")