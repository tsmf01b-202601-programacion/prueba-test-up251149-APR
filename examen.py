problema = int(input("Número del problema (1-10): "))

if problema == 1:
    r = 15
    print(3.1416 * r**2)

elif problema == 2:
    codigo = 88
    lote = "LoteB"
    print(("prod-" + str(codigo) + "-" + lote).lower())

elif problema == 3:
    email = "usuario.upa.edu.mx"
    print("@" in email)

elif problema == 4:
    aviso = "el examen termina pronto"
    print(aviso.upper())

elif problema == 5:
    dato = "150.50"
    f = float(dato)
    print(f, int(f))

elif problema == 6:
    celsius = 30
    print((celsius * 1.8) + 32)

elif problema == 7:
    frase = "Programación en Python"
    print(frase[:5])

elif problema == 8:
    m = 500
    v = 2
    print(m / v)

elif problema == 9:
    numero = -15
    print(numero < 0)

elif problema == 10:
    m = 5
    h = 10
    g = 9.81
    print(m * g * h)

else:
    print("Ingresa un número entre 1 y 10.")