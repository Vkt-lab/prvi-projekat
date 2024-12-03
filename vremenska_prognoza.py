temeperatura = int(input("Unesite temepraturu:"))
test_temeperatura = -1 
temeperatura = test_temeperatura
poruka = ""
if temeperatura < 0:
    poruka = "Oprez klizavo"

if temeperatura > 0 :
    poruka = "Temperatur iznad 0"
    if temeperatura > 30:
        poruka = "Ukljucite klima uredjaje"


ocekivana_poruka = "Oprez klizavo"
if poruka == ocekivana_poruka:
    print("Case-ispod nule - Test prosao")
