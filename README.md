# Die Vitalienbrüder und die Hanse

Ein Quellenapparat zu den Vitalienbrüdern und der Hanse, 1389–1401: Wie wird aus einem Kaperbrief ein Verbrechen? Gemeinfreie Quellen im mittelniederdeutschen oder lateinischen Original neben einer neuhochdeutschen Arbeitsübersetzung, eine Zeitleiste mit Verweisen in die Texte, Tafeln und eine Liste dessen, was noch kommt.

Die These, an den Texten zu prüfen: Die Vitalienbrüder kaperten zuerst im Auftrag eines Krieges, für Mecklenburg und das belagerte Stockholm; der Frieden von 1395 machte dieselben Fahrten zu Seeraub. Die Städte der Hanse, Lübeck voran, bekämpften sie mit Friedeschiffen, die sie über einen Pfundzoll bezahlten, und ließen 1400 und 1401 die Gefangenen in Hamburg enthaupten. Die Akten wissen von Störtebeker weniger als die Legende.

Stufe 1 ist in Arbeit. Abgedruckt:

- **Der Flottenbeschluss von Lübeck (3. März 1394)** — Hanserecesse I.4 (Koppmann 1877), Nr. 192, S. 165–172, am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Lindholm 1395 und Stockholm als Pfand** — Hanserecesse I.4, Nr. 261 und 264, S. 248–259, am Seitenbild gelesen, mit Arbeitsübersetzung.

Geplant (siehe `data/modules.json`): der Hansetag vom September 1395 mit Detmar, Gotland 1398, Friedeschiffe und Pfundgeld, Emden 1400, der Vertrag Hollands mit Störtebeker 1400, Helgoland und die Hinrichtungen 1400/01.

Das Begleitspiel *Vitalienbrüder* (https://vitalienbrueder.netlify.app/) spielt den Lübecker Rat.

Online: https://die-vitalienbrueder-und-die-hanse.netlify.app/

## Daten bauen

```
python tools/build-flotte1394.py
python tools/build-lindholm.py
```

## Lokal starten

Ein beliebiger statischer Server, z. B. `python -m http.server 8150`.

Lizenzen: siehe `LICENSES.md`.
