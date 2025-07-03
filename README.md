# Python Hash Cracker 1.0

Dies ist ein Python-Tool zum Knacken von Passwort-Hashes. Es unterstützt zwei Methoden: Brute-Force und Dictionary-Angriff. Verschiedene Hash-Algorithmen wie MD5, SHA1, SHA256 und SHA512 sind eingebaut.

---

## Funktionen

- Brute-Force-Angriff mit wählbarem Zeichensatz und maximaler Passwortlänge  
- Dictionary-Angriff mit eigener Wortliste  
- Fortschrittsanzeige in Echtzeit für beide Angriffsarten  
- Unterstützt die wichtigsten Hash-Algorithmen  
- Einfach zu bedienen über die Kommandozeile

---

## Voraussetzungen

- Python 3.8 oder höher  
- Das Python-Modul `rich` für Fortschrittsanzeigen, installierbar mit:

pip install rich


---

## Benutzung

### Brute-Force-Angriff

Um einen Brute-Force-Angriff durchzuführen, benutze folgenden Befehl:

python hashcracker.py --hash <Hashwert> --method brute --charset <Zeichensatz> --maxlen <maximale Länge> --algo <Hashalgorithmus>


- `<Hashwert>`: Der Hash, den du knacken willst  
- `<Zeichensatz>`: Zeichensatz für Passwörter (siehe unten)  
- `<maximale Länge>`: Maximale Länge der Passwörter  
- `<Hashalgorithmus>`: z.B. md5, sha1, sha256 oder sha512

### Dictionary-Angriff

Für einen Dictionary-Angriff verwende:

python hashcracker.py --hash <Hashwert> --method dict --wordlist <Pfad zur Wortliste> --algo <Hashalgorithmus>


- `<Pfad zur Wortliste>`: Pfad zu deiner Wortlistendatei

---

## Verfügbare Zeichensätze für Brute-Force

| Code      | Beschreibung                              |
|-----------|-----------------------------------------|
| digits    | Zahlen von 0 bis 9                       |
| lowercase | Kleinbuchstaben a bis z                  |
| uppercase | Großbuchstaben A bis Z                   |
| letters   | Klein- und Großbuchstaben                |
| alphanum  | Buchstaben (klein & groß) und Zahlen    |
| symbols   | Sonderzeichen (z.B. !@#$%^&*)            |
| common    | Buchstaben, Zahlen und ausgewählte Symbole (!@#$_) |
| all       | Alle druckbaren Zeichen inklusive Umlaute (ä, ö, ü, Ä, Ö, Ü, ß) |

---

## Beispielaufruf

Ein Beispiel für Brute-Force mit SHA256-Hash, Zeichensatz „all“ und maximaler Passwortlänge 4:

python hashcracker.py --hash e364c3ae3c983d7db2d6d3733f6a74271eb8c0e55a9d48e7980bb3722155305d --method brute --charset all --maxlen 4 --algo sha256


---

## Lizenz

Dieses Projekt wird unter der MIT-Lizenz veröffentlicht. Das heißt, du darfst den Code frei verwenden, verändern und weitergeben, solange du den Urheber (Mario Madersbacher) nennst und die Lizenz beilegst.

---

## Autor

Mario Madersbacher

---

*Dieses Dokument erklärt das Projekt vollständig und selbstständig, damit du direkt loslegen kannst.*
