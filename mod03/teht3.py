sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ")
hb = int(input("Anna hemoglobiiniarvosi (g/l): "))
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvosi on alhainen..")
    elif hb <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvosi on alhainen..")
    elif hb <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli.")