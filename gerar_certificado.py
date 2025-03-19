from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Função que gera o certificado em PDF para um nome específico
def gerar_certificado(nome, imagem_fundo, font_path, output_path, texto_adicional, nome_organizadora):
    # Definir as dimensões do PDF
    width, height = 1748, 1233  # Tamanho do PDF

    # Criar o objeto canvas para gerar o PDF
    c = canvas.Canvas(output_path, pagesize=(width, height))

    # Registra a fonte customizada
    pdfmetrics.registerFont(TTFont('CustomFont', font_path))

    # Abrir e ajustar a imagem de fundo
    fundo = Image.open(imagem_fundo)
    fundo = fundo.resize((width, height))
    fundo_path = "temp_fundo.jpg"
    fundo.save(fundo_path)
    c.drawImage(fundo_path, 0, 0, width, height)

    # Configuração de fontes e cores
    c.setFont("CustomFont", 100)
    c.setFillColorRGB(0.9529411764705882, 0.6509803921568628, 0.24313725490196078)  # Cor laranja para o nome do participante

    # Posição e formatação do nome do participante
    x, y = int(width * 0.10), int(height * 0.60)
    max_width = 800  # Limitar largura do nome

    # Ajustar o nome para caber no certificado
    lines = quebrar_texto(nome, max_width, font_path, 100)
    for line in lines:
        c.drawString(x, y, line)
        y -= 120  # Espaço entre as linhas do nome

    # Texto adicional
    c.setFont("CustomFont", 40)
    lines_adicional = quebrar_texto(texto_adicional, max_width, font_path, 40)
    y_adicional = 500  # Posição inicial para o texto adicional

    for line in lines_adicional:
        c.setFillColorRGB(0, 0, 0)  # Cor preta para o texto adicional
        c.drawString(x, y_adicional, line)
        y_adicional -= 60  # Espaço entre as linhas

    # Nome da organizadora
    x_organizadora, y_organizadora = int(width * 0.10), int(height * 0.12)
    c.setFont("CustomFont", 40)
    c.drawString(x_organizadora, y_organizadora, nome_organizadora)

    # Salvar o PDF
    c.save()

    # Limpar arquivo temporário
    os.remove(fundo_path)

# Função para quebrar o texto em várias linhas
def quebrar_texto(texto, max_width, font_path, font_size):
    # Criar imagem temporária para calcular o tamanho do texto
    img_temp = Image.new('RGB', (1748, 1233), color=(255, 255, 255))
    draw = ImageDraw.Draw(img_temp)
    lines = []
    current_line = ""
    
    for word in texto.split():
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, ImageFont.truetype(font_path, font_size))
        text_width = bbox[2] - bbox[0]
        
        if text_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

# Função principal para gerar certificados para uma lista de nomes
def gerar_certificados_para_lista(lista_nomes, imagem_fundo, font_path, output_dir, texto_adicional, nome_organizadora):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for nome in lista_nomes:
        output_path = os.path.join(output_dir, f"{nome}_certificado.pdf")
        gerar_certificado(nome, imagem_fundo, font_path, output_path, texto_adicional, nome_organizadora)
        print(f"Certificado gerado para: {nome}")

# Parâmetros configuráveis
texto_adicional         = "Concluiu o ciclo de palestras no 1º Meetup Pyladies Floripa de 2025, o evento ocorreu no dia 15 de março de 2025."
nome_organizadora       = "Letícia Hillesheim"
nomes                   = ["Letícia Duarte Hillesheim", "Maria Eduarda de Souza Oliveira", "Fernanda da Silva Souza"]
imagem_fundo            = "C:/Users/Leticia/Documents/python-gerar-certificado/imagens/pyladies.jpg"
font_path               = "C:/Users/Leticia/Documents/python-gerar-certificado/fontes/AcherusFeral-Bold.ttf"
output_dir              = "certificados-gerados"

# Gerar certificados
gerar_certificados_para_lista(nomes, imagem_fundo, font_path, output_dir, texto_adicional, nome_organizadora)
