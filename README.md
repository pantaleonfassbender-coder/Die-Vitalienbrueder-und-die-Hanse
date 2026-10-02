# Die Vitalienbrüder und die Hanse

Ein Quellenapparat zu den Vitalienbrüdern und der Hanse, 1389–1401: Wie wird aus einem Kaperbrief ein Verbrechen? Gemeinfreie Quellen im mittelniederdeutschen oder lateinischen Original neben einer neuhochdeutschen Arbeitsübersetzung, eine Zeitleiste mit Verweisen in die Texte, Tafeln und eine Liste dessen, was noch kommt.

Die These, an den Texten zu prüfen: Die Vitalienbrüder kaperten zuerst im Auftrag eines Krieges, für Mecklenburg und das belagerte Stockholm; der Frieden von 1395 machte dieselben Fahrten zu Seeraub. Die Städte der Hanse, Lübeck voran, bekämpften sie mit Friedeschiffen, die sie über einen Pfundzoll bezahlten, und ließen 1400 und 1401 die Gefangenen in Hamburg enthaupten. Die Akten wissen von Störtebeker weniger als die Legende.

Stufe 1 ist in Arbeit. Abgedruckt:

- **Der Flottenbeschluss von Lübeck (3. März 1394)** — Hanserecesse I.4 (Koppmann 1877), Nr. 192, S. 165–172, am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Lindholm 1395 und Stockholm als Pfand** — Hanserecesse I.4, Nr. 261 und 264, S. 248–259, am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Der Lübecker Hansetag vom September 1395, mit Detmar** — Hanserecesse I.4, Nr. 308 und 309, S. 303–306; Detmar-Chronik, Chroniken der deutschen Städte 26 (Koppmann 1899), §§ 974–975, 1009, 1019; am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Gotland 1398: der Deutsche Orden nimmt Visby** — Hanserecesse I.4, Nr. 434, 436–438, S. 412–417; Scriptores rerum Prussicarum III (1866), S. 217–218 (Thorner Annalen, Posilge); Detmar-Fortsetzung §§ 1061–1063; am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Friedeschiffe und Pfundgeld, 1398–1399** — Hanserecesse I.4, Nr. 441, 513, 525, 536, 656; am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Emden 1400: der Zug der Städte nach Ostfriesland** — Hanserecesse I.4, Nr. 591 und 602, S. 538–550; am Seitenbild gelesen, mit Arbeitsübersetzung.
- **Der Vertrag Hollands mit Störtebeker, 1400** — Hanserecesse I.4, Nr. 605 und 606, S. 552–553 (mittelniederländisch); am Seitenbild gelesen, mit Arbeitsübersetzung.

Sechzehn Tafeln: Schedels Lübeck (1493), das Elbinger Koggensiegel (1350), das Siegel Konrads von Jungingen (1404), Gotland auf der Carta marina (1539), Emden und Stavoren bei Braun und Hogenberg, Stöwers hansische Schiffe (1902), acht Editionsseiten und eine Karte der Orte.

Geplant (siehe `data/modules.json`): Helgoland und die Hinrichtungen 1400/01.

Das Begleitspiel *Vitalienbrüder* (https://vitalienbrueder.netlify.app/) spielt den Lübecker Rat.

Online: https://die-vitalienbrueder-und-die-hanse.netlify.app/

## Daten bauen

```
python tools/build-flotte1394.py
python tools/build-lindholm.py
python tools/build-luebeck1395.py
python tools/build-gotland.py
python tools/build-pfundgeld.py
python tools/build-emden.py
python tools/build-holland.py
python tools/build-plates.py
```

## Lokal starten

Ein beliebiger statischer Server, z. B. `python -m http.server 8150`.

Lizenzen: siehe `LICENSES.md`.
