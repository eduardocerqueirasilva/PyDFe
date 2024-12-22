from lxml import etree
from Variaveis import CODIGOS_ESTADOS


class Estrutura_XML_DFe:
    
    def Corpo_XML_DFe(ambiente=None, uf=None, cpf_cnpj=None, chave=None, nsu=None, nsu_lote=None):
        DIST_DFE_INT = etree.Element("distDFeInt", versao="1.01", xmlns="http://www.portalfiscal.inf.br/nfe")
        
        etree.SubElement(DIST_DFE_INT, "tpAmb").text = "1" if ambiente == 'producao' else "2"
        
        if uf:
            etree.SubElement(DIST_DFE_INT, "cUFAutor").text = CODIGOS_ESTADOS[uf.upper()]
        
        
        if len(cpf_cnpj) == 11:
            etree.SubElement(DIST_DFE_INT, "CPF").text = cpf_cnpj
        else:
            etree.SubElement(DIST_DFE_INT, "CNPJ").text = cpf_cnpj
        
        
        if nsu_lote:
            distNSU = etree.SubElement(DIST_DFE_INT, "distNSU")
            etree.SubElement(distNSU, "ultNSU").text = str(nsu_lote).zfill(15)
        if chave:
            consChNFe = etree.SubElement(DIST_DFE_INT, "consChNFe")
            etree.SubElement(consChNFe, "chNFe").text = chave
        if nsu:
            consNSU = etree.SubElement(DIST_DFE_INT, "consNSU")
            etree.SubElement(consNSU, "NSU").text = str(nsu).zfill(15)
            
        
        return DIST_DFE_INT

    def Envelope_SOAP_DFe(corpo_xml):
        ENVELOPE = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Envelope', nsmap={
                        'soap12': 'http://www.w3.org/2003/05/soap-envelope',
                        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                        'xsd': 'http://www.w3.org/2001/XMLSchema'
                    })
            
        BODY = etree.SubElement(ENVELOPE, '{http://www.w3.org/2003/05/soap-envelope}Body')

        NFE_DIST_DFE_INTERESSE = etree.SubElement(BODY, "nfeDistDFeInteresse", xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe")

        NFE_DADOS_MSG = etree.SubElement(NFE_DIST_DFE_INTERESSE , 'nfeDadosMsg')

        if corpo_xml is not None:
            NFE_DADOS_MSG.append(corpo_xml)

        return etree.tostring(ENVELOPE, pretty_print=True, xml_declaration=True, encoding='UTF-8')



