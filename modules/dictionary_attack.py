from modules.hash_utils import hash_text
from time import time
from rich.progress import track
from modules.display import format_stats
from pathlib import Path

def run_dictionary_attack(target_hash, algo, wordlist_path):
    wordlist = Path(wordlist_path)
    if not wordlist.exists():
        print("[!] Wortliste nicht gefunden:", wordlist_path)
        return

    print(f"[+] Starte Dictionary-Angriff mit Wortliste: {wordlist_path}")

    with wordlist.open("r", encoding="utf-8", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    start = time()
    attempts = 0

    for word in track(words, description="Teste Wörter..."):
        attempts += 1
        hashed = hash_text(word, algo)
        if hashed == target_hash:
            end = time()
            format_stats("Dictionary", word, attempts, end - start)
            return

    print("\n[✘] Kein Passwort gefunden.")
