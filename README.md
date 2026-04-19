# Lab 1 - Centraliserad säkerhetsövervakning

Detta repo innehåller mitt arbete med Lab 1 i kursen Nätverks-, OT- och AI-säkerhet.

## Kort om labben

I den här labben har jag försökt bygga upp en enklare förståelse för hur centraliserad säkerhetsövervakning fungerar i praktiken.

Jag är fortfarande ny inom det här området, så mitt fokus har varit att förstå grunderna och få de olika delarna att fungera steg för steg.

## Det jag har gjort

I labben har jag bland annat:

- satt upp Wazuh single-node
- anslutit en agent
- kontrollerat att data kommer in till dashboarden
- testat FIM för att se filändringar
- tittat på några inbyggda SSH-regler i Wazuh
- lagt till en egen lokal regel
- gjort en enkel del i Python för anomalidetektion

## Enkel anomalidetektion

Som en enkel AI-stödd del gjorde jag också ett Python-script som läser in en csv-fil med antal misslyckade SSH-försök per minut.

Tanken var inte att göra något avancerat, utan mer att förstå principen bakom anomalidetektion och se hur ett script kan hitta något som sticker ut från det normala.

I min slutliga testdata analyserades 20 minuter. De flesta minuter låg mellan 2 och 5 misslyckade försök, medan minut 20 hade värdet 16. Den minuten markerades som en anomali.

## Filer

- data/ssh_attempts.csv
- scripts/anomaly_detector.py
- docs/anomaly-output.txt

## Körning

python3 scripts/anomaly_detector.py

## Kort slutsats

Det jag framför allt tar med mig från labben är skillnaden mellan vanlig regelbaserad detektion i Wazuh och enklare anomalidetektion i Python.

Jag känner inte att jag kan allt ännu, men den här labben hjälpte mig att förstå bättre hur de olika delarna hänger ihop.
