# Arkitektur

## Enkel översikt
Tanken är att labbmiljön ska bestå av:
- Wazuh manager
- Wazuh indexer
- Wazuh dashboard
- Python-kod för enkel anomalidetektion

## Flöde
1. Loggar och händelser samlas in
2. Wazuh analyserar och visar data
3. Python-delen används för att testa AI-baserad avvikelsedetektion
4. Resultat dokumenteras i screenshots och anteckningar
