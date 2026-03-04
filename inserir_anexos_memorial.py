from pypdf import PdfReader, PdfWriter
from pathlib import Path

def merge_pdfs(lista_pdfs):
    writer = PdfWriter()
    for pdf in lista_pdfs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)
    return writer

def insert_pdf(base_pdf, insert_writer, pagina_insercao):

    if isinstance(base_pdf, (str, Path)):
        reader_base = PdfReader(base_pdf)
        paginas_base = reader_base.pages
    else:
        paginas_base = base_pdf.pages

    writer_final = PdfWriter()

    pagina_insercao = min(pagina_insercao, len(paginas_base))

    for i in range(pagina_insercao):
        writer_final.add_page(paginas_base[i])

    for page in insert_writer.pages:
        writer_final.add_page(page)

    for i in range(pagina_insercao, len(paginas_base)):
        writer_final.add_page(paginas_base[i])

    return writer_final

base_path = Path(r"C:\Users\madra\OneDrive\Desktop\memorial\CONCURSO_IQBQBM")

principal = base_path / "anexos_header.pdf"

bloco_s3_path = base_path / "03_formacao_academica"
s3_2 = bloco_s3_path / "anexo_3.2.pdf"
s3_3 = bloco_s3_path / "anexo_3.3.pdf"
s3_4 = bloco_s3_path / "anexo_3.4.pdf"
bloco_s3_2 = merge_pdfs([s3_2])
bloco_s3_3 = merge_pdfs([s3_3])
bloco_s3_4 = merge_pdfs([s3_4])

bloco_s4_path = base_path / "04_atuacao_profissional"
s4_1a = bloco_s4_path / "anexo_4.1.a.pdf"
s4_1b = bloco_s4_path / "anexo_4.1.b.pdf"
bloco_s4_1a = merge_pdfs([s4_1a])
bloco_s4_1b = merge_pdfs([s4_1b])

bloco_s5_path = base_path / "05_atividades_didaticas_formacao_de_resursos_humanos"
s5_1 = sorted(bloco_s5_path.glob("anexo_5.1*.pdf"))
s5_2 = bloco_s5_path / "anexo_5.2.pdf"
s5_3 = bloco_s5_path / "anexo_5.3.pdf"
s5_4 = bloco_s5_path / "anexo_5.4.pdf"
s5_6 = bloco_s5_path / "anexo_5.6.pdf"
bloco_s5_1 = merge_pdfs(s5_1)
bloco_s5_2 = merge_pdfs([s5_2])
bloco_s5_3 = merge_pdfs([s5_3])
bloco_s5_4 = merge_pdfs([s5_4])
bloco_s5_6 = merge_pdfs([s5_6])

bloco_s6_path = base_path / "06_atividades_de_pesquisa"
s6_5 = bloco_s6_path / "anexo_6.5.pdf"
s6_7 = bloco_s6_path / "anexo_6.7.pdf"
bloco_s6_5 = merge_pdfs([s6_5])
bloco_s6_7 = merge_pdfs([s6_7])

bloco_s7_path = base_path / "07_atividades_de_extensao"
lista_anexos_s7_1 = sorted(bloco_s7_path.glob("anexo_7.1*.pdf"))
lista_anexos_s7_2 = sorted(bloco_s7_path.glob("anexo_7.2*.pdf"))
lista_anexos_s7_3 = sorted(bloco_s7_path.glob("anexo_7.3*.pdf"))
lista_anexos_s7_4 = sorted(bloco_s7_path.glob("anexo_7.4*.pdf"))
lista_anexos_s7_5 = sorted(bloco_s7_path.glob("anexo_7.5*.pdf"))

bloco_s7_1 = merge_pdfs(lista_anexos_s7_1)
bloco_s7_2 = merge_pdfs(lista_anexos_s7_2)
bloco_s7_3 = merge_pdfs(lista_anexos_s7_3)
bloco_s7_4 = merge_pdfs(lista_anexos_s7_4)
bloco_s7_5 = merge_pdfs(lista_anexos_s7_5)

bloco_s8_path = base_path / "08_atividades_adiministrativas"
s8 = bloco_s8_path / "anexo_08.pdf"
bloco_s8 = merge_pdfs([s8])

insercoes = [
    (18, bloco_s8),
    (17, bloco_s7_5),
    (16, bloco_s7_4),
    (15, bloco_s7_3),
    (14, bloco_s7_2),
    (13, bloco_s7_1),
    (12, bloco_s6_7),
    (11, bloco_s6_5),
    (10, bloco_s5_6),
    (9, bloco_s5_4),
    (8, bloco_s5_3),
    (7, bloco_s5_2),
    (6, bloco_s5_1),
    (5, bloco_s4_1b),
    (4, bloco_s4_1a),
    (3, bloco_s3_4),
    (2, bloco_s3_3),
    (1, bloco_s3_2),
]

resultado = principal

for pagina, bloco in insercoes:
    resultado = insert_pdf(resultado, bloco, pagina)

with open(base_path / "anexos_final.pdf", "wb") as f:
    resultado.write(f)