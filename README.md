# Technick Discord Bot

Bei Technik fragen Tech Nick fragen!

## Invite

https://discord.com/api/oauth2/authorize?client_id=1078253643142283264&permissions=2147510272&scope=bot%20applications.commands

## Funktionen

#### Das sind die momentanen Funktionen

/technick

> Schickt ein zufälliges Element aus der Liste "technick". Momentan befinden sich dort nur Werbevideos.

/entscheidung

> Entscheidet zufällig ob etwas "angenickt" oder "angepisst" von Technik ist

/techfakt

> Schickt eine zufällige Zeile aus der Datei "fakt.txt". Dort befinden sich momentan Tech Fakten die ich durch ChatGPT habe. Es kann sein dass sich Fakten wiederholen.

Markierung

> Wenn der Bot markiert wird schickt er eine Sprechblase aus der speechbubble Liste. Er löscht außerdem die Nachricht in der er markiert wurde.

/Geld  

> Gratis Geld Download!

## Dependencies

Der Bot benötigt Python 3.

Außerdem nutzt er [Pycord](https://pycord.dev/) und python-dotenv.

`$ pip install py-cord python-dotenv`

## Setup

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
