import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# ... Seu código existente ...


def log_error_and_notify_slack(mensagem_de_erro):
    logging.error(mensagem_de_erro)

    # Conecte-se à API do Slack usando seu token
    slack_token = "xoxb-5641118665585-5652340450336-YtOMJZEUmqIlyZ3r5f6lj5m0"
    cliente_slack = WebClient(token=slack_token)

    # Defina o canal do Slack onde você deseja enviar a mensagem
    canal_slack = "C05QEBUSAER"

    # Componha a mensagem para enviar ao Slack
    mensagem_slack = f"Ocorreu um erro: {mensagem_de_erro}"

    # Envie a mensagem para o Slack
    try:
        resposta = cliente_slack.chat_postMessage(
            channel=canal_slack, text=mensagem_slack
        )
        assert resposta["message"]["text"] == mensagem_slack
    except SlackApiError as e:
        logging.error(f"Erro na API do Slack: {e.response['error']}")
