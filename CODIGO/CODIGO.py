import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import subprocess
from threading import Thread
import glob

class VideoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONVERSOR DE VÍDEOS")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.selected_directory = ""
        self.output_format = ctk.StringVar(value="mp4")

        self.scrollable_frame = ctk.CTkScrollableFrame(root, width=580, height=580)
        self.scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.scrollable_frame, text="CONVERSOR DE VÍDEOS", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.select_dir_button = ctk.CTkButton(self.scrollable_frame, text="DIRETÓRIO", command=self.select_directory)
        self.select_dir_button.pack(pady=5)

        self.convert_button = ctk.CTkButton(self.scrollable_frame, text="CONVERTER", command=self.start_conversion)
        self.convert_button.pack(pady=5)

        self.format_frame_container = ctk.CTkFrame(self.scrollable_frame, border_width=2, border_color="gray")
        self.format_frame_container.pack(pady=10, padx=10)

        self.format_label = ctk.CTkLabel(self.format_frame_container, text="FORMATO DE SAÍDA:", font=("Arial", 12))
        self.format_label.pack(pady=(10, 0))

        self.radio_buttons_frame = ctk.CTkFrame(self.format_frame_container)
        self.radio_buttons_frame.pack(pady=10, padx=10)

        formats = ["mp4", "avi", "mov", "mkv", "webm"]
        for fmt in formats:
            ctk.CTkRadioButton(
                self.radio_buttons_frame, text=fmt.upper(), variable=self.output_format, value=fmt
            ).pack(side="left", padx=5, pady=5)

        self.status_textbox = ctk.CTkTextbox(self.scrollable_frame, width=500, height=200)
        self.status_textbox.pack(pady=10)
        self.status_textbox.configure(state='disabled')

        self.progress_frame = ctk.CTkFrame(self.scrollable_frame)
        self.progress_frame.pack(pady=(0, 5), fill="x", padx=10)

        self.progress_count_label = ctk.CTkLabel(self.progress_frame, text="0/0", width=50, anchor="w")
        self.progress_count_label.pack(side="left")

        self.progress_bar = ctk.CTkProgressBar(self.progress_frame)
        self.progress_bar.set(0)
        self.progress_bar.pack(side="left", expand=True, fill="x", padx=10)

        self.progress_percent_label = ctk.CTkLabel(self.progress_frame, text="0%", width=50, anchor="e")
        self.progress_percent_label.pack(side="right")

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_directory = directory
            self.append_status(f"Diretório selecionado: {directory}\n")

    def start_conversion(self):
        if not self.selected_directory:
            messagebox.showerror("Erro", "Por favor, selecione um diretório primeiro.")
            return
        self.clear_status()
        Thread(target=self.convert_videos).start()

    def convert_videos(self):
        input_dir = self.selected_directory
        selected_format = self.output_format.get()
        output_dir = os.path.join(input_dir, f"CONVERTIDOS_{selected_format.upper()}")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        video_extensions = ['*.mp4', '*.avi', '*.mov', '*.mkv', '*.flv', '*.wmv', '*.webm', '*.mpeg']
        video_files = []
        for ext in video_extensions:
            video_files.extend(glob.glob(os.path.join(input_dir, ext)))

        total_files = len(video_files)
        if not video_files:
            self.append_status("Nenhum arquivo de vídeo encontrado no diretório!\n")
            return

        converted_count = 0

        for idx, file_path in enumerate(video_files, start=1):
            filename = os.path.basename(file_path)
            name_without_ext = os.path.splitext(filename)[0]
            output_file = os.path.join(output_dir, f"{name_without_ext}.{selected_format}")

            cmd = ["ffmpeg", "-y", "-i", file_path, output_file]

            self.append_status(f"Convertendo: {filename} para {selected_format.upper()}...\n")

            try:
                result = subprocess.run(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                self.append_status(result.stdout)
            except Exception as e:
                self.append_status(f"Erro ao converter {filename}: {e}\n")
                continue

            converted_count += 1
            progress = converted_count / total_files
            self.progress_bar.set(progress)
            self.progress_count_label.configure(text=f"{converted_count}/{total_files}")
            self.progress_percent_label.configure(text=f"{int(progress * 100)}%")

        self.append_status(f"\nConversão concluída!\nArquivos convertidos salvos em: {output_dir}\n")
        messagebox.showinfo("Finalizado", f"Todos os vídeos foram convertidos para {selected_format.upper()} com sucesso!")

    def append_status(self, message):
        self.status_textbox.configure(state='normal')
        self.status_textbox.insert('end', message)
        self.status_textbox.see('end')
        self.status_textbox.configure(state='disabled')

    def clear_status(self):
        self.status_textbox.configure(state='normal')
        current_text = self.status_textbox.get("1.0", "end")
        dir_line = ""
        for line in current_text.strip().splitlines():
            if line.startswith("Diretório selecionado:"):
                dir_line = line
                break

        self.status_textbox.delete("1.0", "end")
        if dir_line:
            self.status_textbox.insert("end", dir_line + "\n")

        self.status_textbox.configure(state='disabled')
        self.progress_bar.set(0)
        self.progress_count_label.configure(text="0/0")
        self.progress_percent_label.configure(text="0%")

if __name__ == "__main__":
    root = ctk.CTk()
    app = VideoConverterApp(root)
    root.state("zoomed")
    root.resizable(True, True)
    root.mainloop()
