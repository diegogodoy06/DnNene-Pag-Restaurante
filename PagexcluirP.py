import cherrypy
from Db.Prato import *

class PagExcluir():

    rodape = open("HTML/rodape.html").read()
    topo = open("HTML/topo_tipo.html").read()

    @cherrypy.expose
    def index(self):
        html = self.topo
        html += '''
                <main class="cadastro_body">
                    <div class="divide">

                     <div class="caixa_cadastro" style="height: 100%; width: 100%;">
        
                        <h1 class="titulo_cadastro">Exclusão de pratos</h1>
                        <p class="subtitulo_cadastro">Selecione o prato para excluir</p>

                        <form method="post" action="gravar_prato" class="form">
                            <div>
                                <div class="agrupamento">
                '''
        html += self.mostrar()
        html += self.rodape
        return html

    @cherrypy.expose
    def excluir_Prato(self, id_prato):
        objPrato = Prato()
        objPrato.set_id(int(id_prato))
        if objPrato.excluir()>0:
            raise cherrypy.HTTPRedirect('/pgExcluir')
        else:
            return '''<h2>Houve problemas, não executou a exclusão...</h2>
                      <a href="/pgExcluir">Voltar</a>
                   '''

    @cherrypy.expose
    def mostrar(self):


        html = '''<br><hr><label style="font-size: 22px" class="opcao" for="">Segunda-Feira</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Segunda-Feira":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])

        html += '''<br><hr><label style="font-size: 22px" class="opcao" for="">Terça-Feira</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Terça-Feira":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])


        html += '''<br><hr><label style="font-size: 22px" class="opcao" for="">Quarta-Feira</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Quarta-Feira":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])

        html += '''<br><hr><label style="font-size: 22px" class="opcao" for="">Quinta-Feira</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Quinta-Feira":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])

        html += '''<br><hr><label style="font-size: 22px" class="opcao" for="">Sexta-Feira</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Sexta-Feira":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])
                                    
        html += '''<br><hr><label style="font-size: 22px" class="opcao" for="">Sábado</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Sábado":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])


        html += '''<br><hr><label style="font-size: 22px" class="opcao" for="">Domingo</label><br><br><br>'''
        objPrato = Prato()
        listaPrato = objPrato.obterPratos_dia()
        for part in listaPrato: 
            if part['dia_sem']=="Domingo":
                html += '''<label style="font-size: 16px" class="opcao" for="">%s</label>
                        <a style= " color: #919191;
                                    font-size: 10px;
                                    margin-left: 8px;
                                    margin-bottom: 10px;
                                    text-align: right;"
                                    href="excluir_Prato?id_prato=%s">[Excluir]</a> <br><br>
                                    ''' %(part['nome_prato'], part['id_prato'])


        html += '''</div></div></form></div></div></main>'''
        return html


