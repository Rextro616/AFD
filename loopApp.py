import tkinter as tk
from tkinter import filedialog, Text, Scrollbar, messagebox
from afdController import main
import csv
from readFileUtils import readFile

class LoopApp:
    def __init__(self, root):
        self.root = root
        self.content = ""
        self.extension = ""
        self.root.title("Lector de Archivos")
        self.root.geometry("800x600")

        # Botón para seleccionar archivo
        self.selectButton = tk.Button(self.root, text="Seleccionar Archivo", command=self.selectFile)
        self.selectButton.pack(pady=10)

        # Botón para descargar el reporte
        self.downloadButton = tk.Button(self.root, text="Descargar Reporte", command=self.downloadReport)
        self.downloadButton.pack(pady=10)

        # Cuadro de texto con scroll para mostrar el contenido del archivo
        self.frameText = tk.Frame(self.root)
        self.frameText.pack(fill=tk.BOTH, expand=True)

        self.scrollBar = Scrollbar(self.frameText)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

        self.outText = Text(self.frameText, wrap=tk.NONE, yscrollcommand=self.scrollBar.set)
        self.outText.pack(fill=tk.BOTH, expand=True)
        self.scrollBar.config(command=self.outText.yview)

    def selectFile(self):
        file = filedialog.askopenfilename(
            title="Seleccionar archivo", 
            filetypes=[("Todos los archivos", "*.*"), ("CSV", "*.csv"), 
                       ("Excel", "*.xlsx"), ("Word", "*.docx"), ("HTML", "*.html")]
        )
        if file:
            self.extension = file.split('.')[-1].lower()  # Obtener la extensión del archivo
            self.content = readFile(file, self.extension)
            self.outText.delete(1.0, tk.END)  # Limpiar cuadro de texto
            self.outText.insert(tk.END, self.content)  # Mostrar el contenido en el cuadro de texto

    def downloadReport(self):
        occurrences = main(self.content, self.extension)
        if self.content:
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