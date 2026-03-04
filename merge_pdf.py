import os
from pypdf import PdfReader, PdfWriter

# ===== CONFIGURE AQUI =====
pasta_entrada = r"C:\Users\madra\OneDrive\Documentos\Certificados\artigos"
pasta_saida = r"C:\Users\madra\OneDrive\Desktop\memorial\CONCURSO_IQBQBM\06_atividades_de_pesquisa"
nome_arquivo_final = "anexo_6.5.pdf"
# ===========================

os.makedirs(pasta_saida, exist_ok=True)
caminho_saida = os.path.join(pasta_saida, nome_arquivo_final)

arquivos_pdf = sorted(
    f for f in os.listdir(pasta_entrada) if f.lower().endswith(".pdf")
)

writer = PdfWriter()

for pdf in arquivos_pdf:
    reader = PdfReader(os.path.join(pasta_entrada, pdf))
    for page in reader.pages:
        writer.add_page(page)  # primeiro adiciona

# agora comprime todas as páginas já dentro do writer
for page in writer.pages:
    page.compress_content_streams()

with open(caminho_saida, "wb") as f:
    writer.write(f)

print("PDFs unidos e otimizados.")