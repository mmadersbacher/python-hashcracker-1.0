from itertools import product
from time import time
from rich.progress import track
from modules.hash_utils import hash_text
from modules.display import format_stats
import string

def resolve_charset(code):
    presets = {
        "digits": string.digits,
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "letters": string.ascii_letters,
        "alphanum": string.ascii_letters + string.digits,
        "symbols": string.punctuation,
        "common": string.ascii_letters + string.digits + "!@#$_",
        "all": string.ascii_letters + string.digits + string.punctuation + "äöüÄÖÜß"
    }
    return presets.get(code.lower())

def run_brute_force(target_hash, algo, charset_code, maxlen):
    charset = resolve_charset(charset_code)
    if not charset:
        print(f"[!] Ungültiger Zeichensatz-Code: {charset_code}")
        print("Gültige Werte:")
        print("  digits, lowercase, uppercase, letters, alphanum, symbols, common, all")
        return

    print(f"[+] Starte Brute-Force mit Charset '{charset_code}' (Hash: {algo.upper()}, Länge bis {maxlen})")

    start = time()
    attempts = 0

    for length in range(1, maxlen + 1):
        total = len(charset) ** length
        print(f"\n[*] Prüfe Passwortlänge {length} ({total:,} Kombinationen)")

        for combo in track(product(charset, repeat=length), total=total, description=f"[{length}] Versuche..."):
            guess = ''.join(combo)
            attempts += 1
            hashed = hash_text(guess, algo)

            if hashed == target_hash:
                end = time()
                format_stats("Brute-Force", guess, attempts, end - start)
                return

    print("\n[✘] Kein Passwort gefunden.")
