from pypdf import PdfWriter
from pathlib import Path

def juntar_pdfs(pdf1, pdf2, nome_saida):
    merger = PdfWriter()

    # A ordem em que você der o 'append' é a ordem final do arquivo
    for pdf in [pdf1, pdf2]:
        try:
            merger.append(pdf)
            print(f"Adicionado: {pdf}")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{pdf}' não foi encontrado.")
            return

    # Salva o resultado
    with open(base_path / nome_saida, "wb") as arquivo_final:
        merger.write(arquivo_final)
    
    merger.close()
    print(f"Sucesso! Arquivo salvo como: {nome_saida}")

# --- USO ---
# Passe os nomes dos arquivos na ordem que desejar

base_path = Path(r"C:\Users\madra\OneDrive\Desktop\memorial\CONCURSO_IQBQBM")

memorial = base_path / "memorial.pdf"
anexos = base_path / "anexos_final.pdf"

juntar_pdfs(memorial,anexos, "memorial_final.pdf")