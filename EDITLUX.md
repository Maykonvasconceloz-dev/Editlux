# Editlux para Linux

Editlux é um editor de vídeo desktop nativo, offline e gratuito para Linux. Ele é
uma derivação independente do Shotcut e utiliza Qt 6, MLT e FFmpeg. A interface é
voltada à edição rápida para criadores, preservando a capacidade profissional da
linha do tempo multicamadas do projeto original.

## O que esta versão altera

- executável, nome da aplicação, configurações, atalhos do sistema e identidade
  visual renomeados para Editlux;
- barra superior organizada em Mídia, Áudio, Texto, Elementos, Efeitos,
  Transições, Legendas, Filtros e Ajustes, com Exportar à direita;
- mídia à esquerda, visualizador no centro, propriedades à direita e linha do
  tempo na parte inferior;
- layout responsivo para telas de 1366 x 768;
- português do Brasil como idioma inicial, com inglês, espanhol, alemão e as
  demais traduções herdadas do Shotcut disponíveis nas preferências;
- predefinições de projeto para YouTube 16:9 em 1080p a 30/60 fps;
- predefinições de projeto para Instagram e Reels 9:16 em 1080p a 30/60 fps;
- atualização automática e links de suporte online desativados na configuração
  padrão, mantendo integrações locais como captura de tela e editores externos;
- fala para texto, texto para fala, modelos e vozes de IA ocultos e não
  empacotados;
- geração de pacote portátil e AppImage para Linux x86_64 por GitHub Actions.

Os recursos locais herdados continuam disponíveis, incluindo importação de mídia,
edição multicamadas, divisão e recorte, transições, filtros, correção de cor,
keyframes, legendas manuais, proxy, captura, mixagem de áudio e exportação local.

## Compilar para desenvolvimento

Dependências mínimas: compilador C++11, CMake, Ninja, Qt 6.4 ou superior, MLT++
7.36 ou superior, FFTW e os componentes multimídia descritos no `CMakeLists.txt`.

```bash
cmake --preset cc-debug-linux
cmake --build build/cc-debug-linux
cmake --install build/cc-debug-linux
```

O binário produzido para Linux chama-se `editlux`. O programa não utiliza
localhost e não é uma aplicação web: a interface e o motor de mídia são executados
diretamente no processo Qt/MLT do desktop.

## Gerar o AppImage

O fluxo `.github/workflows/build-editlux-linux.yml` constrói primeiro o pacote
portátil com todas as bibliotecas necessárias e depois gera o AppImage. Em um fork
publicado no GitHub, abra a aba **Actions**, selecione **build-editlux-linux** e
execute **Run workflow**. Os artefatos de saída serão:

- `editlux-linux-portable`;
- `editlux-linux-appimage`;
- `editlux-source`, com o código-fonte correspondente exigido pela GPLv3.

Para executar o AppImage baixado:

```bash
chmod +x editlux-linux-x86_64-*.AppImage
./editlux-linux-x86_64-*.AppImage
```

Um AppImage x86_64 atende às distribuições Linux desktop mais comuns. Máquinas ARM
ou sistemas muito antigos exigem um pacote compilado especificamente para sua
arquitetura.

## Desempenho em computador modesto

Para projetos grandes ou vídeo 4K, ative **Configurações > Proxy > Usar proxy** e
reduza a resolução de pré-visualização. Para YouTube e Instagram, prefira H.264,
1080p e aceleração de hardware somente quando o driver da máquina estiver estável.

## Licença e autoria

O código é distribuído sob GPLv3; veja `COPYING`. O copyright original do Shotcut,
de Meltytech, LLC, e os avisos das bibliotecas de terceiros permanecem preservados.
Ao distribuir um executável modificado, disponibilize também o código-fonte
correspondente e mantenha a licença e os avisos exigidos.

Editlux não é afiliado ao CapCut nem à ByteDance. Nenhum código, marca, ícone ou
recurso proprietário do CapCut faz parte deste projeto; apenas padrões gerais de
organização de uma interface de edição foram usados como referência.
