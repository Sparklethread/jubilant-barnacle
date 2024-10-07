import os
import shutil

# Definiera sökvägen till nedladdningsmappen
nedladdningar_mapp = os.path.expanduser("~/Downloads")

# Definiera kategorier och deras respektive filtillägg samt en kategori för mappar
kategorier = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Dokument": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Ljud": [".mp3", ".wav", ".ogg", ".flac"],
    "Video": [".mp4", ".avi", ".mov", ".mkv"],
    "Komprimerade": [".zip", ".rar", ".7z"],
    "Övrigt": []  # För filer som inte passar in i andra kategorier
}

# Skapa mappar för varje kategori om de inte redan finns
for kategori in kategorier:
    kategori_mapp = os.path.join(nedladdningar_mapp, kategori)
    if not os.path.exists(kategori_mapp):
        os.makedirs(kategori_mapp)

# Gå igenom alla filer i nedladdningsmappen
for filnamn in os.listdir(nedladdningar_mapp):
    fil_sökväg = os.path.join(nedladdningar_mapp, filnamn)
    
    # Kontrollera om det är en fil (inte en mapp)
    if os.path.isfile(fil_sökväg):
        fil_tillägg = os.path.splitext(filnamn)[1].lower()
        
        # Hitta rätt kategori för filen
        målkategori = "Övrigt"
        for kategori, tillägg in kategorier.items():
            if fil_tillägg in tillägg:
                målkategori = kategori
                break
        
        # Flytta filen till rätt mapp
        mål_sökväg = os.path.join(nedladdningar_mapp, målkategori, filnamn)
        shutil.move(fil_sökväg, mål_sökväg)
        print(f"Flyttade {filnamn} till {målkategori}")

print("Sortering och kategorisering av nedladdningsmappen är klar.")
