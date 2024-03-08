Contabilidade = '''
    Ciêncis Social aplicada
        Tecnicas e metodologias para
            Capta, registra, acumular, resumir e interpretar 
                fenômenos 
                    patrimoniais, financeiros e econômicos 
                        das Entidades
                            Com e Sem fins lucrativos
                                Pessoas físicas
                                Pessoas Jurídicas
                                    D.Público
                                        Estado, Município, União, Autarquia
                                    Privado

'''
class Topico:
    def __init__(self, tema, tese, solution, brain_storm, frases):
        self.tema = tema
        self.tese = tese
        self.solution = solution
        self.brain_storm = brain_storm
        self.frases = frases

    def definir_tema(self, new_tema):
        self.tema = new_tema

    def definir_tese(self, new_tese):
        self.tese = new_tese
    
    def definir_solution(self, new_solution):
        self.solution = new_solution
    
    def definir_brain_srotm(self, new_brain_srotm):
        self.brain_storm = new_brain_srotm

    def definir_brain_srotm(self, new_frases):
        self.frases = new_frases

    def imprimir_informacoes(self):
        print(f"\nTema: {self.tema},\n\tTese: {self.tese}")
        print(f"\t\tSolution: {self.solution}")
        print(f"\nBrain_Storm: {self.brain_storm}\n")
        #print(f"Frases: {self.frases}")
        cout =1
        for i in (self.frases):
            print(f"Frase: {cout} {i}")
            cout = cout +1

# Exemplo de uso da classe
tema_ = 'Tema - Campo de atuação da Contabilidade'
tese_ = 'Tese - O campo de atuação da Contabilidade é Muito Amplo'
solution_ = 'Solution - Desenvolver a noção de contabilidade atravez da experiência fornecida e vivida pelas empresas - Finalidades Lucrativas'
brain_storm_ = [
    'Ciência social aplicada',
    'Captar',
    'Registrar',
    'Acumular',
    'Resumir',
    'Interpretar',
    'Fenômenos Patrimonias',
    'Fenômenos Financeiros',
    'Fenômenos Econômicos',
    'Entidades',
    'Lucratividade',
    'Empresas',
    'Direito Público',
    'Estado',
    'Município',
    'União',
    'Autarquia',
    'Método Contábil',
    'Capitalismo',
    'Comércio',
    'Indústria',
    'Partidadas Dobradas',
    'Controle']
frases_ = [
    'frase1','frase2']
topic1 = Topico(
    tema=tema_, 
    tese=tese_, 
    solution=solution_, 
    brain_storm=brain_storm_,
    frases=frases_)
topic1.imprimir_informacoes()
#pg. 15/345
#file:///L:/Linear_/Base-Jump_08/1%20-%20Contabilidade%20Introdut%C3%B3ria%20(Livro%20Texto)%20-%20Sergio%20Iudicibus.pdf