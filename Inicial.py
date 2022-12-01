import cherrypy
import os
from PagTipo import *
from PagPrato import *
from PagCardapio import *
from PagexcluirP import *

localdir = os.path.dirname(__file__)

class Principal():

    pag = open("Inicial/Inical.html").read()

    @cherrypy.expose
    def index(self):
        html = self.pag
        return html


server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 81
}
cherrypy.config.update(server_config)

local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":localdir},
}

root = Principal() 
root.pgInicial = Principal()
root.pgTipo = PagTipo()
root.pgPrato = PagPrato()
root.pgCardapio = PagCardapio()
root.pgExcluir = PagExcluir()
cherrypy.quickstart(root,config=local_config)
