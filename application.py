from usuario import Usuario

usuario_pedro = Usuario(nombre="Pedro")
usuario_juan = Usuario(nombre="Juan")
usuario_diego = Usuario(nombre="Diego")

usuario_pedro.agregar_tarjeta(nombre_tarjeta="VISA", limite_credito=2000000, intereses=0.02)
usuario_pedro.agregar_tarjeta(nombre_tarjeta="Fallabella", limite_credito=1500000, intereses=0.025)

usuario_juan.agregar_tarjeta(nombre_tarjeta="Lider", limite_credito=1500000, intereses=0.03)
usuario_juan.agregar_tarjeta(nombre_tarjeta="Banco Chile", limite_credito=150000, intereses=0.02)

usuario_diego.agregar_tarjeta(nombre_tarjeta="Banco Estado", limite_credito=1200000, intereses=0.015)
usuario_diego.agregar_tarjeta(nombre_tarjeta="Din", limite_credito=500000, intereses=0.035)

#realizar compras y pagos
usuario_pedro.hacer_compra(300000, "VISA").hacer_compra(200000, "Fallabella")
usuario_pedro.pagar_tarjeta(100000, "VISA")

usuario_juan.hacer_compra(600000, "Lider").hacer_compra(100000, "Banco Chile")
usuario_juan.pagar_tarjeta(200000, "Lider")

usuario_diego.hacer_compra(400000, "Banco Estado").hacer_compra(150000, "Din")
usuario_diego.pagar_tarjeta(100000, "Banco Estado")


print("Información de las tarjetas de Pedro:")
usuario_pedro.mostrar_saldo_usuario()

print("Información de las tarjetas de Juan:")
usuario_juan.mostrar_saldo_usuario()

print("Información de las tarjetas de Diego:")
usuario_diego.mostrar_saldo_usuario()