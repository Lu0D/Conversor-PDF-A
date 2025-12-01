import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Configurações — AJUSTE SE PRECISAR
GS_PATH = r"C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe"
ICC_PROFILE = "sRGB_IEC61966-2-1_black_scaled.icc"

# Verifica se o ICC está na mesma pasta do script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ICC_FULL_PATH = os.path.join(SCRIPT_DIR, ICC_PROFILE)

if not os.path.isfile(ICC_FULL_PATH):
    messagebox.showerror("Erro", f"Arquivo ICC não encontrado:\n{ICC_FULL_PATH}")
    exit(1)

class PDFaConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor PDF para PDF/A")
        self.root.geometry("500x200")
        self.root.resizable(False, False)

        self.pdf_files = []

        # Botão para selecionar arquivos
        tk.Button(root, text="Selecionar PDFs", command=self.select_pdfs, width=20).pack(pady=10)
        self.label_files = tk.Label(root, text="Nenhum arquivo selecionado", wraplength=450)
        self.label_files.pack()

        # Botão para converter
        tk.Button(root, text="Converter para PDF/A", command=self.convert, width=25, bg="#4CAF50", fg="white").pack(pady=15)

        # Status
        self.status = tk.Label(root, text="", fg="blue")
        self.status.pack()

    def select_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Selecione os arquivos PDF",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        self.pdf_files = list(files)
        if self.pdf_files:
            self.label_files.config(text=f"{len(self.pdf_files)} arquivo(s) selecionado(s)")
        else:
            self.label_files.config(text="Nenhum arquivo selecionado")

    def convert(self):
        if not self.pdf_files:
            messagebox.showwarning("Atenção", "Selecione pelo menos um arquivo PDF.")
            return

        # Escolher pasta de saída
        output_dir = filedialog.askdirectory(title="Escolha a pasta de saída")
        if not output_dir:
            return

        self.status.config(text="Convertendo...")
        self.root.update()

        sucesso = 0
        for pdf in self.pdf_files:
            try:
                nome = os.path.splitext(os.path.basename(pdf))[0]
                saida = os.path.join(output_dir, f"{nome}_PDF-A.pdf")

                comando = [
                    GS_PATH,
                    "-dPDFA=2",
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-dUseCIEColor",
                    "-sProcessColorModel=DeviceRGB",
                    "-sDEVICE=pdfwrite",
                    f"-sOutputFile={saida}",
                    "-dAutoRotatePages=/None",
                    "-sColorConversionStrategy=RGB",
                    f"-sDefaultRGBProfile={ICC_FULL_PATH}",
                    "-dPDFACompatibilityPolicy=1",
                    pdf
                ]

                subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                sucesso += 1
            except Exception as e:
                print(f"Erro ao converter {pdf}: {e}")

        self.status.config(text="")
        if sucesso == len(self.pdf_files):
            messagebox.showinfo("Concluído", f"✅ {sucesso} arquivo(s) convertido(s) com sucesso!")
        else:
            messagebox.showwarning("Concluído com falhas", f"⚠️ {sucesso} de {len(self.pdf_files)} convertido(s). Veja o terminal para detalhes.")

# Roda a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFaConverterApp(root)
    root.mainloop()