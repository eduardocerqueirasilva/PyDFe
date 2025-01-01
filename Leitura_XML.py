from lxml import etree
import base64
import gzip


teste = """<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><nfeDistDFeInteresseResponse xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe"><nfeDistDFeInteresseResult><retDistDFeInt xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" versao="1.01" xmlns="http://www.portalfiscal.inf.br/nfe"><tpAmb>1</tpAmb><verAplic>1.7.2</verAplic><cStat>138</cStat><xMotivo>Documento localizado</xMotivo><dhResp>2024-12-30T16:49:51-03:00</dhResp><ultNSU>000000000243874</ultNSU><maxNSU>000000000243931</maxNSU><loteDistDFeInt><docZip NSU="000000000243874" schema="resNFe_v1.01.xsd">H4sIAAAAAAAEAIVSXW+CQBD8KxdeG7i940vJeokiGo2iQW1s3xBRaBQMXNWf31NsG/vS5HI3u5nZmWwOq7QOBym5Hg9F7V3rbUfLpDx5lF4uF+NiGmW1pxyA0fV0skiy9BhrP+T8f7KeF7WMiyTVyDmt6rjsaMwA9pjxpD+VlYwPu7xO4oORFztjU9Fil2oCk0xFFBbj6rg2A8sCBwBsy7Vt5aYgc1jLZoyZpgngtmykjQb9cD4Wzxqk9yZew/KYii7pjZZB6M9W0ZL4s2kQ+aMZ6QdkEERRdxiECzJZ9rtEJ34faaPBUSDa4Lg2d8wWQ6pK3GbBMRccuKUzrvPWkoEHtme1dTA9AKQNAeUpHAilub94VpfTBoOrxDeM23z/Gh+EnEbvcE2qVXcdZB/jtx4fnvhu//niQkeNakjKM0qTjSz/2roeN39tHxws5lUpBbutESxgKjtYbaRNG5NFLm8bU9G+IdLmc4gvJZBFFiUCAAA=</docZip></loteDistDFeInt></retDistDFeInt></nfeDistDFeInteresseResult></nfeDistDFeInteresseResponse></soap:Body></soap:Envelope>"""


def extrair_dados_xml(xml):
    from lxml import etree
    import gzip
    import base64

    if isinstance(xml, str):
        xml_bytes = xml.encode('utf-8')
    else:
        xml_bytes = xml

    resposta = etree.fromstring(xml_bytes)
    ns = {'ns': "http://www.portalfiscal.inf.br/nfe"}    
    contador_resposta = len(resposta.xpath('//ns:retDistDFeInt/ns:loteDistDFeInt/ns:docZip', namespaces=ns))
    cStat = resposta.xpath('//ns:retDistDFeInt/ns:cStat', namespaces=ns)[0].text
    ult_nsu = resposta.xpath('//ns:retDistDFeInt/ns:ultNSU', namespaces=ns)[0].text
    dhResp = resposta.xpath('//ns:retDistDFeInt/ns:dhResp', namespaces=ns)[0].text

    lista_dados = []

    if cStat == '138':
        for contador_xml in range(contador_resposta):
            tipo_schema = resposta.xpath('//ns:retDistDFeInt/ns:loteDistDFeInt/ns:docZip/@schema', namespaces=ns)[contador_xml]   
            nsu = resposta.xpath('//ns:retDistDFeInt/ns:loteDistDFeInt/ns:docZip/@NSU', namespaces=ns)[contador_xml]
            zip_resposta = resposta.xpath('//ns:retDistDFeInt/ns:loteDistDFeInt/ns:docZip', namespaces=ns)[contador_xml].text           
            zip_resposta_descompactado = gzip.decompress(base64.b64decode(zip_resposta)).decode("utf-8")        
            xml_descompactado = etree.fromstring(zip_resposta_descompactado.encode('utf-8'))

            chNFE = xml_descompactado.xpath('//ns:chNFe', namespaces=ns)
            chNFE = chNFE[0].text if chNFE else ""

            cnpj = xml_descompactado.xpath('//ns:CNPJ', namespaces=ns)
            cnpj = cnpj[0].text if cnpj else ""   

            xNome = xml_descompactado.xpath('//ns:xNome', namespaces=ns)
            xNome = xNome[0].text if xNome else ""    

            dhEmi = xml_descompactado.xpath('//ns:dhEmi', namespaces=ns)
            dhEmi = dhEmi[0].text if dhEmi else ""

            vNF = xml_descompactado.xpath('//ns:vNF', namespaces=ns)
            vNF = vNF[0].text if vNF else ""

            dados_documento = {
                "cnpj": cnpj,
                "xNome": xNome,
                "NSU": nsu,
                "chNFE": chNFE,
                "tipoSchema": tipo_schema,
                "zipDescompactado": zip_resposta_descompactado,
                "dhEmi": dhEmi,
                "vNF": vNF,
            }

            lista_dados.append(dados_documento)

    elif cStat == '137':
        print(f'Não há mais documentos a pesquisar')

    else:
        print(f'Falha')

    documentos_fiscais = {
        "dadosDocumentos": lista_dados
    }

    return documentos_fiscais, ult_nsu , cStat, dhResp



#documentos_fiscais, ult_nsu , cStat, dhResp = extrair_dados_xml(teste)
#print(documentos_fiscais)