from Descompactar_Gzip import DescompactaGzip
from Estrutura_DFe import Estrutura_XML_DFe
from Comunicacao import Envia_Requisicao
from Variaveis import URL_DFE


# Possui 3 tipos de consulta
# Consulta nota pela chave, exemplo: chave="43241287235172000122550010035894771753157631"
# Colsulta nsu específico, exemplo: nsu="000000000243000"
# Colsulta nsu por lote, retorna 50 nsu a partir do nsu informado, exemplo: nsu_lote="000000000243000"

# ambiente = 'producao' ou 'homologacao'

corpo_xml = Estrutura_XML_DFe.Corpo_XML_DFe(
    ambiente="producao",  
    cpf_cnpj="75104406000113",
    uf="PR",
    chave="43241287235172000122550010035894771753157631"
    #nsu="000000000243000"
    #nsu_lote="000000000243000"
   )

xml_completo = Estrutura_XML_DFe.Envelope_SOAP_DFe(corpo_xml)
        
        
print("XML COMPLETO:" , xml_completo.decode('utf-8'))


# Necessário informar a 'EMPRESA' e o ambiente, pode ser 'producao' ou 'homologacao'
xml_retornado = Envia_Requisicao('EMPRESA1',URL_DFE["producao"],xml_completo)

if xml_retornado:
    DescompactaGzip.extrair_gzip(xml_retornado)