import argparse
from modules.brute_force import run_brute_force
from modules.dictionary_attack import run_dictionary_attack

def main():
    parser = argparse.ArgumentParser(description="Python Hash Cracking Tool")
    parser.add_argument("--hash", required=True, help="Ziel-Hashwert")
    parser.add_argument("--method", required=True, choices=["brute", "dict"], help="Angriffsmethode")
    parser.add_argument("--charset", default="all", help="Charset (nur für brute): digits, lowercase, uppercase, letters, alphanum, symbols, common, all")
    parser.add_argument("--maxlen", type=int, default=4, help="Maximale Passwortlänge (nur für brute)")
    parser.add_argument("--wordlist", help="Pfad zur Wortliste (nur für dict)")
    parser.add_argument("--algo", default="sha256", help="Hash Algorithmus: md5, sha1, sha256, sha512")

    args = parser.parse_args()

    if args.method == "brute":
        run_brute_force(args.hash, args.algo, args.charset, args.maxlen)
    elif args.method == "dict":
        if not args.wordlist:
            print("[!] Wortliste muss mit --wordlist angegeben werden.")
            return
        run_dictionary_attack(args.hash, args.algo, args.wordlist)

if __name__ == "__main__":
    main()
