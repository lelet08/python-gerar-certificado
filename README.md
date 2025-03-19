# Gerador de Certificados para a Comunidade PyLadies

Este projeto é um gerador de certificados em PDF desenvolvido para a comunidade PyLadies. Ele foi criado para automatizar a geração de certificados de participação em eventos, como palestras e meetups. O código utiliza a biblioteca `PIL` (Pillow) para manipulação de imagens e `reportlab` para a criação de PDFs.

## Funcionalidades

- Gera certificados em PDF personalizados para cada participante.
- Ajusta automaticamente o nome do participante para caber no certificado.
- Adiciona texto adicional e o nome da organizadora ao certificado.
- Suporta a utilização de fontes personalizadas.

## Atenção Especial: Nomes dos Participantes

Para evitar que o texto fique sobreposto ou desalinhado, o nome de cada participante é limitado a **3 nomes**. Por exemplo, o nome "Maria Eduarda de Souza Oliveira" será reduzido para "Maria Eduarda de Souza". Isso garante que o texto fique legível e bem formatado no certificado.

## Variáveis do Projeto

- **`texto_adicional`**: Texto que será exibido no certificado, como uma mensagem de conclusão ou detalhes do evento.
- **`nome_organizadora`**: Nome da organizadora do evento, que será exibido no certificado.
- **`nomes`**: Lista de nomes dos participantes que receberão os certificados.
- **`imagem_fundo`**: Caminho da imagem de fundo que será utilizada no certificado.
- **`font_path`**: Caminho da fonte personalizada que será utilizada no certificado.
- **`output_dir`**: Diretório onde os certificados gerados serão salvos.

## Como Utilizar

1. **Instale as dependências**:
   Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalá-las usando o pip:
   ```bash
   pip install pillow reportlab

2. **Configure as Variáveis**:

Para utilizar o gerador de certificados, é necessário configurar as variáveis conforme as informações do evento e dos participantes. Abaixo estão os detalhes de cada variável:

#### **`texto_adicional`**
- **Descrição**: Texto que será exibido no certificado, como uma mensagem de conclusão ou detalhes do evento.
- **Exemplo**:
  ```python
  texto_adicional = "Concluiu o ciclo de palestras no 1º Meetup Pyladies Floripa de 2025, o evento ocorreu no dia 15 de março de 2025."
  ```python

# Parâmetros configuráveis
nome_organizadora       = "Letícia Hillesheim"  # Nome da organizadora do evento
nomes                   = [  # Lista de nomes dos participantes (limitado a 3 nomes por participante)
    "Letícia Duarte Hillesheim", 
    "Maria Eduarda de Souza Oliveira", 
    "Fernanda da Silva Souza"
]
imagem_fundo            = "C:/python-gerar-certificado/imagens/pyladies.jpg"  # Caminho da imagem de fundo
font_path               = "C:/python-gerar-certificado/fontes/AcherusFeral-Bold.ttf"  # Caminho da fonte personalizada
output_dir              = "certificados-gerados"  # Diretório de saída para os certificados

# Gerar certificados
gerar_certificados_para_lista(nomes, imagem_fundo, font_path, output_dir, texto_adicional, nome_organizadora)


### Explicação das Variáveis:
- **`nome_organizadora`**: Nome da pessoa responsável pela organização do evento, que será exibido no certificado.
- **`nomes`**: Lista de nomes dos participantes. Cada nome será limitado a 3 nomes para evitar sobreposição de texto no certificado.
- **`imagem_fundo`**: Caminho completo da imagem que será usada como fundo do certificado.
- **`font_path`**: Caminho completo da fonte personalizada que será usada no texto do certificado.
- **`output_dir`**: Diretório onde os certificados gerados serão salvos. Se o diretório não existir, ele será criado automaticamente.

### Como Executar:
1. Configure as variáveis acima com os valores corretos.
2. Execute o script para gerar os certificados.
3. Os certificados serão salvos no diretório especificado em `output_dir`.
