# -*- coding: utf-8 -*-
"""
poema.py

Cria um time de três agentes colaborativos usando o Google ADK para compor um poema no estilo Carlos Drummond de Andrade.
Pronto para uso no Google Colab com API Gemini configurada via secrets.

Fluxo:
- AgenteTema: propõe 5 temas e escolhe 1.
- AgenteVersos: estrutura o poema em 3 estrofes de 4 versos cada, a partir do tema escolhido.
- AgenteDrummond: revisa e entrega a versão final do poema.

Autor: Seu Nome
"""

import os
import asyncio
import logging
import warnings
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# Suprime warnings do ADK e Gemini para output limpo
logging.getLogger("google_genai.types").setLevel(logging.ERROR)
logging.getLogger("google.adk.runners").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

# Configuração da API Gemini
def setup_api_key():
    try:
        from google.colab import userdata
        # Se estiver no Colab, usa secrets
        chave = userdata.get('senha')
    except ImportError:
        # Se estiver local, usa variável de ambiente
        chave = os.getenv('GOOGLE_API_KEY')
        if not chave:
            raise ValueError("GOOGLE_API_KEY não encontrada nas variáveis de ambiente")
    
    os.environ["GOOGLE_API_KEY"] = chave
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

setup_api_key()
gemini = "gemini-2.0-flash"

# Sessão ADK
APP_NAME = "poema_adk_app"
USER_ID = "user_poema"
SESSION_ID = "sessao_poema_001"
session_service = InMemorySessionService()
if not session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID):
    session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

# Função utilitária para extrair o tema escolhido do texto salvo em 'temas_e_escolhido'
def extrair_tema_escolhido(sess):
    temas = sess.state.get("temas_e_escolhido", "")
    for linha in temas.splitlines():
        if linha.lower().startswith("tema escolhido:"):
            return linha.split(":", 1)[-1].strip()
    return ""

# --- Definição dos Agentes ---

agente_tema = LlmAgent(
    name="agente_tema",
    model=gemini,
    description="Pensa em 5 temas poéticos e escolhe o melhor.",
    instruction=(
        "Pense em 5 temas poéticos profundos e universais no estilo de Carlos Drummond de Andrade. "
        "Liste os 5 temas numerados, um por linha, e depois escreva apenas o tema escolhido na linha final, no formato: Tema escolhido: ...\n"
        "Exemplo de resposta:\n"
        "1. Tema 1\n2. Tema 2\n3. Tema 3\n4. Tema 4\n5. Tema 5\nTema escolhido: ...\n"
        "Responda apenas com a lista e o tema escolhido, sem explicações."
    ),
    output_key="temas_e_escolhido"
)

agente_versos = LlmAgent(
    name="agente_versos",
    model=gemini,
    description="Estrutura o poema em 3 estrofes de 4 versos cada, a partir do tema escolhido.",
    instruction=(
        "Com base no tema escolhido:\n{state.tema_escolhido}\n\n"
        "Crie um poema em 3 estrofes de 4 versos cada, no estilo de Carlos Drummond de Andrade. "
        "Use a simplicidade drummondiana, o tom cotidiano e introspectivo. "
        "Responda apenas com o poema, sem explicações ou comentários."
    ),
    output_key="poema_estruturado"
)

agente_drummond = LlmAgent(
    name="agente_drummond",
    model=gemini,
    description="Revisa e entrega a versão final do poema.",
    instruction=(
        "Revise e finalize este poema:\n{state.poema_estruturado}\n\n"
        "Aplique o estilo característico de Carlos Drummond de Andrade:\n"
        "- Linguagem simples mas profunda\n"
        "- Imagens do cotidiano com significado universal\n"
        "- Tom reflexivo e irônico\n"
        "- Métrica e ritmo equilibrados\n\n"
        "Responda apenas com o poema revisado, sem explicações ou comentários."
    ),
    output_key="poema_final"
)

# --- Orquestrador sequencial ---
orquestrador = SequentialAgent(
    name="orquestrador_poema",
    description="Orquestra a criação do poema no estilo Drummond.",
    sub_agents=[agente_tema, agente_versos, agente_drummond]
)

runner_orquestrador = Runner(agent=orquestrador, app_name=APP_NAME, session_service=session_service)

async def criar_poema_sequencial():
    print("\n--- Iniciando composição do poema (sequencial) ---")
    
    content = types.Content(role='user', parts=[types.Part(text="Crie um poema no estilo de Carlos Drummond de Andrade.")])
    
    # Limpar estado anterior para garantir um início limpo
    session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state={}
    )
    
    try:
        # Executar o orquestrador que rodará os agentes em sequência
        async for event in runner_orquestrador.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
            # Verificar o tipo de evento usando isinstance
            if hasattr(event, 'delta') and event.delta:
                sess = session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
                current_state = sess.state
                
                # Atualizar estado com novo delta
                new_state = {**current_state, **event.delta}
                
                # Se recebemos temas_e_escolhido, extrair e salvar tema_escolhido
                if "temas_e_escolhido" in event.delta:
                    tema_escolhido = extrair_tema_escolhido(sess)
                    new_state["tema_escolhido"] = tema_escolhido
                
                # Atualizar sessão com novo estado
                session_service.create_session(
                    app_name=APP_NAME,
                    user_id=USER_ID,
                    session_id=SESSION_ID,
                    state=new_state
                )
        
        # Obter estado final da sessão
        sess = session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
        
        print("\nTemas sugeridos e escolha:")
        print(sess.state.get("temas_e_escolhido", "(não encontrado)"))
        
        print("\nPoema estruturado:")
        print(sess.state.get("poema_estruturado", "(não encontrado)"))
        
        print("\nPoema final revisado:")
        print(sess.state.get("poema_final", "(não encontrado)"))
    
    except Exception as e:
        if "RESOURCE_EXHAUSTED" in str(e) and "Gemini 2.5 Pro Preview" in str(e):
            print("\nErro: Quota do Gemini excedida!")
            print("Sugestão: Use o modelo 'gemini-2.0-flash' ou 'gemini-2.5-pro-exp-03-25' em vez do Gemini 2.5 Pro Preview.")
        else:
            # Para outros erros, mostra a mensagem completa
            print(f"\nErro inesperado: {str(e)}")

# --- Execução ---
def is_running_in_colab():
    try:
        from google.colab import userdata
        return True
    except ImportError:
        return False

if is_running_in_colab():
    # Para Colab/Jupyter, wrapping em função async
    async def main():
        await criar_poema_sequencial()
    await main()
else:
    # Para script Python (.py)
    if __name__ == "__main__":
        asyncio.run(criar_poema_sequencial())
