from Db.Banco import *

class Tipo():

    def __init__(self):
        
        self.__id = 0
        self.__nome = ''
        self.__banco = Banco()

    def set_id(self,tId):
       if tId>0:
           self.__id = tId

    def set_nome(self, tNome):
        if tNome!= '':
            self.__nome = tNome

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome



    def obterTipos(self):
        sql = '''SELECT Id_tipo, Nome_tipo
                 FROM Tipo_prato
                 ORDER by Id_tipo   '''
        return self.__banco.executarSelect(sql)

    def gravar(self):
        sql = '''INSERT into Tipo_prato (Nome_tipo) VALUES("#tNome")'''
        sql = sql.replace('#tNome', self.__nome)
        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):
        sql = 'DELETE FROM Tipo_prato WHERE Id_tipo = #tId'
        sql = sql.replace('#tId', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)