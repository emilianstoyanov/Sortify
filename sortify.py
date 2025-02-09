import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp", ".ico", ".heic", ".raw", ".nef",
               ".cr2"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".csv", ".odt", ".rtf", ".tex", ".log"],
    "E-Books": [".epub", ".mobi", ".azw3", ".fb2", ".djvu"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff", ".opus"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"],
    "Program Files": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".php", ".rb", ".swift", ".cs", ".go",
                      ".ts", ".sh", ".bat",
                      ".ps1", ".json", ".xml", ".yaml", ".ini", ".pl", ".lua", ".kt", ".rs"],
    "Executables": [".exe", ".msi", ".apk", ".app", ".deb", ".rpm", ".run"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "CAD & 3D Models": [".dwg", ".dxf", ".stl", ".obj", ".step", ".iges", ".skp", ".blend", ".3ds"],
    "Torrents": [".torrent"],
    "Backups": [".bak", ".bkp", ".backup", ".old"],
    "Disk Images": [".iso", ".img", ".vmdk", ".dmg"],
    "Database Files": [".sql", ".sqlite", ".db", ".mdb", ".accdb"],
    "Spreadsheets": [".xls", ".xlsx", ".ods"],
}


def organize_files(directory):
    """Функция за подреждане на файловете в избраната директория."""
    if not directory:
        messagebox.showerror("Грешка / Error", "Моля, изберете директория! / Please choose a directory")

        return

    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            for folder, extensions in FILE_CATEGORIES.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(directory, folder))
                    break

    messagebox.showinfo("Готово! / Done!", "Файловете са подредени успешно! ✅ / Files sorted successfully! ✅!")


def choose_directory():
    """Отваря прозорец за избор на директория."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)



root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

btn_select = tk.Button(root, text="Избери папка и подреди!\n"
                                  "Choose a folder and organize!",
                       command=choose_directory, padx=10, pady=5)
btn_select.pack(pady=50)


root.mainloop()
