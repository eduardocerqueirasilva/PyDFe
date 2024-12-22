from Variaveis import URL_MDFE
from Comunicacao import Envia_Requisicao
from Estrutura_MDe import EventoManifestacaoDest
from datetime import datetime

# Para realizar a Manifestação é necessário assinar o corpo do xml,
# para isso é necessário informar a chave da empresa que consta no arquivo Certificado.py. Exemplo: "CP"
# ambiente = 'producao' ou 'homologacao'
# uf = 'AN' | Ambiente Nacional
# operacao = '1' | Confirmacao da Operação
# operacao = '2' | Ciência da Operação
# operacao = '3' | Deconhecimento da operacao
# operacao = '4' | Operação não Realizada | Informar Justificativa
# justificativa = "Só é necessário informar em caso de Operação não Realizada"


xml_corpo_assinado = EventoManifestacaoDest.corpo_xml_ManifestacaoDest(
    empresa='EMPRESA1',
    ambiente='producao',
    cpf_cnpj='75104406000113',
    chave='43241287235172000122550010035894771753157631',
    data_emissao=datetime.now(),
    uf='AN',
    operacao=1, 
    justificativa='teste'
    )

#print(etree.tostring(xml_corpo_assinado).decode("utf-8"))

xml_completo = EventoManifestacaoDest.Envelope_SOAP_ManifestacaoDest(xml_corpo_assinado)

print("XML COMPLETO:" , xml_completo.decode())

# Necessário informar a 'EMPRESA' e o ambiente, pode ser 'producao' ou 'homologacao'
xml_retornado = Envia_Requisicao('EMPRESA1',URL_MDFE["producao"],xml_completo)