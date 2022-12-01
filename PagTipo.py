import cherrypy
from Db.Tipo import *
from time import sleep

class PagTipo():

    rodape = open("HTML/rodape.html").read()
    topo = open("HTML/topo_tipo.html").read()

    @cherrypy.expose
    def index(self, tId = 0, tNome =''):
        html = self.topo
        html += '''<main class="cadastro_body">
                        <div class="divide">

                            <div class="caixa_cadastro_tipo">

                            <h1 class="titulo_cadastro">Cadastro de Tipos</h1>
                            <p class="subtitulo_cadastro">Somente tipos não cadastrados serão aceitos!</p>
                            <form method="post" action="gravar_tipo" class="form">
                                <div>
                                    <div class="agrupamento">
                                        <label class="opcao" for="">Nome</label> <br>
                                        <input type="hidden" name="id" id="id" value="%s" required>
                                        <input class="caixa_nome" type="text" name="nome" value="%s" maxlength="28" id="nome" required
                                            placeholder="Digite o tipo do prato">
                                    </div>
                                    <div class="agrupamento">
                                    
                                        '''%(tId, tNome)
        html += self.mostar_cadastrados()
        html += '''                           
                                    </div>
                                    <button type="submit" value="Gravar" class="btn_cadastro">Cadastrar</button>
                                </div>
                            </form>                
                        </div>

                    </main>'''

        html += self.rodape
        return html


    @cherrypy.expose
    def mostar_cadastrados(self):
        html = '''<label class="opcao" for="">Tipos já cadastrados:</label> <br><br>'''

        objTipo = Tipo()
        listaTipo = objTipo.obterTipos()
        for part in listaTipo:
            html += '''<label class="ja_cadastrado" for="">◎&#160;  %s</label>
            <a style= " color: #919191;
                        font-size: 10px;
                        margin-left: 8px;
                        margin-bottom: 10px;
                        text-align: right;"
                        href="excluir_Tipo?idPartido=%s">[Excluir]</a> <br>''' %(part['nome_tipo'], part['id_tipo'])
        return html


    @cherrypy.expose
    def gravar_tipo(self, nome, id):
        if len(nome)>0:
            objTipo = Tipo()
            objTipo.set_nome(nome)
            retorno = 0 
            if int(id) == 0:
                retorno = objTipo.gravar()
            else: 
                objTipo.set_id(int(id))    

            if retorno>0:   
                raise cherrypy.HTTPRedirect('/pgTipo')
                   
            else:
                raise cherrypy.HTTPRedirect('/pgTipo')
            
        else:
            raise cherrypy.HTTPRedirect('/pgTipo')

        

    @cherrypy.expose()
    def excluir_Tipo(self, idPartido):
        objTipo = Tipo()
        objTipo.set_id(int(idPartido))
        if objTipo.excluir()>0:
            raise cherrypy.HTTPRedirect('/pgTipo')
        else:
            return '''<h2>Houve problemas, não executou a exclusão...</h2>
                      <a href="/pgTipo">Voltar</a>
                   '''


