# Sistema de Distribuição DFe e Manifestação de Destinatário (MDe)

## Descrição
Este projeto integra dois sistemas principais:

1. **Distribuição DFe**
   Um sistema para consulta de Notas Fiscais Eletrônicas (NF-e) por:
   - NSU (Número Sequencial Único)
   - Chave de Acesso
   - Lote de NSUs

2. **MDe (Manifestação de Destinatário)**
   Um sistema para manifestação de eventos relacionados às Notas Fiscais Eletrônicas, permitindo as seguintes ações:
   - **Confirmação da Operação**: Confirma que a operação registrada na NF-e ocorreu.
   - **Ciência da Operação**: Informa ciência sobre a operação registrada na NF-e.
   - **Desconhecimento da Operação**: Indica que o destinatário desconhece a operação registrada.
   - **Operação Não Realizada**: Declara que a operação registrada na NF-e não foi realizada.

## Funcionalidades

### Distribuição DFe
- Consulta individual de NF-e por NSU
- Consulta individual de NF-e por Chave de Acesso
- Consulta em lote de NSUs

### MDe
- Manifestação de eventos conforme as regras da Receita Federal:
  - Confirmação da operação
  - Ciência da operação
  - Desconhecimento da operação
  - Declaração de operação não realizada

## Tecnologias Utilizadas

- Linguagem de Programação: Python
- Integração com Web Services da Receita Federal

## Instalação

1. Clone o repositório:

   git clone https://github.com/eduardocerqueirasilva/PyDFe

2. Crie uma VirtualEnv caso preferir:
   python -m venv .venv

3. Instale as dependências:
    pip install -r requirements.txt

4. Necessário adicionar o certificado digital no formato pfx na pasta 'certificados'
  
  🛠️ Instruções para Configurar e Executar a Extração do Certificado

Siga as etapas abaixo para realizar a extração do seu certificado `.pfx` corretamente:

1️⃣ Coloque seu certificado no diretório correto
   - Primeiro, você precisa salvar o seu arquivo de certificado com extensão `.pfx` no diretório chamado `certificados`.
   - Este diretório é o local onde o script buscará seu certificado para realizar a extração.

2️⃣ Edite o arquivo 'empresas.py' com as informações necessárias   
   
   EMPRESAS = {
    "EMPRESA1": ["empresa1.pfx", "cp123cd"],
    "EMPRESA2": ["empresa2.pfx", "cp123cd"]
   }
   - Permite utilizar uma ou mais empresas. Necessitando informar o nome do seu certificado com sua respectiva senha. 

3️⃣ O Sistema fará a extração do certificado automaticamente ao executar uma 'Consulta' ou 'Manifestação'.
   - Será criado 2 arquivos para cada empresa, um contendo o 'Certificado' e o outro a 'Chave'. 
   Ex: EMPRESA_VALIDO_ATE_31-07-2025_cert.pem e EMPRESA_VALIDO_ATE_31-07-2025_key.pem

Seguindo esses passos, você concluirá a extração com sucesso.
Caso encontre algum erro, verifique se o nome do arquivo e a senha estão corretos, e se as dependências necessárias estão instaladas.


## Utilização

No arquivo contem 2 arquivos com exemplo:

- Consulta DFe 
Exemplo_Consulta_DistribuicaoDFe.py

- Manifestação MDe
Exemplo_Manifestacao_MDe.py


## Contato

Para dúvidas ou sugestões, entre em contato:
- Nome: Eduardo Cerqueira da Silva
- Email: eduardocerqueirasilva@gmail.com
- GitHub: github.com/eduardocerqueirasilva
