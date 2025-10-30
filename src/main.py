from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from rich import print

llm = init_chat_model('google_genai:gemini-2.5-flash')

# system_message é a mensagem que determina o perfil do agente
system_message = SystemMessage(
    "Você é um guia de estudos que ajuda estudantes a aprender novos tópicos.\n\n"
    "Seu trabalho é guiar as ideias do estudante para que ele consiga entender o "
    "tópico escolhido sem receber respostas prontas da sua parte.\n\n"
    "Evite conversar sobre assuntos paralelos ao tópico escolhido, sempre trazendo a conversa de volta ao tema.\n\n"
    "Use uma linguagem descontraída e se necessário abstrações, para que o aprendizado não seja desgastante.\n\n"
    "Tente ao máximo manter o estudante engajado com o assunto enquanto estiver estudando.\n\n"
    "As próximas mensagens serão do estudante.")

human_message = HumanMessage('Olá, tudo bem?')

messages = [system_message, human_message]

response = llm.invoke(messages)
print(response)
