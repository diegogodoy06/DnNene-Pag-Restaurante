from Db.Banco import *

class Prato():

    def __init__(self):
        
        self.__id = 0
        self.__semana = ''
        self.__nome = ''
        self.__descricao = ''
        self.__valor = 0
        self.__tipo = 0
        self.__img = ''
        self.__banco = Banco()

    def set_id(self,cId):
       if cId>0:
           self.__id = cId

    def set_sem(self, sem):
        if sem!= '':
            self.__semana = sem

    def set_nome(self, cNome):
        if cNome!= '':
            self.__nome = cNome

    def set_desc(self, cdesc):
        if cdesc!= '':
            self.__descricao = cdesc

    def set_valor(self,valor):
       if valor>0:
           self.__valor = valor

    def set_tipo(self,pTipo):
       if pTipo>0:
           self.__tipo = pTipo  

    def set_img(self, img):
        if img!= '':
            self.__img = img

    def get_id(self):
        return self.__id

    def get_sem(self):
        return self.__semana

    def get_nome(self):
        return self.__descricao
        
    def get_valor(self):
        return self.__valor
        
    def get_tipo(self):
        return self.__tipo
        
    def get_img(self):
        return self.__img
    
    def get_nome(self):
        return self.__nome


    def obterPratos_dia(self):
        sql = '''SELECT Id_prato, Nome_prato, Desc_prato, Valor_prato,
                Tipo_prato, Img_prato, Dia_sem FROM Cardapio ORDER by Dia_sem'''
        return self.__banco.executarSelect(sql)

    def obterPratos(self):
        sql = '''SELECT Id_prato, Nome_prato, Desc_prato, Valor_prato,
                Tipo_prato, Img_prato, Dia_sem FROM Cardapio ORDER by Tipo_prato'''
        return self.__banco.executarSelect(sql)

    def gravar(self):
        sql = '''INSERT INTO Cardapio (Nome_prato, Desc_prato, Valor_prato,
        Tipo_prato, Dia_sem, Img_prato) VALUES ("#cNome", "#cdesc", #valor, #ptipo, "#Dia_sem", "#Img_prato")'''

        sql = sql.replace('#cNome', self.__nome)
        sql = sql.replace('#cdesc', self.__descricao)
        sql = sql.replace('#valor', str(self.__valor))
        sql = sql.replace('#ptipo', str(self.__tipo))
        sql = sql.replace('#Dia_sem', self.__semana)
        sql = sql.replace('#Img_prato', self.__img)
        return self.__banco.executarInsertUpdateDelete(sql)



    def excluir(self):
        sql = '        DELETE FROM Cardapio WHERE Id_prato = #cId'
        sql = sql.replace('#cId', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)