import cherrypy
from Db.Prato import *
from Db.Tipo import Tipo

class PagPrato():
    
    rodape = open("HTML/rodape.html").read()
    topo = open("HTML/topo_tipo.html").read()

    @cherrypy.expose
    def index(self, cId = 0, cNome ='', sem='', cdesc='', valor=0, pTipo=0, img=''):
        html = self.topo
        html += '''
                <main class="cadastro_body">
                    <div class="divide">

                    <div class="caixa_cadastro" style="height: 1080px">

                        <h1 class="titulo_cadastro">Cadastro de pratos</h1>
                        <p class="subtitulo_cadastro">Complete todas as informações do prato</p>

                        <form method="post" action="gravar_prato" class="form">
                            <div>
                                <div class="agrupamento">
                                    <label class="opcao" for="">Nome</label> <br>
                                    <input type="hidden" name="id" id="id" value="%s" required>
                                    <input class="caixa_nome" type="text" value="%s" name="nome" id="nome" required
                                        placeholder="Digite o nome do prato">
                                </div>
                                <div class="agrupamento">
                                    <label class="opcao" for="">Valor:</label> <br>
                                    <label class="opcao_2" for="">R$:</label>
                                    <input class="caixa_valor" type="number" value="%s" name="valor" id="valor" min="0" required>
                                </div>
                            </div>

                            <div class="agrupamento">
                                <label class="opcao_3" for="">Qual o Dia?</label> <br><br>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Segunda-Feira" id="dia" >Segunda
                                </label>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Terça-Feira" id="dia" >Terça
                                </label>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Quarta-Feira" id="dia" >Quarta
                                </label>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Quinta-Feira" id="dia" >Quinta <br>
                                </label>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Sexta-Feira" id="dia" >Sexta
                                </label>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Sábado" id="dia" >Sábado
                                </label>
                                <label class="opcao_2" for="">
                                    <input type="radio" name="dia" value="Domingo" id="dia" >Domingo
                                </label>
                            </div>'''%(cId, cNome, valor)

        html += self.mostar_cadastrados()

        html +=             '''
                            
                                <label class="opcao" for="">Adicione a descrição</label> <br>
                                <textarea class="caixa_area" value="%s" cols="5" name="textarea" rows="5" id="textarea" placeholder="Escreva aqui" rows="10" style="width: 332px;height: 142px;margin-top: 10px;"></textarea><br><br>
                            

                            <div class="agrupamento">
                                <label class="opcao" for="">Adicione uma imagem</label> <br>
                                <input type="file" value="%s" name="enviar_img" id="enviar_img" accept="image/*">
                            </div>
                            <button type="submit" value="Gravar" class="btn_cadastro">Cadastrar</button>
                            <hr>
                           
                        </div></form>
                            <button onclick="excluir_prato()" style="margin-top: 0px;" class="btn_cadastro">Excluir Pratos</button> </main>
                         '''%(cdesc, img)

        html += self.rodape
        return html


    @cherrypy.expose
    def excluir_prato(self):
        cherrypy.HTTPRedirect('/pgTipo')

    @cherrypy.expose
    def mostar_cadastrados(self):
        html = '''<div class="agrupamento">
                 <label class="opcao_3" for="">Qual o Tipo do prato?</label> <br><br>'''

        objTipo = Tipo()
        listaTipo = objTipo.obterTipos()
        for part in listaTipo:
            html += '''<label class="opcao_2" for="">
                        <input type="radio" name="tipo" value="%s" id="tipo" >%s
                        </label>''' %(part['id_tipo'] , part['nome_tipo'])
        html += '''<br><br><br><br>'''
        return html


    @cherrypy.expose
    def gravar_prato(self, nome, valor, dia, textarea, tipo ,enviar_img, id):
        if len(nome)>0:
            objPrato = Prato()
            objPrato.set_nome(nome)
            if len(dia)>0:
                objPrato.set_sem(dia)
                if int(valor)>0:
                    objPrato.set_valor(int(valor))
                    if int(tipo)>0:
                        objPrato.set_tipo(int(tipo))
                        if len(textarea)>0:
                            objPrato.set_desc(textarea)
                            if len(enviar_img)>0:
                                objPrato.set_img(enviar_img)

            retorno = 0 
            if int(id) == 0:
                retorno = objPrato.gravar()
            else: 
                objPrato.set_id(int(id)) 
            if retorno>0:
                raise cherrypy.HTTPRedirect('/pgPrato')
                    
            else:
                return '''
                   <h2>Erro ao gravar o prato!!</h2>
                   <a href="/pgPrato">Voltar</a>
                '''
        else:
            return '''
               <h2>O campo Nome deve estar preenchidos!!</h2>
               <a href="/pgPrato">Voltar</a>
            '''
