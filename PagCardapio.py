import cherrypy
from Db.Prato import *  
from datetime import date
from Db.Tipo import *

class PagCardapio():
    
    rodape = open("Cardapio/Cardapio2.html").read()
    topo = open("Cardapio/Cardapio1.html").read()

    @cherrypy.expose
    def index(self):
        html = self.topo
        html += self.happy_hour()
        html += self.exibir_cardapio()

        html +='''</section> </main>'''
        html += self.rodape
        return html

    @cherrypy.expose
    def happy_hour(self):
        num = date.today().weekday()
        sem = ("Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo")
        if (sem[num]) == 5:
            html = '''    <main class="conteudo">
        <section class="conteudo-secundario"><br>
            <h1 class="conteudo-titulo" style="font-family:freestyle, Helvetica, sans-serif;  text-transform: none;"><strong>SEXTA DO HAPPY HOUR!</strong></h1>
            <h2 class="conteudo-subtitulo">Seja lá qual for o seu dia, um momento de descontração é mais do  que merecido no</h2>
            <h2 class="conteudo-subtitulo">cotidiano de todos que lutam para cumprir e superar as metas diárias.</h2>  
            <br><br>

            <h1 class="conteudo-titulo"><strong>Nosso Cardápio</strong></h1>
            <h2 class="conteudo-subtitulo">Na D&#170; NENÊ Delivery nossa missão é oferecer um cardápio variado. Enaltecendo a culinária típica brasileira. Aqui são mais de 40 opções,</h2>
            <h2 class="conteudo-subtitulo"> divididas em 7 linhas: Segunda, Terça, Quarta, Quinta, Sexta, Sábado e Domingo.</h2>'''
            return html
        else:
            html = '''
            <main class="conteudo">
            <section class="conteudo-secundario"><br>
                <h1 class="conteudo-titulo"><strong>Nosso Cardápio</strong></h1>
                <h2 class="conteudo-subtitulo">Na D&#170; NENÊ Delivery nossa missão é oferecer um cardápio variado. Enaltecendo a culinária típica brasileira. Aqui são mais de 40 opções,</h2>
                <h2 class="conteudo-subtitulo"> divididas em 7 linhas: Segunda, Terça, Quarta, Quinta, Sexta, Sábado e Domingo.</h2>
            '''
            return html

    @cherrypy.expose
    def exibir_cardapio(self):
        aux = 0
        objPrato = Prato()
        listaPrato = objPrato.obterPratos()      
        objTipo = Tipo()
        num = date.today().weekday()
        sem = ("Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo")
        if num == 0:
            img = 'img_segunda'
        elif num == 1:
            img = 'img_terca'
        elif num == 2:
            img = 'img_quarta'
        elif num == 3:
            img = 'img_quinta'
        elif num == 4:
            img = 'img_sexta'
        elif num == 5:
            img = 'img_sabado'
        else: img = 'img_domingo'

        html = ''''''
        for part in listaPrato:
            listaTipo = objTipo.obterTipos()
            for part2 in listaTipo:
                if part2['id_tipo'] == part['tipo_prato']:
                    tipo = part2['nome_tipo']
            if (sem[num]) == part['dia_sem']:
                resto = aux % 2
                if resto != 0:
                    html += '''
                    <div class="Cardapio-inverso" style="max-width: 1280px;">
                        <div>   
                            <h1 class="dia-semana">%s</h1>
                            <h1 class="conteudo-titulo">%s</h1>
                            <h1 class="conteudo-titulo" style="font-size: 22px;">Categoria - %s</h1>
                            <h2 class="conteudo-subtitulo-d">%s</h2>  <br><br>        
                            <h1 class="conteudo-titulo" style="font-size: 50px;">R$ %s,00</h1>
                        </div>
                        <img class="foto-cardapio-inverso" src="/Cardapio/%s/%s" alt="%s">
                    </div>'''%(part['dia_sem'] , part['nome_prato'], tipo ,part['desc_prato'], part['valor_prato'], img ,part['img_prato'], part['nome_prato'])
                    aux = aux + 1
                    

                else:
                    html += '''
                    <div class="Cardapio">
                        <div>   
                            <h1 class="dia-semana">%s</h1>
                            <h1 class="conteudo-titulo">%s</h1>
                            <h1 class="conteudo-titulo" style="font-size: 22px;">Categoria - %s</h1>
                            <h2 class="conteudo-subtitulo-d">%s</h2>  <br><br>        
                            <h1 class="conteudo-titulo" style="font-size: 50px;">R$ %s,00 </h1>
                        </div>
                        <img class="foto-cardapio" src="/Cardapio/%s/%s" alt="%s">
                    </div>'''%(part['dia_sem'] , part['nome_prato'], tipo, part['desc_prato'], part['valor_prato'], img, part['img_prato'], part['nome_prato'])
                    aux = aux + 1

        return html

