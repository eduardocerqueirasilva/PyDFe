from lxml import etree
from datetime import datetime
from Variaveis import CODIGOS_ESTADOS
from AssinaturaXML import AssinaturaA1
import xmlschema
from Certificado import certificadoA4

class EventoManifestacaoDest:

    def corpo_xml_ManifestacaoDest(empresa=None,ambiente=None,cpf_cnpj=None,chave=None,data_emissao=None,uf=None,operacao=None,justificativa=None):
        
        tp_evento = {1: "210200", 2: "210210", 3: "210220", 4: "210240"}
        descricao = {1: "Confirmacao da Operacao",2: "Ciencia da Operacao",3: "Desconhecimento da Operacao",4: "Operacao nao Realizada",}
                        
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        n_seq_evento = 1
        identificador = "ID%(tp_evento)s%(chave)s%(n_seq_evento)s" % {"tp_evento": tp_evento[operacao],"chave": chave, "n_seq_evento": str(n_seq_evento).zfill(2),}
        
        ENV_EVENTO = etree.Element("envEvento", versao="1.00" ,xmlns="http://www.portalfiscal.inf.br/nfe")
        etree.SubElement(ENV_EVENTO, "idLote").text = "000000000000001" #str(id_lote)
        
        EVENTO = etree.Element("evento", versao="1.00" ,xmlns="http://www.portalfiscal.inf.br/nfe")
        
        INF_EVENTO = etree.SubElement(EVENTO, "infEvento", Id=identificador)
        
        etree.SubElement(INF_EVENTO, "cOrgao").text = CODIGOS_ESTADOS[uf.upper()]
        
        etree.SubElement(INF_EVENTO, "tpAmb").text = "1" if ambiente == 'producao' else "2"
        
        if len(cpf_cnpj) == 11:
            etree.SubElement(INF_EVENTO, "CPF").text = cpf_cnpj
        else:
            etree.SubElement(INF_EVENTO, "CNPJ").text = cpf_cnpj
        
        etree.SubElement(INF_EVENTO, "chNFe").text = chave
        
        etree.SubElement(INF_EVENTO, "dhEvento").text = (data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz)
        
        etree.SubElement(INF_EVENTO, "tpEvento").text = tp_evento[operacao]
        
        etree.SubElement(INF_EVENTO, "nSeqEvento").text = str(n_seq_evento)
        
        etree.SubElement(INF_EVENTO, "verEvento").text = "1.00"
        
        DET_EVENTO = etree.SubElement(INF_EVENTO, "detEvento", versao="1.00")
        
        etree.SubElement(DET_EVENTO, "descEvento").text = descricao[operacao]
                
        if operacao == 4:
            etree.SubElement(DET_EVENTO, "xJust").text = justificativa
        
        CORPO_ASSINADO = AssinaturaA1.assinar(empresa,EVENTO)  # Retorna como string

        ENV_EVENTO.append(CORPO_ASSINADO)
               
        return ENV_EVENTO


    def Envelope_SOAP_ManifestacaoDest(corpo_xml):

        ENVELOPE = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Envelope', nsmap={
                        'soap12': 'http://www.w3.org/2003/05/soap-envelope',
                        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                        'xsd': 'http://www.w3.org/2001/XMLSchema'
                    })
            
        BODY = etree.SubElement(ENVELOPE, '{http://www.w3.org/2003/05/soap-envelope}Body')

        NFE_DADOS_MSG = etree.SubElement(BODY , 'nfeDadosMsg', xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4")
            
        if corpo_xml is not None and len(corpo_xml) > 0:        
            NFE_DADOS_MSG.append(corpo_xml)

        return etree.tostring(ENVELOPE, xml_declaration=True, encoding='UTF-8')










