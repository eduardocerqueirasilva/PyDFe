# -*- coding: utf-8 -*-
import signxml
from lxml import etree
from signxml import XMLSigner
from unicodedata import normalize
from Certificado import certificadoA4

class CustomXMLSigner(XMLSigner):
    def __init__(self, method, signature_algorithm, digest_algorithm, c14n_algorithm):
        super().__init__(method, signature_algorithm, digest_algorithm, c14n_algorithm)

    def check_deprecated_methods(self):
        pass


def remover_acentos(txt):
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")

class AssinaturaA1():
    def assinar(empresa, xml):
        """Assina o XML usando a chave e o certificado fornecidos."""
        # Busca a tag que tem Id (reference_uri), independente do namespace
        reference = xml.find(".//*[@Id]").attrib["Id"]

        # Retira acentos do XML
        xml_str = remover_acentos(etree.tostring(xml, encoding="unicode", pretty_print=False))
        xml = etree.fromstring(xml_str)

        signer = CustomXMLSigner(
            method=signxml.methods.enveloped,
            signature_algorithm="rsa-sha1",
            digest_algorithm="sha1",
            c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        )
        signer.excise_empty_xmlns_declarations = True

        # Define namespaces
        ns = {None: signer.namespaces["ds"]}
        signer.namespaces = ns

        # Prepara referência URI
        ref_uri = ("#%s" % reference) if reference else None

        with open(certificadoA4(empresa)[0], "rb") as certificado:
            certificado = certificado.read()
        
        with open(certificadoA4(empresa)[1], "rb") as chave:
            chave = chave.read()

        # Realiza a assinatura
        signed_root = signer.sign(xml, key=chave, cert=certificado, reference_uri=ref_uri)
                
        return signed_root
