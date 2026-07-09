# 🔤 Jogo das Letras Faladas

Um jogo de letras interativo e totalmente acessível, desenvolvido em **Python** utilizando a biblioteca gráfica **Tkinter** e recursos de **Text-to-Speech (TTS)**. O projeto foi projetado com foco em inclusão digital, acessibilidade para pessoas com deficiência visual e apoio pedagógico na alfabetização infantil.

---

## 🏗️ Arquitetura do Projeto e Boas Práticas

O maior diferencial deste projeto está na sua **arquitetura limpa e desacoplada**, seguindo princípios de design de software como a separação de responsabilidades e a injeção de dependência. O sistema é dividido em camadas bem definidas dentro do pacote `app/`:

* **`PalavraRepository` (`app/repository.py`):** Camada de dados responsável pelo armazenamento e gerenciamento das palavras e suas respectivas letras iniciais em memória.
* **`JogoEngine` (`app/game_engine.py`):** Concentra todas as regras de negócio e o controle de estado do jogo (contagem de acertos, erros e validação da rodada), sendo totalmente independente da interface gráfica.
* **`AudioService` (`app/audio_service.py`):** Camada de infraestrutura que encapsula o motor de voz (Text-to-Speech) utilizando a biblioteca `pyttsx3`.
* **`JogoView` (`app/game_view.py`):** Camada de apresentação que gerencia a interface gráfica com Tkinter e captura os eventos do teclado.
* **`main.py`:** O ponto de entrada da aplicação, responsável por orquestrar a inicialização e realizar a **Injeção de Dependência** de forma explícita.

Essa separação garante que o código seja altamente testável, de fácil manutenção e modular, permitindo, por exemplo, alterar o motor de áudio ou o banco de dados sem impactar as regras do jogo ou a interface visual.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Desenvolvido e testado no ecossistema Python 3.13)
* **Tkinter** (Interface Gráfica nativa)
* **pyttsx3** (Mecanismo de síntese de voz / Text-to-Speech)

---

## 📦 Estrutura de Pastas

```text
jogo_letras/
│
├── app/
│   ├── __init__.py
│   ├── audio_service.py
│   ├── game_engine.py
│   ├── game_view.py
│   └── repository.py
│
├── .gitignore
├── main.py
└── requirements.txt
```

---

## 🚀 Como Executar o Projeto

Como o projeto utiliza recursos nativos de interface gráfica e áudio, siga as instruções abaixo de acordo com o seu sistema operacional.

### 📋 Pré-requisitos

* **No Windows:**
  Certifique-se de ter o **Python 3** instalado através do [site oficial do Python](https://www.python.org/). Durante a instalação, verifique se a opção **"Add Python to PATH"** e o suporte a **tcl/tk and IDLE** (que inclui o Tkinter) estão marcados. O serviço de voz nativo do Windows (SAPI5) já é suportado automaticamente pela biblioteca de áudio.

* **No Linux (Sistemas baseados em Debian/Ubuntu):**
  Em distribuições Linux, o Tkinter é separado do pacote padrão do Python para otimização de espaço. Certifique-se de instalar a extensão gráfica antes de iniciar:
  ```bash
  sudo apt update
  sudo apt install python3-tk -y
  ```

### ⚙️ Configuração do Ambiente Virtual

1. Clone ou baixe este repositório na sua máquina e abra o terminal dentro da pasta raiz do projeto.
2. Crie o ambiente virtual (`venv`):
   * **Linux / macOS / Windows:**
     ```bash
     python -m venv .venv
     ```
     *(Nota: No Linux, se o comando acima falhar, utilize `python3 -m venv .venv`)*

3. Ative o ambiente virtual:
   * **No Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```
   * **No Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   * **No Windows (Prompt de Comando - CMD):**
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
     *(Dica para Windows: Se o PowerShell bloquear a ativação, execute o comando `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

4. Com o ambiente virtual ativado, instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### 🎮 Executando o Jogo

Com o ambiente virtual ativo e as dependências instaladas, execute o arquivo principal:

* **No Linux:**
  ```bash
  python3 main.py
  ```
* **No Windows:**
  ```cmd
  python main.py
  ```

---

## 🕹️ Como Jogar

O jogo foi pensado para ser controlado inteiramente pelo teclado, facilitando a usabilidade e acessibilidade:

* **Barra de Espaço (`Space`):** Inicia um novo desafio ou avança para a próxima palavra após o feedback do sistema.
* **Teclas Alfabéticas (`A-Z`):** Digite a letra correspondente à primeira letra da palavra ditada pelo sistema.
* **Tecla Esc (`Escape`):** Fecha o jogo a qualquer momento de forma segura.

---

## 📈 Próximos Passos (Roadmap de Evolução)

* [ ] Adicionar suporte nativo cross-platform otimizado para chamadas de sistema no Linux (`espeak` via `subprocess`).
* [ ] Implementar testes unitários para a camada `JogoEngine`.
* [ ] Adicionar suporte a categorias de palavras (Animais, Objetos, Alimentos).