# VIDEO CONVERTER
📱ESTE APLICATIVO CONVERTE AUTOMATICAMENTE ARQUIVOS DE VÍDEO PARA UM FORMATO ESCOLHIDO PELO USUÁRIO (COMO: "MP4", "AVI", "MOV", "MKV", "WEBM") USANDO O FFMPEG.

<img src="./IMAGENS/FOTO_01.png" align="center" width="400"> <br>
<img src="./IMAGENS/FOTO_02.png" align="center" width="400"> <br>
<img src="./IMAGENS/FOTO_03.png" align="center" width="400"> <br>

## DESCRIÇÃO:
O aplicativo é um **Conversor de Vídeos com interface gráfica moderna**, desenvolvido com `customtkinter`, `tkinter`, `ffmpeg` e `threading`. Ele permite converter automaticamente arquivos de vídeo de um diretório para um novo formato com poucos cliques, mantendo uma interface intuitiva e responsiva.

Ideal para quem precisa converter vários vídeos de forma rápida e centralizada, com feedback visual de progresso e status em tempo real.

## FUNCIONALIDADES:
✅ **Conversão automática** de todos os arquivos de vídeo em um diretório para o formato desejado.

🎞️ **Suporte a formatos populares**: `MP4`, `AVI`, `MOV`, `MKV`, `WEBM`, entre outros.

🖼️ **Interface gráfica moderna (tema escuro)** com `customtkinter`, responsiva e redimensionável.

📁 **Botão de seleção de diretório** para escolher a pasta com os vídeos que serão convertidos.

🔘 **Botões horizontais de seleção de formato** (MP4, AVI, MOV, MKV, WEBM), centralizados e organizados em uma área com borda visual elegante.

⚙️ **Conversão em segundo plano (thread)**, sem travar a interface.

📊 **Barra de progresso com contador e percentual**, indicando visualmente o andamento da conversão.

📝 **Área de status com logs em tempo real**, exibindo mensagens do `ffmpeg`, nomes dos arquivos e possíveis erros.

🔄 Ao iniciar uma nova conversão, **a barra de progresso e os logs são reiniciados automaticamente**, mas **a mensagem do diretório selecionado é preservada**.

📂 Os arquivos convertidos são salvos em uma **subpasta automática chamada `CONVERTIDOS_<FORMATO>`** (exemplo: `CONVERTIDOS_MP4`), dentro do mesmo diretório original.

✅ Ao final da conversão, uma mensagem de sucesso é exibida e o caminho da pasta de saída é mostrado no log.

## COMO USAR?
1. **Instale as bibliotecas necessárias:** Antes de executar o app, certifique-se de instalar todas as dependências necessárias. No terminal, execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt em `CODIGO`:
   ```bash
   pip install -r requirements.txt
   ```

2. **Instalar `ffmpeg`:** O App depende da ferramenta externa chamada `ffmpeg` para converter os arquivos de vídeo.

   1. **Baixar `ffmpeg`:**
      - Vá para o site oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
      - Na seção de downloads, clique em "Windows builds from gyan.dev" ou um equivalente.
      - Baixe o arquivo ZIP de uma versão estável, por exemplo: `ffmpeg-git-full.7z`.

   2. **Extrair o `ffmpeg`:**
      - Extraia o conteúdo do arquivo baixado para uma pasta em seu computador, como `C:\ffmpeg`.

   3. **Adicionar `ffmpeg` ao caminho (PATH):**
      - Abra o **Painel de Controle** e vá para **Sistema e Segurança** > **Sistema** > **Configurações avançadas do sistema**.
      - Clique em **Variáveis de Ambiente**.
      - Em **Variáveis de Sistema**, selecione a variável **Path** e clique em **Editar**.
      - Adicione uma nova entrada com o caminho completo para a pasta `bin` dentro da pasta onde você extraiu o `ffmpeg`, por exemplo: `C:\ffmpeg\bin`.
      - Clique em **OK** e feche as janelas.

   4. **Verificar a instalação:**
      - Abra o Prompt de Comando e digite `ffmpeg` para verificar se está funcionando corretamente. Você deve ver uma lista de comandos suportados se tudo foi configurado corretamente.

3. **Executar o APP:**
   * No diretório `./CODIGO`, execute o aplicativo com o comando:

   ```bash
   python CODIGO.py
   ```

4. **Abrir o Programa**
   Execute o script Python. A janela principal do conversor será exibida em modo maximizado e com tema escuro.

5. **Selecionar um Diretório**
   Clique no botão **"DIRETÓRIO"** para escolher a pasta onde estão os seus vídeos.
   O caminho selecionado será exibido na caixa de status.

6. **Escolher o Formato de Saída**
   Selecione o formato desejado clicando em um dos botões horizontais (por exemplo: `MP4`, `AVI`, `MKV`, etc).

7. **Iniciar a Conversão**
   Clique no botão **"CONVERTER"** para iniciar o processo.
   Isso irá:

   * Zerar a barra de progresso.
   * Limpar os logs anteriores da área de status (preservando o diretório selecionado).
   * Iniciar a conversão em segundo plano, mantendo a interface responsiva.

8. **Acompanhar o Progresso**

   * A barra de progresso será atualizada a cada vídeo convertido.
   * A contagem e o percentual aparecerão abaixo da caixa de status.
   * A área de status exibirá mensagens em tempo real do `ffmpeg`, além de possíveis erros.

9. **Conferir os Arquivos Convertidos**

   * Após a finalização, será exibida uma mensagem de sucesso.
   * A caixa de status mostrará **"Conversão concluída!"** e também o caminho da pasta onde os arquivos foram salvos.
   * Os vídeos convertidos estarão em uma subpasta criada automaticamente chamada:
     **`CONVERTIDOS_<FORMATO>`** (por exemplo: `CONVERTIDOS_MP4`), dentro da pasta original.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
- Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

- **Observação:** Certifique-se de que o `ffmpeg` esteja instalado e adicionado à variável de ambiente PATH do sistema para que o executável funcione corretamente.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE CUSTOMTKINTER](https://github.com/VILHALVA/CURSO-DE-CUSTOMTKINTER)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO BASEADO NO "AUDIO CONVERTER"](https://github.com/VILHALVA/AUDIO-CONVERTER)