from Mundo.Contacto import Contacto

class ListaDeContactos:
    def _init_(self):
        self.__contactos = []

    def darTodosLosContactos(self):
        lista = []
        for contacto in self.__contactos:
            lista.append(contacto.darNombre() + " " + contacto.darApellido())
        return lista

    def buscarContactosPalabraClave(self, palabra):
        nombres = []
        for contacto in self.__contactos:
            if contacto.contienePalabraClave(palabra):
                nombres.append(contacto.darNombre() + " " + contacto.darApellido())
        return nombres

    def buscarContacto(self, nombre, apellido):
        for contacto in self.__contactos:
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
            self.__contactos.append(nuevo)
            return True
        return False
    
    def eliminarContacto(self, nombre, apellido):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            self.__contactos.remove(contacto)
            return True
        return False

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            contacto.cambiarDireccion(direccion)
            contacto.cambiarCorreo(correo)
            self.actualizarTelefonos(telefonos, contacto)
            self.actualizarPalabras(palabras, contacto)
            return True
        return False
        
    def actualizarTelefonos(self, telefonos, contacto):
        lista_vieja = contacto.darTelefonos()
        eliminar = [tel for tel in lista_vieja if tel not in telefonos]
        for tel in eliminar:
            contacto.eliminarTelefono(tel)
        for tel in telefonos:
            contacto.agregarTelefono(tel)
    
    def actualizarPalabras(self, palabras, contacto):
        lista_vieja = contacto.darPalabras()
        eliminar = [pal for pal in lista_vieja if pal not in palabras]
        for pal in eliminar:
            contacto.eliminarPalabra(pal)
        for pal in palabras:
            contacto.agregarPalabra(pal)