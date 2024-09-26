import os
import shutil
import tkinter as tk
from tkinter import simpledialog, messagebox


def path_validation(path: str) -> bool:
    return os.path.isdir(path)


def create_dirs(path: str):
    for dir in DIR_TYPES:
        dir_path = os.path.join(path, dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


def list_all_files(path: str) -> list:
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    return files


def extract_file_extension(file: str) -> str:
    _, extension = os.path.splitext(file)
    return extension


def map_extension_to_folder(path: str) -> dict:
    extension_mapping = {}
    for dir, extensions in zip(DIR_TYPES, FILE_EXT_TYPES):
        dir_path = os.path.join(path, dir)
        extension_mapping[dir_path] = extensions
    return extension_mapping








def organize_files():
    path = path_entry.get()

    if not path_validation(path):
        messagebox.showerror("Eroare", "Calea introdusă nu este validă!")
        return

    mapping = map_extension_to_folder(path)
    create_dirs(path)
    files = list_all_files(path)

    moved_files = []
    for file in files:
        file_extension = extract_file_extension(file)
        moved = False
        for dir_path, extensions in mapping.items():
            if file_extension in extensions:
                try:
                    shutil.move(os.path.join(path, file), dir_path)
                    moved_files.append(file)
                    moved = True
                    break
                except Exception as e:
                    messagebox.showerror("Eroare", f'{file} nu a putut fi mutat! Eroare: {e}')
        if not moved:
            messagebox.showwarning("Atenție", f'{file} nu se potrivește cu niciun director și nu a fost mutat.')

    messagebox.showinfo("Finalizare", "Fișierele tale au fost organizate!")


def add_directory_types():
    def save_directory_types():
        new_dirs = entry_dirs.get()
        if new_dirs:
            global DIR_TYPES
            DIR_TYPES.extend([d.strip() for d in new_dirs.split(',')])
            messagebox.showinfo("Succes", "Noi tipuri de directoare au fost adăugate!")
            add_dir_window.destroy()

    add_dir_window = tk.Toplevel(root)
    add_dir_window.title("Adaugă Tipuri de Directoare")

    tk.Label(add_dir_window, text="Introduceti noi tipuri de directoare, separate prin virgulă:").pack(pady=10)
    tk.Label(add_dir_window, text="Exemplu: Pictures, Videos, Documents").pack(pady=5)

    entry_dirs = tk.Entry(add_dir_window, width=50)
    entry_dirs.pack(pady=5)

    tk.Button(add_dir_window, text="Adaugă Directoare", command=save_directory_types).pack(pady=20)


def add_file_extensions():
    def save_file_extensions():
        new_exts = entry_exts.get()
        if new_exts:
            global FILE_EXT_TYPES
            new_ext_list = [ext.strip().split() for ext in new_exts.split(',')]
            FILE_EXT_TYPES.extend(new_ext_list)
            messagebox.showinfo("Succes", "Noi extensii de fișiere au fost adăugate!")
            add_ext_window.destroy()

    add_ext_window = tk.Toplevel(root)
    add_ext_window.title("Adaugă Extensii de Fișiere")

    tk.Label(add_ext_window,
             text="Introduceti extensii noi, separate prin virgulă (folosiți lista în formatul '.ext'):")
    tk.Label(add_ext_window, text="Exemplu: .jpg, .png, .mp4, .txt").pack(pady=5)

    entry_exts = tk.Entry(add_ext_window, width=50)
    entry_exts.pack(pady=5)

    tk.Button(add_ext_window, text="Adaugă Extensii", command=save_file_extensions).pack(pady=20)


def confirm_add_files():
    response = messagebox.askyesno("Adăugare Fișiere", "Vrei să adaugi noi tipuri de directoare și extensii?")
    if response:
        add_directory_types()
        add_file_extensions()


# Configurarea interfeței grafice
root = tk.Tk()
root.title("Organizator de Fișiere")

# Crearea câmpului de text pentru cale
tk.Label(root, text="Introduceti calea:").pack(pady=10)
path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

# Crearea butonului pentru organizare
organize_button = tk.Button(root, text="Organizează Fișiere", command=organize_files)
organize_button.pack(pady=20)

# Crearea butonului pentru adăugarea de directoare și extensii
add_button = tk.Button(root, text="Adaugă Directoare și Extensii", command=confirm_add_files)
add_button.pack(pady=10)

# Definirea tipurilor de directoare și extensii
DIR_TYPES = ['Pictures', 'Videos', 'PDF_files',
             'Music', 'TXT_files', 'Python_files', 'Excel_files', 'Word_files', 'Exe_files',
             'Archived_files', 'CDR_files']
FILE_EXT_TYPES = [['.jpg', '.jpeg', '.png', '.JPG'], ['.mov', '.MOV', '.avi'], ['.pdf', '.PDF'],
                  ['.mp3', '.mp4'], ['.txt'], ['.py'],
                  ['.xls', '.xlsx', '.csv'], ['.doc', '.docx'], ['.exe'],
                  ['.7z', '.zip'], ['.cdr']]

# Pornirea aplicației
root.mainloop()