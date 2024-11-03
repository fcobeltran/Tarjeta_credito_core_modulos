from dataclasses import dataclass

@dataclass
class TarjetaCredito:
    nombre: str
    limite_credito: float
    intereses: float
    saldo_pagar: float = 0.0
    limite_disponible: float = 0.0  

    def __post_init__(self):
        self.limite_disponible = self.limite_credito

    def compra(self, monto: float) -> "TarjetaCredito":
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            self.limite_disponible -= monto  # Reducimos el límite disponible
        else:
            print(f"{self.nombre}: Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto: float) -> "TarjetaCredito":
        if monto > self.saldo_pagar:
            print(f"{self.nombre}: El pago excede el saldo pendiente. Pagando solo ${self.saldo_pagar:.2f}.")
            monto = self.saldo_pagar  # Solo pagar el saldo pendiente

        
        self.saldo_pagar -= monto
        nuevo_limite_disponible = self.limite_disponible + monto

        # que el limite no exceda el total de crédito
        if nuevo_limite_disponible > self.limite_credito:
            print(f"{self.nombre}: El pago excede el límite de crédito. Límite disponible ajustado al máximo.")
            self.limite_disponible = self.limite_credito
        else:
            self.limite_disponible = nuevo_limite_disponible

        return self

    def mostrar_info_tarjeta(self) -> None:
        print(f"Tipo de tarjeta: {self.nombre}")
        print(f"Interés: {self.intereses}")
        print(f"Límite de crédito total: ${self.limite_credito:.2f}")
        print(f"Límite disponible: ${self.limite_disponible:.2f}")  
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}\n")

    def cobrar_interes(self) -> "TarjetaCredito":
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self