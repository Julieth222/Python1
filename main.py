import os
import datetime
import pickle

class Nota:
    def __init__(self, titulo, descripcion, categoria="general"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.categoria = categoria
        self.fecha_creacion = datetime.datetime.now()

    def __str__(self):
        return (f"Título: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Categoría: {self.categoria}\n"
                f"Fecha de creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")

class GestorNotas:
    archivo_datos = "notas_guardadas.pkl"

    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def guardar_notas(notas):
        with open(GestorNotas.archivo_datos, "wb") as f:
            pickle.dump(notas, f)

    @staticmethod
    def cargar_notas():
        try:
            with open(GestorNotas.archivo_datos, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def agregar_nota(notas):
        GestorNotas.limpiar_pantalla()
        print("=== Agregar Nueva Nota ===")
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        categoria = input("Categoría (personal, trabajo, estudio, etc): ")
        nota = Nota(titulo, descripcion, categoria)
        notas.append(nota)
        GestorNotas.guardar_notas(notas)
        print("Nota guardada con éxito.")
        input("Presione Enter para continuar...")

    @staticmethod
    def mostrar_notas(notas):
        GestorNotas.limpiar_pantalla()
        print("=== Notas Guardadas ===")
        if not notas:
            print("No hay notas.")
        else:
            for nota in notas:
                print(nota)
                print("-" * 30)
        input("Presione Enter para continuar...")

    @staticmethod
    def buscar_nota(notas):
        GestorNotas.limpiar_pantalla()
        palabra_clave = input("Buscar por palabra clave o categoría: ").lower()
        encontradas = [n for n in notas if palabra_clave in n.titulo.lower() or
                       palabra_clave in n.descripcion.lower() or
                       palabra_clave in n.categoria.lower()]
        if encontradas:
            for nota in encontradas:
                print(nota)
                print("-" * 30)
        else:
            print("No se encontraron notas.")
        input("Presione Enter para continuar...")

    @staticmethod
    def eliminar_nota(notas):
        GestorNotas.limpiar_pantalla()
        titulo = input("Título exacto de la nota a eliminar: ")
        for nota in notas:
            if nota.titulo == titulo:
                notas.remove(nota)
                GestorNotas.guardar_notas(notas)
                print("Nota eliminada.")
                break
        else:
            print("Nota no encontrada.")
        input("Presione Enter para continuar...")

    @staticmethod
    def editar_nota(notas):
        GestorNotas.limpiar_pantalla()
        titulo = input("Título de la nota a editar: ")
        for nota in notas:
            if nota.titulo == titulo:
                nota.descripcion = input("Nueva descripción: ")
                nota.categoria = input("Nueva categoría: ")
                nota.fecha_creacion = datetime.datetime.now()
                GestorNotas.guardar_notas(notas)
                print("Nota actualizada.")
                break
        else:
            print("Nota no encontrada.")
        input("Presione Enter para continuar...")

    @staticmethod
    def menu():
        notas = GestorNotas.cargar_notas()
        while True:
            GestorNotas.limpiar_pantalla()
            print("\n=== Diario Personal ===")
            print("1. Agregar Nota")
            print("2. Mostrar todas las Notas")
            print("3. Buscar Nota")
            print("4. Editar Nota")
            print("5. Eliminar Nota")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                GestorNotas.agregar_nota(notas)
            elif opcion == "2":
                GestorNotas.mostrar_notas(notas)
            elif opcion == "3":
                GestorNotas.buscar_nota(notas)
            elif opcion == "4":
                GestorNotas.editar_nota(notas)
            elif opcion == "5":
                GestorNotas.eliminar_nota(notas)
            elif opcion == "6":
                print("Hasta pronto :)")
                break
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")

# Ejecutar
GestorNotas.menu()
