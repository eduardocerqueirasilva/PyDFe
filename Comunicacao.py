import requests
from Certificado import certificadoA4



def Envia_Requisicao(empresa,ambiente, data):

    session = requests.Session()
    session.cert = (certificadoA4(empresa))

    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8;",
        "Accept": "application/soap+xml; charset=utf-8;",
    }

    try:
        # Tenta enviar a requisição
        response = session.post(ambiente, data=data, headers=headers, verify=False)
        response.raise_for_status()  # Levanta exceção para status HTTP de erro (4xx, 5xx)
        
        if response.status_code == 200:
            print("Lote enviado com sucesso!\n")
            #print("Response Headers:\n", response.headers)
            print("Response Content:\n", response.content.decode('utf-8'))           
            return response.content
        
        else:
            print(f"Erro no envio do lote: {response.status_code} - {response.content.decode('utf-8')}")

    except requests.exceptions.RequestException as e:
        # Captura todos os erros de requisição (conexão, HTTP, etc.)
        print(f"Erro na requisição: {e}")