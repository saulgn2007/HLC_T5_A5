# Crea una clase Libro con atributos titulo y autor. Luego, crea una clase Biblioteca 
# que contenga una lista de libros y métodos para agregar libros y mostrarlos.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"Libro: {libro.titulo}, Autor: {libro.autor}")

libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
libro2 = Libro("El señor de los anillos", "J.R.R. Tolkien")
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca
biblioteca.mostrar_libros()
