import random 
valorCompra=int(input("se ingrasa el valor de la compra: "))
balota= random.choice(["roja", "verde", "azul", "amarrilla", "negra"])
descuento=0
if valorCompra>=50000 and balota=="roja":
    descuento=0.10
    print("balota elegida es roja")
    print("El descuento es de",valorCompra*descuento)
    print("El valor a pagar es: ",valorCompra-(valorCompra*descuento))
elif valorCompra>=50000 and balota=="verde":
    descuento=0.15
    print("balota elegida es verde")
    print("El descuento es de",valorCompra*descuento)
    print("El valor a pagar es: ",valorCompra-(valorCompra*descuento))
elif valorCompra>=50000 and balota=="azul":
    descuento=0.20
    print("balota elegida es azul")
    print("El descuento es de",valorCompra*descuento)
    print("El valor a pagar es: ",valorCompra-(valorCompra*descuento))
elif valorCompra>=50000 and balota=="amarilla":
    descuento=0.50
    print("balota elegida es amarilla")
    print("El descuento es de",valorCompra*descuento)
    print("El valor a pagar es: ",valorCompra-(valorCompra*descuento))
elif valorCompra>=50000 and balota=="negra":
    descuento=100
    print("balota elegida es negra")
    print("El descuento es de",valorCompra*descuento)
    print("El valor a pagar es: ",valorCompra-(valorCompra*descuento))
elif valorCompra<=50000:
    print("no participas")
    print("El valor a pagar es: ",valorCompra-(valorCompra*descuento))
