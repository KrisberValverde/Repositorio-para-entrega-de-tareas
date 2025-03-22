#Cálculo de descuento en compras

def calcular_descuento(monto_total, porcentaje_de_descuento=10):
    Descuento= monto_total * (porcentaje_de_descuento/100)
    return Descuento

#Monto de la compra de ropa y zapatos
Compra_de_ropa = 240
Compra_de_zapatos = 90

#Cálculo del descuento de la compra de ropa
Primer_descuento = calcular_descuento(Compra_de_ropa)
Monto_final_primer_descuento= Compra_de_ropa - Primer_descuento
print(f"El monto de la compra de ropa es de: ${Compra_de_ropa:.2f} ; Su descuento es de: ${Primer_descuento:.2f} ; Y el monto a pagar es: ${Monto_final_primer_descuento:.2f}")

#Cálculo del descuento de la compra de zapatos
Segundo_descuento = calcular_descuento(Compra_de_zapatos)
Monto_final_segundo_descuento = Compra_de_zapatos - Segundo_descuento
print(f"El monto de la compra de zapatos es de: ${Compra_de_zapatos:.2f} ; Su descuento es de: ${Segundo_descuento:.2f} ; Y el monto a pagar es: ${Monto_final_segundo_descuento:.2f}")

#Cálculo del descuento de las dos compras
Monto_total = Compra_de_ropa + Compra_de_zapatos
Descuento_general = calcular_descuento(Monto_total)
Monto_final_descuento_general = Monto_total - Descuento_general
print(f"El monto total de la compra de ropa y zapatos es de: ${Monto_total:.2f} ; Sl descuento es de: ${Descuento_general:.2f} ; Y el monto final a pagar es de: ${Monto_final_descuento_general:.2f}")