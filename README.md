# Technick Discord Bot

Bei Technik fragen Tech Nick fragen!

# Funktionen

### Momentan gibt es 3 Funktionen

`/technick`
Schickt ein zufälliges Element aus der Liste "technick". Momentan befinden sich dort nur Werbevideos.
`/abgenickt`
Entscheidet zufällig ob etwas "angenickt" oder "angepisst" von Technik ist
`/techfakt`
Schickt eine zufällige Zeile aus der Datei "fakt.txt". Dort befinden sich momentan Tech Fakten die ich durch ChatGPT habe. Es kann sein dass sich Fakten wiederholen.

# Dependencies

Der Bot benötigt Python 3.

Außerdem nutzt er [Pycord](https://pycord.dev/).
`$ pip install py-cord`

# Setup

Aus Sicherheitsgründen erwartet der Bot den Token in einer .env datei
Füge in DEINDISCORDTOKEN den Token von deinen Discord Bot ein
Beispiel unter Linux:
`$ echo ""TOKEN" = DEINDISCORDTOKEN" > .env`

Oder einfach in eine .env datei folgendes reinschreiben:

> "TOKEN" = DEINDISCORDTOKEN

Um den Bot zu starten:

`$ python main.py`
Oder
`$ python3 main.py`
