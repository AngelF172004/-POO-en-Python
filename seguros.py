
def safe_calcular_pago(p: Pagable) -> float:
    try:
        return p.calcular_pago()
    except PagoInvalidoException as e:
        print(f"[Error Pago] {e}")
        return 0.0

def safe_calcular_promedio(c: Calificable) -> float:
    try:
        return c.calcular_promedio()
    except PromedioInvalidoException as e:
        print(f"[Error Promedio] {e}")
        return 0.0
