import mysql.connector

try:
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="nozomi.proxy.rlwy.net",
        port=10430,
        user="root",
        password="NWVmzRUKcrsPmwtVeAAEgiZNScYtYfaW",
        database="hotel_posada_riscal"
    )
    cursor = conn.cursor()

    # Consultar las reservaciones existentes con su pago correspondiente
    cursor.execute("""select * from Reservaciones""")

    resultados = cursor.fetchall()

    print("\n📋 Últimas reservaciones registradas:")
    for fila in resultados:
        print(f"\nID reservación: {fila[0]}")
        print(f"Costo total: {fila[1]}")
        print(f"Depósito: {fila[2]}")
        print(f"Monto restante: {fila[3]}")

except mysql.connector.Error as err:
    print("❌ Error al consultar datos:", err)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\n🔌 Conexión cerrada.")