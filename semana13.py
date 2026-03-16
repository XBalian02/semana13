# ============================================
# PROGRAMA: CALCULAR TOTAL DE COMPRA
# ============================================

def calcular_total(precio, cantidad):
    """
    Método que calcula el total de una compra
    Parámetros:
        precio: float - precio unitario del producto
        cantidad: int - cantidad de productos
    Retorna:
        float - total de la compra (precio * cantidad)
    """
    total = precio * cantidad
    return total


def main():
    """
    Función principal del programa
    """
    # Datos de ejemplo
    precio_producto = 10.50
    cantidad_producto = 3
    
    # Llamar al método
    resultado = calcular_total(precio_producto, cantidad_producto)
    
    # Mostrar resultado en consola
    print("=" * 40)
    print("CALCULADORA DE TOTAL DE COMPRA")
    print("=" * 40)
    print(f"Precio del producto: ${precio_producto}")
    print(f"Cantidad: {cantidad_producto}")
    print("-" * 40)
    print(f"TOTAL A PAGAR: ${resultado}")
    print("=" * 40)


# Punto de entrada del programa
if __name__ == "__main__":
    main()