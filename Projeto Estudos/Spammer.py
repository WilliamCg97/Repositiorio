import pywhatkit as kit
import datetime

# Função para enviar mensagem no WhatsApp
def enviar_mensagem_whatsapp(numero, mensagem, hora, minuto):
    try:
        kit.sendwhatmsg(numero, mensagem, hora, minuto)
        print(f"Mensagem enviada para {numero} às {hora}:{minuto}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    numero_contato = "+1234567890"  # Substitua pelo número do contato
    mensagem_enviar = "Olá! Isso é um teste de chatbot."
    hora_envio = datetime.datetime.now().hour
    minuto_envio = datetime.datetime.now().minute + 1  # Envia em 1 minuto

    enviar_mensagem_whatsapp(numero_contato, mensagem_enviar, hora_envio, minuto_envio)
