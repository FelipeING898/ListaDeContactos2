from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.__ListaDeContactos = []

    def darTodosLosContactos(self):
        todosContactos = []
        for contacto in self.__ListaDeContactos:
            todosContactos.append(contacto.darNombre() + " " + contacto.darApellido())
        return todosContactos

    def buscarContactosPalabraClave(self, palabra):
        pClave = []
        for contacto in self.__ListaDeContactos:
            if contacto.contienePalabraClave(palabra):
                pClave.append(contacto.darNombre() + " " + contacto.darApellido())
        return pClave

    def buscarContacto(self, nombre, apellido):
        for contacto in self.__ListaDeContactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido) is None:
            palabras.append(nombre)
            palabras.append(apellido)
            nuevo = Contacto(nombre, apellido, direccion, correo)
            for telefono in telefonos:
                nuevo.agregarTelefono(telefono)
            for palabra in palabras:
                nuevo.agregarPalabra(palabra)
            self.__ListaDeContactos.append(nuevo)
            return True
        return False
    
    def eliminarContacto(self, nombre, apellido):
        buscado = self.buscarContacto(nombre, apellido)
        if buscado:
            self.__ListaDeContactos.remove(buscado)
            return True
        return False

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        buscado = self.buscarContacto(nombre, apellido)
        if buscado:
            buscado.cambiarDireccion(direccion)
            buscado.cambiarCorreo(correo)
            self.actualizarTelefonos(telefonos, buscado)
            self.actualizarPalabras(palabras, buscado)
            return True
        return False
        
    def actualizarTelefonos(self, telefonos, contacto): 
        telefonos = contacto.darTelefonos()
        eliminar = [tel for tel in telefonos if tel not in telefonos]
        for tel in eliminar:
            contacto.eliminarTelefono(tel)
        for tel in telefonos:
            contacto.agregarTelefono(tel)
    
    def actualizarPalabras(self, palabras, contacto):
        palabras = contacto.darPalabras()
        eliminar = [pal for pal in palabras if pal not in palabras]
        for pal in eliminar:
            contacto.eliminarPalabra(pal)
        for pal in palabras:
            contacto.agregarPalabra(pal)