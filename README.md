# AWS Lambda Email Sender

## Descrição

Este projeto consiste em uma função AWS Lambda desenvolvida em Python que envia e-mails utilizando o AWS Simple Email Service (SES). A função foi criada para demonstrar como integrar e documentar uma solução serverless. Ela utiliza variáveis de ambiente para configurar os endereços de remetente e destinatário, garantindo flexibilidade e segurança.

## Funcionalidades

- **Envio de E-mails:** Utiliza o AWS SES para enviar e-mails.
- **Uso de Variáveis de Ambiente:** Endereços de e-mails são configurados como variáveis de ambiente (ex.: `EMAIL_ORIGEM` e `EMAIL_DESTINO`).
- **Tratamento de Erros:** Possui tratamento de exceções para retornar mensagens claras em caso de falhas.
- **Integração com AWS Lambda:** A função é configurada e executada na AWS, com logs enviados para o CloudWatch.

## Pré-requisitos

- Conta na AWS com acesso ao Lambda e SES.
- E-mails (remetente e destinatário) verificados no AWS SES ou conta liberada do modo sandbox.
- Python 3.x instalado (se deseja testar localmente).
- AWS CLI configurado com as credenciais necessárias (caso opte por testes via terminal).

## Instalação

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/aws-lambda-email-sender.git
   cd aws-lambda-email-sender
Instalar Dependências

Crie um ambiente virtual (opcional) e instale as dependências necessárias:

bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Nota: Certifique-se de incluir o boto3 no arquivo requirements.txt se ainda não estiver lá.

Configuração
Antes de executar ou fazer o deploy da função, você precisará configurar as variáveis de ambiente:

EMAIL_ORIGEM: Endereço de e-mail remetente verificado no SES.

EMAIL_DESTINO: Endereço de e-mail destinatário.

Como Configurar na AWS Lambda
Acesse o Console da AWS e selecione sua função Lambda.

Na aba Configuração, vá para Variáveis de Ambiente.

Adicione as chaves EMAIL_ORIGEM e EMAIL_DESTINO com os respectivos valores.

Salve as alterações.

Teste e Execução
Testando no Console da AWS
No Console da AWS Lambda, crie um evento de teste (pode ser um JSON simples, pois a função utiliza apenas as variáveis de ambiente).

Exemplo de evento:

json
{
  "test": true
}
Clique em Test e verifique o resultado na resposta e nos logs do CloudWatch.

Testando Localmente
Você pode testar a função localmente se tiver o AWS CLI configurado ou utilizando o AWS SAM CLI:

Execute o comando de invocação (substitua NomeDaSuaFuncao pelo nome correto):

bash
aws lambda invoke --function-name NomeDaSuaFuncao --payload file://event.json output.json
Confira o arquivo output.json para a resposta e analise os logs, se necessário.

Considerações Finais
Este repositório reúne não apenas o código-fonte da função Lambda, mas também a documentação completa para que qualquer pessoa possa entender, testar e, se necessário, implantar a solução em sua própria conta AWS. Em futuras atualizações, você poderá integrar pipelines de CI/CD para automatizar o deploy e os testes.
