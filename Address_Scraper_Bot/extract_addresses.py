'''
Importa o modulo http.client que fornece a funcionalidade
de cliente HTTP para Python, permitindo fazer requisições
a servidores web.
'''
import http.client

'''
Importa o modulo json que fornece métodos para 
trabalhar comdados formato json, um formato comum para 
troca de dados na web.
'''
import json

#Especifica o cep para consulta
cep_exemplo = "05001000"


def obter_endereco_por_cep(cep):

    '''
    Cria uma conexão HTTPS com o servidor 'viacep.com.br', que
    hospeda a API do ViaCep. A conexão HTTPS garante que os dados 
    enviados e recebidos sejam criptografados para segurança.
    '''
    conexao = http.client.HTTPSConnection("viacep.com.br")
    '''
    Formata e envia uma requisição GET ao servidor ViaCEP
    a requisição inclui o CEP fornecido na URL. '/ws/{cep}/json/'
    especifica o formato da API que inclui o CEP e espera a resposta em formato JSON
    O método 'request' realiza a solicitação ao servidor com metodo HTTP 'GET'
    '''
    conexao.request("GET", f"/ws/{cep}/json/")

    '''
    Aguarda a resposta do servidor a solicitação feita anteriormente 
    e armazena essa resposta no objeto 'resposta' o metodo 'getresponse'
    retorna um objeto que representa a resposta HTTP recebida do servidor
    '''
    resposta = conexao.getresponse()
    '''
    Lê o conteudo completo da resposta HTTP, que é enviado pelo servidor em formato de bytes.
    O metodo 'read'. Lê os dados da resposta até que todos os dados sejam recebidos.
    '''
    dados = resposta.read()
    '''
    Decodifica os bytes recebidos para uma string em formato UTF-8
    UTF-8 é um padrão comum para codificação de caracteres
    Converte a string JSON decodificada em um dicionario Python
    usando o metodo 'Loads' do modulo json.
    Isso permite acessar os dadoss do JSON como um dicionario comum do python
    '''
    endereco = json.loads(dados.decode("utf-8"))
    conexao.close()
    

    '''
    Verifica se a chave 'erro' esta presente no ddicionario de endereço
    a presença da chave 'erro' indica que o CEP fornecido não é valido.
    '''
    if "erro" not in endereco:
        return endereco
    else:
        #se houver erro (CEP não encontrado), retorna uma mensagem de erro 
        return "CEP não encontrado"




#Utiliza a função para obter o endereço relacionado ao CEP
endereco_resultado = obter_endereco_por_cep(cep_exemplo)

#Exibe o endereço ou a mensagem de erro resultante
print(endereco_resultado)