# Kontaktliste
- En kontaktliste nettside som består av 1 side med overikt over ulike kontakter, og som trengs brukeren å logge inn for å kunne få tilgang til selve hovedsiden. Det blir brukt programmer som VS Code(Flask, Python, HTML), MariaDB, Hyper-V, og Github.

## For å starte Flask koden

### Oppstart
1. Start MariaDB på Ubuntu VM.
2. Sjekk at brannmuren tilatter port 3306.
3. Start Flask med `python app.py` eller ved VS Code sin egen start knapp.

### Vanlige feil og løsninger
- "Feil brukernavn/passord": Sjekk at SHA-256 hash i databasen matcher.
- "Can't connect to MariaDB": Sjekk IP, bruker og passord i `app.py`.
- "Table doesn't exist": Husk å kjøre SQL-skriptet for å lage tabeller.
