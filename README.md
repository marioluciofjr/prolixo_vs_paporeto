# Debate sem firula: Prolixo versus Papo Reto
Um debate de agentes com opiniões divergentes sobre um mesmo assunto

![license - MIT](https://img.shields.io/badge/license-MIT-green)
[![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)](https://prazocerto.me)
[![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)](https://linkedin.com/in/marioluciofjr)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como obter a API KEY no Google AI Studio](#como-obter-a-api-key-no-google-ai-studio)
* [Como configurar a API KEY no Google Colab](#como-configurar-a-api-key-no-google-colab)
* [Como executar](#como-executar)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

O projeto "Debate sem Firula" é uma implementação criativa do Google ADK (Agent Development Kit) que simula um debate entre dois agentes de IA com personalidades contrastantes: o Prolixo, que representa uma voz cautelosa e corporativa, e o Papo Reto, que encarna uma perspectiva direta e popular. Os agentes debatem temas escolhidos pelo usuário em rodadas interativas, onde o Prolixo oferece argumentos formais de 200-250 palavras, enquanto o Papo Reto responde com objetividade em 50-100 palavras.

## Estrutura do projeto

A ideia desse debate de agentes surgiu de um prompt compartilhado pelo colega Sidnei, do site [Mestre dos Prompts](https://toque-aqui.com/mestredosprompts/), no grupo chamado [![WhatsApp - Inteligência Artificial](https://img.shields.io/badge/WhatsApp-Inteligência_Artificial-green?logo=whatsapp&logoColor=white)](https://chat.whatsapp.com/LEb0g7ITiP0BgwhI7q6dDN "link do grupo no Whats"). Ele postou um prompt com uma proposta semelhante e tendo outros nomes. Gostei da estrutura e adaptei para esse projeto. 

Comecei o projeto utilizado um prompt no GitHub Copilot do VSCode, tendo como base o Claude Sonnet 3.5 como modelo generativo, a fim de buscar ideias a partir do prompt do Sidnei, levando em consideração a estrutura de agentes inteligentes presente na documentação oficial do Google sobre [ADK (Agent Development Kit)](https://google.github.io/adk-docs/). Além disso, eu utilizei os arquivos `adk_tutorial.py` e `poema.py`, que estão na pasta 📁 [Ref](https://github.com/marioluciofjr/prolixo_vs_paporeto/tree/main/Ref) deste repositório, como contexto do meu prompt.

O prompt que utilizei foi: 

```prompt
  <função>
  Você atuará como um desenvolvedor sênior, especializado em códigos .ipynb. Ou seja, códigos python que rodam no Google Colab. Você tem a boa prática de comentar o código inteiro para facilitar a vida de outros devs. Seu comentários sempre são em português         brasileiro. Você sempre faz o debbuging do código e segue os princípio do 'Zen of python': 
  "Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!"
  </função>
  <contexto>
  Na base de conhecimento tem os seguintes arquivos que são **PRIMORDIAIS** para a sua tarefa: 
  '@poema.py' - arquivo que funcionou no Google Colab perfeitamente e será seu modelo base para qualquer arquivo que crie daqui em diante.
  '@adk_tutorial.py' - arquivo que também funcionou no Google Colab e que servirá de documentação.
  @adk-python-main - documentação oficial do ADK Google. É uma boa prática sempre conferir a documentação.
  </contexto>
  <tema>
  1. Utilize a primeira mensagem da pessoa usuária para fazer a seguinte pergunta: "Qual será o tema do nosso ADK de hoje?"
  2. Assim que a pessoa definir o tema, você vai criar um código python de acordo com a estrutura do modelo 'poema.py'. 
  Lembre-se que os pacotes necessários para instalação encabeçam o código: 
  ```python
    # Instalando o pacote necessário
    !pip install -q -U google-adk 
    !pip install -q -U litellm 
    print("Instalação completa")
    ```
  REGRA: mantenha o sinal "!" antes do pip, pois será útil para a pessoa usuária quando copiar para o Google Colab.
  3. Refatore o código para verificar se está tudo correto. Pense passo a passo nessa etapa. 
  4. Entregue o código final em uma caixa de código que permita que a pessoa copie o código para inserir no Google Colab em seguida: 
  ```python
    código final
    ```
  </tarefa>
  
```

  > [!CAUTION]
  > ⚠️ Antes de mergulhar no "vibe coding", saiba que é fundamental ter uma compreensão básica da estrutura do código. Conhecer os fundamentos da programação e a arquitetura do projeto permite uma colaboração mais efetiva com a IA generativa, resultando em soluções mais coerentes e personalizadas para suas necessidades específicas. Lembre-se também de sempre ler as documentações oficiais.

Depois de refinar o código como eu queria, colei no Google Colab e separei em 5 seções: 

1. `Bibliotecas necessárias`
2. `Classes necessárias`
3. `Configuração da API`
4. `Definição do modelo generativo`
5. `Código ADK`

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/63e3b960-3dc5-48fc-a300-b3104430235f" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/284057b9-6543-4245-ae33-12fe293e7dca" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/cf957637-962d-4548-87d4-bbde91fadc22" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/31ed57e7-f4b7-4d86-9373-668a38f8db17" />&nbsp;&nbsp;&nbsp  
  <img align="center" height="60" width="80" src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Google_Colaboratory_SVG_Logo.svg" />&nbsp;&nbsp;&nbsp    
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/0324b2d2-c9f4-4c2e-ba62-703a7f346de6" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
    
</div>

## Requisitos

Para utilizar este projeto, você precisa de:

- **Conta Google**: Necessária para acessar o Google AI Studio e o Google Colab
- **Chave de API do Google AI Studio (Gemini API)**: Instruções para obtenção abaixo

> [!IMPORTANT]
> O código está configurado para ser executado no Google Colab, que fornece todos os recursos computacionais necessários gratuitamente.

## Como obter a API KEY no Google AI Studio

Para utilizar este código, você precisará de uma chave de API do Google Gemini:

1. Acesse o [Google AI Studio](https://ai.dev/app/apikey)
2. Faça login com sua conta Google
3. Clique no botão "Criar chave de API"
4. Aceite os termos de serviço, se solicitado
5. Copie a chave gerada e guarde-a em local seguro

> [!IMPORTANT]
> Atualmente, o Google AI Studio oferece um uso gratuito da API para testes. Sobre demais detalhes da API do Gemini, leia a [documentação oficial](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#:~:text=O%20uso%20do%20Google%20AI,em%20todos%20os%20pa%C3%ADses%20dispon%C3%ADveis). Caso você não queira utilizar o Gemini, pesquise como obter a API KEY do modelo generativo de sua preferência.

## Como configurar a API KEY no Google Colab

Para utilizar sua chave API no Google Colab de forma segura:

1. Abra seu notebook no Google Colab
2. Na barra lateral esquerda, clique no ícone 🔑 (Secrets)
3. Clique em "+ Adicionar novo secret"
4. No campo "Nome", digite `senha`
5. No campo "Valor", cole sua chave API do Google AI Studio

> [!TIP]
> O código está configurado para acessar a chave por meio de `chave = userdata.get('senha')`. Se preferir usar outro nome, modifique esta linha no código: 

```python
# Usa a chave armazenada nos secrets do Colab sob o nome 'senha'
        chave = userdata.get('senha')
  ```

## Como executar

Abaixo você terá um checklist básico para utilizar o código no Google Colab, sendo que o atalho para executar as células por lá é `CTRL` + `ENTER`

- [ ] Obter a API_KEY no Google AI Studio
- [ ] Clicar no botão ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) dentro do arquivo [`debate_sem_firula.ipynb`](https://github.com/marioluciofjr/prolixo_vs_paporeto/blob/main/debate_sem_firula.ipynb)
- [ ] Configurar a API_KEY em 'Secrets' no Google Colab
- [ ] Executar o primeiro bloco do código (instalações - deixei também a biblioteca [`litellm`](https://github.com/BerriAI/litellm) caso queira utilizar outro modelo generativo em vez do Gemini)
- [ ] Executar o segundo bloco do código (importações)
- [ ] Executar o terceiro bloco de código (api)
- [ ] Executar o quarto bloco do código (escolher o modelo generativo - no caso do Gemini, você pode ver todas as opções disponíveis com o código [`Modelos_Gemini.ipynb`](https://github.com/marioluciofjr/codesoiram.python/blob/main/Modelos_Gemini.ipynb))
- [ ] Executar o quinto bloco de código (adk)

## Links úteis

* [Documentação oficial do ADK (Agent Development Kit)](https://google.github.io/adk-docs/) - Tudo que você precisa saber sobre o ADK do Google;
* [O que é vibe coding?](https://medium.com/@niall.mcnulty/vibe-coding-b79a6d3f0caa) - Explica como programar descrevendo o que você quer em linguagem natural;
* [O que são agentes de IA?](https://www.ibm.com/br-pt/think/topics/ai-agents) - Explicação da IBM sobre agentes inteligentes de IA;
* [6 segredos do GitHub Copilot no VSCode](https://youtu.be/FaR6tQ1VMnc?si=vvtBvtGKnhNmline) - vídeo do canal `Código Fonte TV`sobre o GitHub Copilot no VSCode, com explicação bem didática a respeito do assunto;
* [O que é uma API?](https://www.alura.com.br/artigos/api) - Guia da Alura sobre APIs;
* [Tudo sobre o Secrets do Google Colab](https://medium.com/@parthdasawant/how-to-use-secrets-in-google-colab-450c38e3ec75) - Tutorial completo sobre armazenamento seguro no Google Colab;
* [Como instalar o VSCode](https://code.visualstudio.com/download) - link direto para download.

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/prolixo_vs_paporeto/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 








