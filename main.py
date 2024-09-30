import tkinter as tk
from tkinter import filedialog, Text, Scrollbar, messagebox
import pandas as pd
from docx import Document
from bs4 import BeautifulSoup
import csv

def readFile(pathFile):
    extension = pathFile.split('.')[-1].lower()

    if extension == 'csv':
        try:
            df = pd.read_csv(pathFile)
            return df.to_string()
        except Exception as e:
            return f"Error al leer el archivo CSV: {e}"
    elif extension == 'xlsx':
        try:
            df = pd.read_excel(pathFile, engine='openpyxl')
            return df.to_string()
        except Exception as e:
            return f"Error al leer el archivo XLSX: {e}"
    elif extension == 'docx':
        try:
            doc = Document(pathFile)
            fullText = [paragraphs.text for paragraphs in doc.paragraphs]
            return '\n'.join(fullText)
        except Exception as e:
            return f"Error al leer el archivo DOCX: {e}"
    elif extension == 'html':
        try:
            with open(pathFile, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                try:
                    tables = pd.read_html(pathFile)
                    return tables[0].to_string()  # Mostramos solo la primera tabla
                except:
                    pass
                
                return soup.get_text()
        except Exception as e:
            return f"Error al leer el archivo HTML: {e}"
    else:
        return "Tipo de archivo no soportado."

def selectFile():
    file = filedialog.askopenfilename(
        title="Seleccionar archivo", 
        filetypes=[("Todos los archivos", "*.*"), ("CSV", "*.csv"), 
                   ("Excel", "*.xlsx"), ("Word", "*.docx"), ("HTML", "*.html")]
    )
    if file:
        content = readFile(file)
        outText.delete(1.0, tk.END)  # Limpiar cuadro de texto
        outText.insert(tk.END, content)  # Mostrar el contenido en el cuadro de texto
        print(content)

def downloadReport():
    content = outText.get(1.0, tk.END).strip()
    
    if content:
        savePath = filedialog.asksaveasfilename(
            defaultextension=".csv", 
            filetypes=[("CSV files", "*.csv")],
            title="Guardar reporte"
        )
        
        if savePath:
            try:
                keys = occurrences[0].keys()
                with open(savePath, 'w', newline='') as output:
                    writer = csv.DictWriter(output, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(occurrences)
                
                messagebox.showinfo("Éxito", "El reporte ha sido guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    else:
        messagebox.showwarning("Advertencia", "No hay contenido para guardar.")

# Crear la ventana principal
window = tk.Tk()
window.title("Lector de Archivos")

# Configurar el tamaño de la ventana
window.geometry("800x600")

# Crear un botón para seleccionar el archivo
selectButton = tk.Button(window, text="Seleccionar Archivo", command=selectFile)
selectButton.pack(pady=10)

# Crear un botón para descargar el reporte
downloadButton = tk.Button(window, text="Descargar Reporte", command=downloadReport)
downloadButton.pack(pady=10)

# Crear un cuadro de texto con scroll para mostrar el contenido del archivo
frameText = tk.Frame(window)
frameText.pack(fill=tk.BOTH, expand=True)

scrollBar = Scrollbar(frameText)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

outText = Text(frameText, wrap=tk.NONE, yscrollcommand=scrollBar.set)
outText.pack(fill=tk.BOTH, expand=True)
scrollBar.config(command=outText.yview)

window.mainloop()
