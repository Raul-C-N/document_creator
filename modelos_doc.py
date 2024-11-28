from os import listdir
modelos_doc = {}
PATH_MODELOS = "Secrets\\Modelos"


##funcao carregar modelos da pasta de modelos
    #PATH = "Secrets\\1a_cip.txt"
    #f = open(PATH,'r')
        # 1) roda a lista de arquivos 2) cria o caminho total do modelo a ser aberto 3) abre o modelo com a funcao open(PATH,'r')


## funcao retorna lista arquivos na pasta definida no caminho 'PATH'
def listar_arquivos(PATH):
    '''funcao retorna lista arquivos na pasta definida no caminho 'PATH'''
    return listdir(PATH)
