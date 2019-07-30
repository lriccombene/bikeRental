class configuracion(object):
    def config(self):
        cadena = 'postgresql://postgres:slam2016@localhost:5432/bikeRental'
        # cadena = 'postgresql://vsoftcoo_slam2016:Slamcoop2016@postgres.cicuxlbsejat.us-east-2.rds.amazonaws.com:5432/sgc'
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
