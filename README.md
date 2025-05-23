# VIDEO CONVERTER
📱ESTE APLICATIVO CONVERTE AUTOMATICAMENTE ARQUIVOS DE VÍDEO PARA UM FORMATO ESCOLHIDO PELO USUÁRIO (COMO: "MP4", "AVI", "MOV", "MKV", "WEBM") USANDO O FFMPEG.

<img src="./IMAGENS/FOTO_01.png" align="center" width="400"> <br>
<img src="./IMAGENS/FOTO_02.png" align="center" width="400"> <br>
<img src="./IMAGENS/FOTO_03.png" align="center" width="400"> <br>

## DESCRIÇÃO:
O aplicativo é um **Conversor de Vídeos com interface gráfica**, feito com `customtkinter`, `tkinter`, `ffmpeg` e `threading`. Ele permite converter diversos arquivos de vídeo de um diretório para outro formato com poucos cliques. 

## FUNCIONALIDADES:
* Converte automaticamente **todos os arquivos de vídeo** em um diretório para um formato de saída escolhido.
* Suporta formatos populares como: `MP4`, `AVI`, `MOV`, `MKV`, `WEBM`, entre outros.
* Feita com `customtkinter`, usando tema escuro e visual responsivo.
* Permite selecionar um diretório com arquivos de vídeo usando um botão de navegação.
* Você pode escolher o formato desejado com botões de seleção (MP4, AVI, MOV, etc).
* Mostra no final uma mensagem de sucesso.
* Exibe o log de conversão e erros, se houver, em uma **caixa de texto**.
* Os arquivos convertidos são salvos automaticamente em uma subpasta: `CONVERTIDOS_<FORMATO>` (por exemplo: `CONVERTIDOS_MP4`).

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
   Execute o script Python. A janela principal será exibida.

5. **Selecionar um Diretório**
   Clique no botão **"DIRETÓRIO"** para escolher a pasta onde estão seus vídeos.

6. **Escolher o Formato de Saída**
   Clique em um dos botões de formato (por exemplo, `MP4`, `MKV`, `AVI`) para selecionar o formato desejado.

7. **Iniciar Conversão**
   Clique no botão **"CONVERTER"**.
   O programa processará os vídeos automaticamente em segundo plano (sem travar a interface).

8. **Acompanhar o Progresso**
   A janela de status mostrará os vídeos sendo convertidos e possíveis mensagens do `ffmpeg`.

9. **Conferir os Arquivos Convertidos**
   Após o término, os arquivos convertidos estarão em uma subpasta criada dentro da pasta original.

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