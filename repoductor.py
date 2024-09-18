import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor de Música")
        self.root.geometry("300x250")
        self.root.config(bg="#333")  # Fondo de la ventana

        # Inicializar el mixer de pygame
        mixer.init()

        # Crear estilo común para los botones
        button_style = {"bg": "#555", "fg": "white", "font": ("Arial", 12), "relief": "raised"}

        # Botón para cargar una canción
        self.load_button = tk.Button(self.root, text="Cargar Canción", command=self.load_song, **button_style)
        self.load_button.pack(pady=10)

        # Botón de reproducir
        self.play_button = tk.Button(self.root, text="Reproducir", command=self.play_song, **button_style)
        self.play_button.pack(pady=5)

        # Botón de pausa
        self.pause_button = tk.Button(self.root, text="Pausar", command=self.pause_song, **button_style)
        self.pause_button.pack(pady=5)

        # Botón de detener
        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_song, **button_style)
        self.stop_button.pack(pady=5)

        # Variable para almacenar la ruta de la canción
        self.song_path = None

    def load_song(self):
        # Abrir un cuadro de diálogo para seleccionar una canción
        self.song_path = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3 *.wav")])
    
    def play_song(self):
        if self.song_path:
            mixer.music.load(self.song_path)
            mixer.music.play()

    def pause_song(self):
        mixer.music.pause()

    def stop_song(self):
        mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
