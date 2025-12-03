# 📄 Conversor PDF para PDF/A

[![Offline](https://img.shields.io/badge/status-offline%20only-brightgreen)](https://github.com/seu-usuario/conversor-pdfa)
[![Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/seu-usuario/conversor-pdfa)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Uma ferramenta **simples, local e offline** para converter arquivos PDF comuns para o formato arquivístico **PDF/A** (ISO 19005), compatível com exigências legais, fiscais e de preservação digital.

Projetado para funcionar em **apenas uma máquina Windows**, sem necessidade de internet, nuvem ou assinaturas — ideal para setores administrativos que precisam de conformidade em documentos.

---

## ✨ Recursos

- Interface gráfica intuitiva (sem linha de comando)
- Seleção múltipla de arquivos PDF
- Escolha da pasta de saída
- Conversão para **PDF/A-2b** (recomendado para uso moderno)
- Totalmente offline e gratuito
- Funciona em ambientes corporativos restritos

---

## 🛠️ Requisitos

Você precisa instalar **três componentes** (todos gratuitos):

| Componente | Versão Testada | Link para Download |
|-----------|----------------|--------------------|
| **Python** | 3.10+ (recomendado: 3.10.11) | [Python Manager 25.0 (MSIX)](https://www.python.org/ftp/python/pymanager/python-manager-25.0.msix) |
| **Ghostscript** | 10.06.0 | [gs10060w64.exe (64-bit)](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10060/gs10060w64.exe) |
| **Perfil de Cor ICC** | sRGB IEC61966-2-1 | [sRGB_IEC61966-2-1_black_scaled.icc](https://www.color.org/sRGB_IEC61966-2-1_black_scaled.icc) |

> 💡 **Dicas de instalação**:
> - Ao instalar o **Python**, **marque a opção "Add Python to PATH"**.
> - O **Ghostscript** deve ser instalado com permissões padrão (não altere o caminho de instalação).
> - O arquivo `.icc` **deve ficar na mesma pasta do script**.

---

## 🚀 Como usar

### 1. Baixe os arquivos

- [`conversor_pdfa_gui.py`](./conversor_pdfa_gui.py)
- [`sRGB_IEC61966-2-1_black_scaled.icc`](https://www.color.org/sRGB_IEC61966-2-1_black_scaled.icc)
- [`ConverterPDFA.bat`](./ConverterPDFA.bat)

## 2. Estrutura de arquivos

Todos os arquivos devem estar na mesma pasta (raiz do projeto):

### 3. Execute

- Dê **duplo clique em `ConverterPDFA.bat`**
- A interface gráfica será aberta
- Clique em **"Selecionar PDFs"** → escolha um ou mais arquivos
- Clique em **"Converter para PDF/A"** → escolha a pasta de destino
- Aguarde a conclusão!

> ✅ Os arquivos convertidos terão o sufixo `_PDF-A.pdf`.

---

## ⚙️ Como funciona por trás

O programa usa o **Ghostscript** via linha de comando para:

- Embutir fontes
- Converter cores para sRGB com perfil ICC válido
- Adicionar metadados PDF/A conforme a norma ISO
- Garantir conformidade com validadores como VeraPDF

O Python (`tkinter`) fornece apenas a interface — **todo o processamento é feito localmente pelo Ghostscript**.

---

## 📦 Opcional: Gerar executável (.exe)

Se quiser distribuir sem exigir Python instalado, use o [PyInstaller](https://pyinstaller.org):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "sRGB_IEC61966-2-1_black_scaled.icc;." conversor_pdfa_gui.py
