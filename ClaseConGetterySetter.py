class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None #es privada, no se puede acceder
        
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor # con Setter puedo cambiar la privada, al permitir meter valores
        
    def getPropiedadPrivada(self):# Getter devuelve lo que hay dentro, al ser solo de lectura
        return self.__propiedad_privada
    
    def propiedadPrivada(self, valor=None):# los mismo que set y get pero en uno
        if valor==None:
            #actua como getter
            return self.__propiedad_privada
        else:
            #actua como setter
            self.__propiedad_privada = valor
            
        
    def __str__(self):
        return 'ClaseConGetterySetter con propiedadPrivada -> {}'.format(self.__propiedad_privada)
    
if __name__ == '__main__':
    c = ClaseConGetterySetter()

c.getPropiedadPrivada()
print(c)
c.setPropiedadPrivada('Un zorro con 7 colas')
print(c)
c.getPropiedadPrivada()
print(c)
c.propiedadPrivada('Brandon es color canela')
print(c)
c.getPropiedadPrivada()
print(c)


