from typing import List, Optional, TYPE_CHECKING
from tarjeta_credito import TarjetaCredito 


if TYPE_CHECKING:
    from httmlcsscurso.PYTHON.TarjetaCredito_Core.TarjetaCredito.tarjeta_credito import TarjetaCredito

class Usuario:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.tarjetas: List["TarjetaCredito"] = [] 

    def agregar_tarjeta(self, nombre_tarjeta: str, limite_credito: float, intereses: float) -> "Usuario":
        tarjeta = TarjetaCredito(nombre=nombre_tarjeta, limite_credito=limite_credito, intereses=intereses)
        self.tarjetas.append(tarjeta)
        return self

    def hacer_compra(self, monto: float, nombre_tarjeta: str) -> "Usuario":
        tarjeta = self.obtener_tarjeta(nombre_tarjeta)
        if tarjeta:
            tarjeta.compra(monto)
        else:
            print(f"No se encontró la tarjeta {nombre_tarjeta}")
        return self

    def pagar_tarjeta(self, monto: float, nombre_tarjeta: str) -> "Usuario":
        tarjeta = self.obtener_tarjeta(nombre_tarjeta)
        if tarjeta:
            tarjeta.pago(monto)
        else:
            print(f"No se encontró la tarjeta {nombre_tarjeta}")
        return self

    def mostrar_saldo_usuario(self) -> None:
        print(f"Usuario: {self.nombre}")
        for tarjeta in self.tarjetas:
            tarjeta.mostrar_info_tarjeta()

    def obtener_tarjeta(self, nombre_tarjeta: str) -> Optional["TarjetaCredito"]:
        for tarjeta in self.tarjetas:
            if tarjeta.nombre == nombre_tarjeta:
                return tarjeta
        return None