# =============================================================================
# Programa: Gestión de notas de alumnos
# Autor: RafaDAM123
# Fecha: 26/02/2026
# Descripción: Este programa calcula la media de tres notas por alumno,
#              determina su calificación y muestra un informe por pantalla.
# =============================================================================


def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    return (nota1 + nota2 + nota3) / 3


def obtener_calificacion(media):
    """
    Devuelve la calificación textual según la media obtenida.

    Args:
        media (float): La media aritmética del alumno.

    Returns:
        str: Calificación textual (Sobresaliente, Notable, Aprobado o Suspenso).
    """
    # Se usan elif para que solo se evalúe una condición
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"


def esta_aprobado(media):
    """
    Indica si el alumno ha aprobado o suspendido según su media.

    Args:
        media (float): La media aritmética del alumno.

    Returns:
        bool: True si aprobado, False si suspendido.
    """
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False


def mostrar_alumno(nombre, nota1, nota2, nota3):
    """
    Muestra por pantalla el informe completo de un alumno.

    Args:
        nombre (str): Nombre completo del alumno.
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.
    """
    # Calculamos la media y la calificación antes de mostrar
    media = calcular_media(nota1, nota2, nota3)
    calificacion = obtener_calificacion(media)

    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    print("Media: " + str(media))
    print(calificacion)
    print("----------------------")


def main():
    """
    Función principal que ejecuta el programa con los alumnos de ejemplo.
    """
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)

main()