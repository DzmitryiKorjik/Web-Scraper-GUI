import requests
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext, font
from bs4 import BeautifulSoup
import customtkinter as ctk

def scraper():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Attention", "Veuillez saisir une URL.")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        contenu = response.text

        preview.configure(state="normal")
        preview.delete("1.0", "end")
        apercu = "\n".join(contenu.splitlines()[:20])
        preview.insert("end", apercu)
        preview.configure(state="disabled")

        save_button.configure(state="normal")
        extract_button.configure(state="normal")
        global full_content
        full_content = contenu

    except requests.RequestException as e:
        messagebox.showerror("Erreur", f"Erreur lors de la récupération de la page :\n{e}")

def sauvegarder():
    fichier = filedialog.asksaveasfilename(
        defaultextension=".html",
        filetypes=[("Fichiers HTML", "*.html"), ("Tous les fichiers", "*.*")]
    )
    if fichier:
        with open(fichier, "w", encoding="utf-8") as f:
            f.write(full_content)
        messagebox.showinfo("Succès", f"Fichier sauvegardé sous : {fichier}")

def extraire_infos():
    if not full_content:
        messagebox.showwarning("Attention", "Aucun contenu à analyser.")
        return

    soup = BeautifulSoup(full_content, "html.parser")
    infos = []

    titre = soup.title.string.strip() if soup.title and soup.title.string else "(pas de titre)"
    infos.append(f"TITLE : {titre}")

    description = soup.find("meta", attrs={"name": "description"})
    keywords = soup.find("meta", attrs={"name": "keywords"})
    desc = description['content'] if description and 'content' in description.attrs else "(pas de description)"
    keys = keywords['content'] if keywords and 'content' in keywords.attrs else "(pas de mots-clés)"
    infos.append(f"DESCRIPTION : {desc}")
    infos.append(f"KEYWORDS : {keys}")

    for hn in ["h1", "h2", "h3"]:
        titres = [t.get_text(strip=True) for t in soup.find_all(hn)]
        if titres:
            infos.append(f"{hn.upper()} :")
            for titre in titres:
                infos.append(f"  - {titre}")

    preview.configure(state="normal")
    preview.delete("1.0", "end")
    preview.insert("end", "\n".join(infos))
    preview.configure(state="disabled")

# --- Interface dark mode ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

BG_COLOR = "#2F2F2F"  # Couleur homogène pour toute la fenêtre

root = ctk.CTk()
root.title("Web Scraper")
root.configure(bg=BG_COLOR)

url_frame = ctk.CTkFrame(root, fg_color=BG_COLOR, corner_radius=6, border_width=0)
url_frame.pack(pady=(12, 0), padx=0)

url_label = ctk.CTkLabel(url_frame, text="URL à scraper :", font=("Segoe UI", 11), text_color="#ffffff")
url_label.pack(side="left", padx=(10, 8))
url_entry = ctk.CTkEntry(url_frame, width=400, font=("Segoe UI", 11))
url_entry.pack(side="left")
scrape_button = ctk.CTkButton(
    url_frame, text="Scraper", font=("Segoe UI", 11, "bold"), corner_radius=6,
    fg_color="#233d23", hover_color="#2FA600", text_color="#b2fcb2", command=scraper
)
scrape_button.pack(side="left", padx=8)

preview = ctk.CTkTextbox(
    root, width=720, height=240, font=("Consolas", 11),
    fg_color="#232329", text_color="#EDEDED", corner_radius=8, border_width=0
)
preview.pack(padx=14, pady=(10, 0))
preview.configure(state="disabled")

action_frame = ctk.CTkFrame(root, fg_color=BG_COLOR, corner_radius=6, border_width=0)
action_frame.pack(pady=(10, 12))

save_button = ctk.CTkButton(
    action_frame,
    text="Sauvegarder dans un fichier",
    font=("Segoe UI", 11, "bold"),
    corner_radius=6,
    fg_color="#233d23",
    hover_color="#2FA600",
    text_color="#b2fcb2",
    command=sauvegarder,
    state="disabled"
)
save_button.pack(side="left", padx=5)

extract_button = ctk.CTkButton(
    action_frame, text="Extraire infos (titres, meta)", font=("Segoe UI", 11, "bold"), corner_radius=6,
    fg_color="#1a293c", hover_color="#79f8f8", text_color="#121519", command=extraire_infos, state="disabled"
)
extract_button.pack(side="left", padx=5)

full_content = ""

root.mainloop()