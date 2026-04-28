# Lab 1 - Centraliserad säkerhetsövervakning

Detta repo innehåller mitt arbete med Lab 1 i kursen Nätverks-, OT- och AI-säkerhet.

## Kort om labben

I den här labben har jag försökt förstå hur centraliserad säkerhetsövervakning fungerar i praktiken.

Jag är ny inom det här, så jag har tagit det steg för steg och fokuserat på att få saker att fungera först och sen försöka förstå vad som händer.

## Det jag har gjort

I labben har jag:

- satt upp Wazuh single-node
- anslutit en agent
- kollat att data kommer in i dashboarden
- testat FIM för att se filändringar
- kollat några SSH-regler i Wazuh
- lagt till en egen lokal regel
- gjort en enkel Python-del för anomalidetektion

## Enkel anomalidetektion

Jag gjorde ett enkelt Python-script som läser en csv-fil med misslyckade SSH-försök per minut.

Tanken var mest att testa och förstå hur anomalidetektion funkar, inte att bygga något avancerat.

I min testdata hade jag 20 minuter där de flesta låg mellan 2-5 försök, och en minut stack ut med 16. Den blev markerad som en anomali.

## Filer

- data/ssh_attempts.csv  
- scripts/anomaly_detector.py  
- docs/anomaly-output.txt  

## Körning

python3 scripts/anomaly_detector.py

## Kort slutsats

Det jag främst har förstått är skillnaden mellan regelbaserad detektion i Wazuh och enklare anomalidetektion i Python.

Jag är fortfarande i början av att lära mig detta, men jag börjar få en bättre bild av hur delarna hänger ihop.

## Arbetslogg

Jag började med att få igång Wazuh single-node och dashboarden. När det fungerade gick jag vidare med agenten i min WSL-miljö och kontrollerade att den dök upp som active i Wazuh.

Efter det testade jag FIM. Jag skapade en egen testmapp och ändrade i en fil för att se om Wazuh märkte förändringen. Först fungerade det inte direkt som jag trodde, men efter felsökning förstod jag att realtime behövdes för att ändringen skulle synas snabbare.

Sedan kollade jag på några av Wazuhs färdiga SSH-regler. Det hjälpte mig att förstå att Wazuh inte bara ser saker, utan att den matchar loggar mot regler. Efter det skapade jag en egen lokal regel, 100002, som jag testade med wazuh-logtest.

Jag gjorde också en enkel Python-del med IsolationForest. Den delen är inte avancerad, men den hjälpte mig att förstå skillnaden mellan en vanlig regel och en enklare anomalidetektion. Regeln letar efter något bestämt, medan anomalidelen försöker hitta något som sticker ut från det normala.

Mot slutet skapade jag en enkel dashboard och tog screenshots på de viktigaste delarna: agenten, FIM, den lokala regeln, Python-output och dashboarden.
