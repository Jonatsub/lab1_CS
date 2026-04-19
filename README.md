# Lab 1 - Centraliserad säkerhetsövervakning

Detta repo innehåller mitt arbete för Lab 1 i kursen Nätverks-, OT- och AI-säkerhet.

## Enkel anomalidetektion

Jag gjorde också en enkel del i Python för att få med anomalidetektion i labben.

Jag använde en csv-fil med antal misslyckade SSH-försök per minut. Sedan läste scriptet in filen och letade efter något som stack ut från det normala.

I den slutliga testdatan analyserades 20 minuter. De flesta minuter låg på normala värden mellan 2 och 5 misslyckade försök, medan minut 20 hade värdet 16. Den minuten markerades som en anomali.

Filer:
- data/ssh_attempts.csv
- scripts/anomaly_detector.py
- docs/anomaly-output.txt

Kör så här:
python3 scripts/anomaly_detector.py

Det här är ett enkelt test, men den visar hur anomalidetektion kan användas som komplement till vanliga regler i Wazuh.
