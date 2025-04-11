OSPF = 110
RIP =120
EIGRP = 90
BGP = 20

Protocolo = input("Dime el nombre del protocolo (OSPF, RIP, EIGRP, BGP): ")

if Protocolo == "OSPF":
    print(f"La distancia administrativa de {Protocolo} es {OSPF}.")
elif Protocolo == "RIP":
    print(f"La distancia administrativa de {Protocolo} es {RIP}.")
elif Protocolo == "EIGRP":
    print(f"La distancia administrativa de {Protocolo} es {EIGRP}.")
elif Protocolo == "BGP":
    print(f"La distancia administrativa de {Protocolo} es {BGP}.")
else:
    print("No reconozco esa respuesta. Por favor ingresa uno como: (OSPF, RIP, EIGRP, BGP).")

