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
lista_anexos_s3 = sorted(bloco_s3_path.glob("*.pdf"))
bloco_s3 = merge_pdfs(lista_anexos_s3)

bloco_s4_path = base_path / "04_atuacao_profissional"
lista_anexos_s4 = sorted(bloco_s4_path.glob("*.pdf"))
bloco_s4 = merge_pdfs(lista_anexos_s4)

bloco_s5_path = base_path / "05_atividades_didaticas_formacao_de_resursos_humanos"
lista_anexos_s5 = sorted(bloco_s5_path.glob("*.pdf"))
bloco_s5 = merge_pdfs(lista_anexos_s5)

bloco_s6_path = base_path / "06_atividades_de_pesquisa"
s6_5 = bloco_s6_path / "anexo_6.5.pdf"
s6_7 = bloco_s6_path / "anexo_6.7.pdf"

bloco_s8_path = base_path / "08_atividades_adiministrativas"
s8 = bloco_s8_path / "anexo_08.pdf"
# print(s8)
# print(s8.exists())
# print(list((base_path / "08_atividades_adiministrativas").glob("*")))

bloco_s6_5 = merge_pdfs([s6_5])
bloco_s6_7 = merge_pdfs([s6_7])
bloco_s8 = merge_pdfs([s8])

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


insercoes = [
    (12, bloco_s8),
    (10, bloco_s7_5),
    (9, bloco_s7_4),
    (8, bloco_s7_3),
    (7, bloco_s7_2),
    (6, bloco_s7_1),
    (5, bloco_s6_7),
    (4, bloco_s6_5),
    (3, bloco_s5),
    (2, bloco_s4),
    (1, bloco_s3),
]

resultado = principal

for pagina, bloco in insercoes:
    resultado = insert_pdf(resultado, bloco, pagina)

with open(base_path / "anexos_final.pdf", "wb") as f:
    resultado.write(f)