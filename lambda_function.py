import os
import json
import boto3

def lambda_handler(event, context):
    # Inicializa o cliente para o SES
    ses_client = boto3.client('ses')
    
    try:
        # Obtém os valores das variáveis de ambiente
        email_origem = os.environ.get('EMAIL_ORIGEM')
        email_destino = os.environ.get('EMAIL_DESTINO')
        
        # Verifica se as variáveis estão definidas
        if not email_origem or not email_destino:
            raise Exception("As variáveis de ambiente 'EMAIL_ORIGEM' ou 'EMAIL_DESTINO' não foram definidas.")
        
        # Envia um e-mail utilizando os valores das variáveis de ambiente
        response = ses_client.send_email(
            Source=email_origem,
            Destination={
                'ToAddresses': [email_destino]
            },
            Message={
                'Subject': {'Data': 'Teste de E-mail via AWS Lambda'},
                'Body': {'Text': {'Data': 'Olá! Esta mensagem está sendo enviada a partir de uma função Lambda.'}}
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('E-mail enviado com sucesso!')
        }
    
    except Exception as e:
        print(f"Erro: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao enviar e-mail: {str(e)}')
        }
