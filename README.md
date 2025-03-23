# Gerador de Certificados em PDF

Este projeto tem como objetivo gerar certificados em PDF personalizados com base em uma lista de participantes e palestrantes de um evento. O certificado é gerado com uma imagem de fundo e informações sobre o evento, palestrantes e organizadores.

## Funcionalidades

- Geração de certificados personalizados em formato PDF.
- Personalização de fontes e cores para o nome do participante, palestrantes, data do evento e outros detalhes.
- Inclusão de uma imagem de fundo no certificado.
- Suporte para gerar certificados para múltiplos participantes em um único comando.

## Requisitos

Este projeto utiliza as seguintes bibliotecas:

- **Pillow**: Para manipulação de imagens (usado para calcular a largura do texto e para ajustar a imagem de fundo).
- **ReportLab**: Para gerar o arquivo PDF e manipular a tipografia.

Você pode instalar as dependências executando:

```bash
pip install pillow reportlab
```

## Como Usar

### Configuração dos Parâmetros

O script precisa de algumas informações configuráveis para gerar os certificados:

- **data_evento**: Data do evento.
- **nome_evento**: Nome do evento.
- **palestrantes**: Uma lista de palestrantes, onde cada palestrante tem o nome e o título da palestra.
- **organizacao**: Nome da Comissão do evento.
- **nomes**: Uma lista de nomes dos participantes que irão receber o certificado.
- **imagem_fundo**: Caminho para a imagem de fundo que será usada no certificado.
- **font_path**: Caminho para a fonte customizada (.ttf) que será usada no certificado.
- **output_dir**: Diretório onde os certificados serão salvos.

### Gerar Certificados

Chame a função `gerar_certificados_para_lista` passando os parâmetros configuráveis para gerar os certificados.

#### Exemplo de código:

```python
data_evento = '15 de março de 2025'
nome_evento = 'Concluiu o 1º Meetup Pyladies Floripa de 2025'
palestrantes = [
    {"pessoa": "• Débora Vieira", "palestra": "Data Analytics no Dia a Dia: Como Dashboards Podem Impulsionar Decisões Estratégicas"},
    {"pessoa": "• Isadora Xavier", "palestra": "Dados e Produto: Por Que Essas Duas Áreas Andam Lado a Lado"},
    {"pessoa": "• Luanda Dantas", "palestra": "Apache Airflow: A Melhor Amiga das Engenheiras de Dados"}
]
nome_organizadora = "Comissão PyLadies Floripa"
nomes = ["Letícia Duarte Hillesheim", "Maria Eduarda de Souza Oliveira", "Fernanda da Silva Souza"]
imagem_fundo = "path/to/background_image.jpg"
font_path = "path/to/font.ttf"
output_dir = "certificados-gerados"

gerar_certificados_para_lista(nomes, imagem_fundo, font_path, output_dir, palestrantes, nome_organizadora, data_evento, nome_evento)
```

### Como Executar:
    1. Configure as variáveis acima com os valores corretos.
    2. Execute o script para gerar os certificados.
    3. Os certificados serão salvos no diretório especificado em `output_dir`.

## Resultado

O código criará um arquivo PDF para cada participante com a seguinte estrutura:

- Imagem de fundo personalizada.
- Nome do participante em destaque.
- Data do evento e nome do evento.
- Detalhes sobre os palestrantes e suas respectivas palestras.
- Nome da Comissão do evento.

## Detalhamento das Funções

### `quebrar_texto`
Função que quebra o texto para que ele se ajuste corretamente dentro de um limite de largura, dividindo o texto em várias linhas, se necessário.

### `gerar_certificado`
Função principal para gerar o certificado de um único participante, incluindo informações sobre o evento, palestrantes e organizadora.

### `gerar_certificados_para_lista`
Função que chama a função `gerar_certificado` para uma lista de nomes de participantes, gerando um certificado para cada um.

## Personalização

Você pode personalizar o seguinte no código:

- **Fonte**: Para mudar a fonte, basta substituir o caminho da variável `font_path` com a localização da sua fonte `.ttf` personalizada.
- **Imagem de fundo**: Troque o caminho da variável `imagem_fundo` para usar a imagem que preferir como fundo do certificado.
- **Texto**: Altere os parâmetros como `data_evento`, `nome_evento`, `nome_organizadora` e outros para ajustar o conteúdo do certificado.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo `LICENSE` para mais detalhes.