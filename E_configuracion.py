'''
Este archivo contiene metodos y variables de configuracion .
This file contains methods and configuration variables.


'''






class configuracion(object):

    '''
    en este medtodo se debe armarn el string de coccion tipo de base, usuario, 
    clave , nombre db y puerto de comunicacion del servicio de la db

    In this method, the cooking string of the base type, 
    user, password, db name and communication port of the db service must be set
    '''
    def config(self):
        cadena = 'postgresql://postgres:slam2016@localhost:5432/bikeRental'

        return cadena

    # lugar donde se descargan archivos local
    def ruta(self):
        cadena = "/home/soporte/Documentos/facultad/sgc/sgc20190401"
        return cadena

    # lugar de donde se obtienen los archivos del servidor
    def ruta_server(self):
        # cadena ="/home/soporte/Documentos/facultad/credired20180108"
        cadena = "/home/soporte/Documentos/facultad/sgc/"

        return cadena

    def host_server(self):
        cadena = 'localhost'
        return cadena

    def usu_server(self):
        cadena = 'user'
        return cadena

    def pass_server(self):
        cadena = 'slam2016'
        return cadena
