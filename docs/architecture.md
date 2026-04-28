# Arkitektur

## Syfte

Tanken med den här labben har varit att bygga upp en enkel miljö för centraliserad säkerhetsövervakning och samtidigt försöka förstå hur delarna hänger ihop i praktiken.

## Delar i miljön

Det här är delarna jag har använt i labben:

- Wazuh agent
  Kör på min Ubuntu/WSL-miljö och skickar in händelser och loggar.

- Wazuh manager
  Tar emot data från agenten och analyserar det med regler.

- Wazuh indexer
  Lagrar datan så att den går att söka fram i Wazuh.

- Wazuh dashboard
  Visar agentstatus, events, FIM och annan information i webbläsaren.

- Python-del för anomalidetektion
  Läser testdata från csv och markerar sådant som sticker ut.

## Enkel nätverksöversikt

Ubuntu / WSL med Wazuh agent
          |
          v
     Wazuh manager
          |
          v
     Wazuh indexer
          |
          v
    Wazuh dashboard

Separat del:
Python-skript -> läser csv -> markerar avvikelser -> skriver output

## Dataflöde

1. Något händer i den övervakade miljön.
2. Wazuh agent samlar in loggar och filhändelser.
3. Agenten skickar datan vidare till Wazuh manager.
4. Wazuh manager analyserar datan med regler.
5. Datan lagras i Wazuh indexer.
6. Resultatet går att se i Wazuh dashboard.
7. Python-delen används separat för att testa enkel anomalidetektion.

## Regler

I labben har jag arbetat både med standardregler och egna lokala regler.

Standardregler som jag utgått från:
- 5710 - invalid user i SSH
- 5716 - failed password i SSH

Egna lokala regler:
- 100001 - SSH authentication failed från en specifik IP
- 100002 - flera invalid user-försök från samma IP inom viss tid
- 100003 - flera failed password-försök från samma IP inom viss tid

## FIM

FIM användes för att övervaka filändringar och se att Wazuh kunde upptäcka när filer ändrades.

Detta verifierades i dashboarden genom både översikt och enskilda events.

## Active response

Jag har konfigurerat en active response med:

- firewall-drop
- regel-ID 100003
- timeout 60

Tanken är att det ska fungera som en enkel automatisk åtgärd vid upprepade misslyckade SSH-försök från samma IP.

## Python-del

Python-delen är tänkt som ett enkelt exempel och inte som någon avancerad AI-lösning.

Den består av:
- data/ssh_attempts.csv
- scripts/anomaly_detector.py
- docs/anomaly-output.txt

I testdatan analyseras 20 minuter med misslyckade SSH-försök, där minut 20 sticker ut med värdet 16 och markeras som en anomali.

## Kort sammanfattning

Min labb bygger på att Wazuh står för den regelbaserade och centraliserade övervakningen, medan Python-delen används som ett enkelt komplement för att visa skillnaden mellan vanliga regler och anomalidetektion.
