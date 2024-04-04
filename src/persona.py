class Persona:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def formato_doc(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono
        }