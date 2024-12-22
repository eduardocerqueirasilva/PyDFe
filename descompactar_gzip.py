import base64
import gzip
from lxml import etree

class DescompactaGzip:
    def descompacta(stringZipada):
        # Decodifica Base64, descompacta Gzip e parseia o XML
        xml_descompactado = etree.fromstring(
            gzip.decompress(base64.b64decode(stringZipada)).decode("utf-8")
        )

        # Opcional: printa o XML formatado
        print("XML Descompactado: \n",etree.tostring(xml_descompactado, encoding="unicode"))

        # Retorna o elemento XML
        return xml_descompactado


    def extrair_gzip(xml_resposta):
        resposta = etree.fromstring(xml_resposta)
        ns = {'ns': "http://www.portalfiscal.inf.br/nfe"}
        zip_respostas = resposta.xpath('//ns:retDistDFeInt/ns:loteDistDFeInt/ns:docZip', namespaces=ns)
        
        if not zip_respostas:
            print("Nenhum elemento docZip encontrado.")
            return

        print(f"Quantidade de docZip encontrados: {len(zip_respostas)}")
        
        for idx, doc_zip in enumerate(zip_respostas):
            zip_conteudo = doc_zip.text
            DescompactaGzip.descompacta(zip_conteudo)

