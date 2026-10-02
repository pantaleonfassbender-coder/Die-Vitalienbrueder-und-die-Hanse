"""Baut data/holland.json: Herzog Albrecht von Holland und die Vitalienbrüder, 1400.

Mittelniederländisch: Hanserecesse, 1. Abt., Bd. 4, hg. von Karl Koppmann (Leipzig 1877), Nr. 605 (15. August 1400) und
Nr. 606 (11. November 1400), S. 552–553, nach dem Memoriale B. M. 1396–1401 im Staatsarchiv Den Haag.
Internet Archive hanserecesse12roppgoog, Blatt = Seite + 41. Am Seitenbild gelesen.
Übersetzung: eigene Arbeitsübersetzung (CC0).
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "holland.json"

VERTRAG = [
    dict(n=1, titel="Johan Stortebeker und 113 andere", pg="HR I.4 S. 552",
         orig="Aelbrecht etc. doen cond allen luden, dat wii een voerwaerde gedadingt ende gemaect hebben mit Herman Haweupe, Johan Stortebeker, Hinrich Corte, Jan Velhove, Otte Rover, Tiderich Hogezee, Yesse Dene ende Gůdemont Janneszon van hore gemeenre vitaelgebroedere wegen tot hondert ende 14 manne toe, ende die bescreven over te leveren in deser manieren, dat wii se tot onser vriensscap nemen ende gheven him luden een goet, vry, vaste ende zeker geleide, vrylich te comen, te varen, te marren, te keren ende te wesen overal in onsen landen, so waer dats him gevoecht.",
         en="Albrecht usw. tun allen Leuten kund, dass wir einen Vertrag verhandelt und gemacht haben mit Hermann Haweupe, Johan Stortebeker, Hinrich Corte, Jan Velhove, Otte Rover, Tiderich Hogezee, Yesse Dene und Gudemont Janszoon, im Namen ihrer gemeinen Vitalienbrüder, bis zu hundertundvierzehn Mann, und die Liste schriftlich zu übergeben, in dieser Weise: dass wir sie in unsere Freundschaft nehmen und ihnen ein gutes, freies, festes und sicheres Geleit geben, frei zu kommen, zu fahren, zu verweilen, zu kehren und zu sein überall in unseren Landen, wo es ihnen passt.",
         note="Ausgestellt von Albrecht, Herzog von Bayern und Graf von Holland, Seeland und Hennegau, der seit 1396 Krieg um Friesland führte. Der Text steht in einem Registerband seiner Kanzlei, nicht als Original. Unter den acht Wortführern steht ‚Johan Stortebeker‘: Hier ist der Name, den die Chroniken später mit ‚Klaus‘ verbinden, in einer Urkunde greifbar, an zweiter Stelle einer Liste, als einer von acht Vertretern einer Genossenschaft von 114 Mann. Die Vitalienbrüder handeln als Körperschaft: ‚van hore gemeenre vitaelgebroedere wegen‘."),
    dict(n=2, titel="Feinde unserer Feinde", pg="HR I.4 S. 552",
         orig="Voert so sullen dese voersc[reven] vitaelgebroeders vyant wesen alle der geenre, die onse vyande siin, dats te verstaen: die Oestvriesen van Westergo ende van Oestergo toter Lauwers toe, dier van Grůeningen, dier van Hamborch ende anders die ghene die over die Lauwers geseten siin, ende wii mit recht veeden mogen. Ende wat gevangen, scepe of enigerhande goede dese voers[eiden] vitaelgebroeders in den onsen brengen sullen, die sullen sii vriliken daer gebruken ende voeren daer sii willen ende daer of beschermt wesen, up dat zi se up onse vyande voergen[ompt] genomen hebben. Voert so en sullen sii van ons noch van onsen ondersaten niet vervolcht noch bescadicht werden, sii en sullen eerst in der zee up horen vryen wege wesen.",
         en="Ferner sollen diese genannten Vitalienbrüder Feinde all derer sein, die unsere Feinde sind, das heißt: der Friesen von Westergo und von Oostergo bis an die Lauwers, derer von Groningen, derer von Hamburg und sonst derer, die jenseits der Lauwers sitzen und die wir mit Recht befehden dürfen. Und was diese genannten Vitalienbrüder an Gefangenen, Schiffen oder irgendwelchem Gut in das Unsere bringen werden, das sollen sie dort frei gebrauchen und führen, wohin sie wollen, und darin geschützt sein, sofern sie es unseren genannten Feinden genommen haben. Ferner sollen sie von uns und unseren Untertanen nicht verfolgt noch geschädigt werden, bevor sie wieder auf See auf ihrem freien Weg sind.",
         note="Das ist ein Kaperbrief: Der Fürst nimmt die Vitalienbrüder in Dienst gegen seine Feinde und garantiert, dass ihre Beute in seinen Häfen frei verkauft werden darf. Unter den Feinden steht Hamburg, das im Frühjahr mit Lübeck die Vitalienbrüder in der Ems geschlagen hatte (Emden 1400 Kampf). Dieselben Männer, die Hamburg als Seeräuber richtet, sind für Holland rechtmäßige Kriegsleute, solange sie nur Friesen, Groninger und Hamburger berauben. Die Lauwers ist der Grenzfluss zwischen dem westlichen Friesland und dem Groninger Land."),
    dict(n=3, titel="Ein Vierteljahr und vierzehn Tage Kündigung", pg="HR I.4 S. 552",
         orig="Dese voers[creven] voerwaerden sullen ingaen upten date des briefs ende gedueren een quart[al] jaers daer naest volgende ende darentenden 14 dage lang na onsen wederseggen, dat wii den voers[eiden] vitaelgebroeders mit onsen brieven wederseggen sullen ende te weten laten, ende alle ding sonder argelist. Ende om dat wii den selven vitaelgebroeders geloeft hebben ende geloven mit desen brieven te houden ende te doen houden alle pointen ende voervaerden, geliic voerscreven is, soe hebben wii in getugenisse daer of desen brief doen besegelen mit onsen segel hier aen gehangen. Ende hebben om die meerre zekerheit willen bevolen onsen get[r]ůwen, den here van Vrederode, den here van Wassenaer, heren Gheriit van Egmonde ende heren Ghiiskiin van Diepenborch, dat sii desen brief mit ons besegelen. […] Gegeven tot Harlem up onser v[r]ůwen dach assumpcio anno 1400.",
         en="Dieser genannte Vertrag soll mit dem Datum des Briefes beginnen und ein Vierteljahr danach dauern, und am Ende noch vierzehn Tage lang nach unserer Aufkündigung, die wir den genannten Vitalienbrüdern mit unseren Briefen aufkündigen und wissen lassen werden, und alles ohne Arglist. Und weil wir denselben Vitalienbrüdern gelobt haben und mit diesem Brief geloben, alle Punkte und Vereinbarungen zu halten und halten zu lassen, wie vorgeschrieben ist, haben wir zum Zeugnis dessen diesen Brief mit unserem hier angehängten Siegel besiegeln lassen. Und um größerer Sicherheit willen haben wir unseren Getreuen, dem Herrn von Brederode, dem Herrn von Wassenaar, Herrn Gerrit van Egmond und Herrn Gijskijn van Diepenborch, befohlen, dass sie diesen Brief mit uns besiegeln. […] Gegeben zu Haarlem an Unser Frauen Himmelfahrt im Jahr 1400.",
         note="15. August 1400. Ein Vertrag auf Zeit, drei Monate, kündbar mit vierzehn Tagen Frist: Der Fürst mietet eine Flotte. Vier Ritter des holländischen Adels siegeln mit, darunter die Herren von Brederode und Wassenaar. Ausgelassen ist ihre Siegelformel. Drei Monate später verlängert Albrecht das Geleit für eine andere Gruppe (Holland 1400 Staveren [1]). Ein Jahr danach werden in Hamburg Vitalienbrüder enthauptet, und die Hamburger Chronik nennt unter ihnen einen Störtebeker."),
]

STAVEREN = [
    dict(n=1, titel="Hundertfünfzig beim Grafen von Oldenburg", pg="HR I.4 S. 552–553",
         orig="Aelbrecht etc. doen cond allen luden, dat wii genomen hebben ende nemen mit desen brieve den vitaelgebroders, die op desen tiit siin bi den grave van Oldenburch of dair omtrent tot anderhalf hondert persoenen toe in onser sunderlinge beschermenisse, ende gheven him allen een goed, vry, vast ende zeker gheleide veilich te varen, te comen, te merren, te keren over al in onsen landen ende in onser stat van Staveren mit horen scepen ende goeden om te bescadigen onse vyande, dat is te verstaen: die Oestvriesen van Oestergoe ende van Westergoe, die van Groeningen, die van Hamborch ende anders die ghene, die over die Lauwers geseten siin ende wii mit rechte veeden moghen. Dit sal gedueren een maent lang na onsen wederseggen. In oirconde desen brief ende onse segel hier op gedruct. Gegeven in den Hage op sinte Martiins dach in den winter anno 1400.",
         en="Albrecht usw. tun allen Leuten kund, dass wir die Vitalienbrüder, die zu dieser Zeit beim Grafen von Oldenburg oder dort in der Nähe sind, bis zu anderthalbhundert Personen, mit diesem Brief in unseren besonderen Schutz genommen haben und nehmen, und geben ihnen allen ein gutes, freies, festes und sicheres Geleit, sicher zu fahren, zu kommen, zu verweilen und zu kehren überall in unseren Landen und in unserer Stadt Stavoren, mit ihren Schiffen und Gütern, um unsere Feinde zu schädigen, das heißt: die Friesen von Oostergo und von Westergo, die von Groningen, die von Hamburg und sonst die, die jenseits der Lauwers sitzen und die wir mit Recht befehden dürfen. Dies soll einen Monat lang nach unserer Aufkündigung dauern. Zur Urkunde dieser Brief und unser Siegel hier aufgedrückt. Gegeben im Haag an St. Martins Tag im Winter im Jahr 1400.",
         note="11. November 1400. Die Vitalienbrüder liegen jetzt beim Grafen von Oldenburg, dessen Bastard im Mai in Emden enthauptet worden war (Emden 1400 Kampf [3]). Albrecht gibt ihnen Stavoren an der Zuiderzee als Stützpunkt. Ein halbes Jahr nach dem Zug der Städte in die Ems haben die Vitalienbrüder einen neuen Herrn, einen neuen Hafen und denselben Feind: Hamburg."),
]

doc = {
    "id": "holland",
    "titel": "Der Vertrag Hollands mit Störtebeker, 1400",
    "autor": "Albrecht, Herzog von Bayern, Graf von Holland, Seeland und Hennegau",
    "jahr": "1400",
    "sprache": "de",
    "orig_sprache": "dum",
    "pg_label": "",
    "quelle": "Hanserecesse. Die Recesse und andere Akten der Hansetage von 1256–1430, Bd. 4, bearb. von Karl Koppmann (Leipzig 1877), Nr. 605 (15. August 1400) und Nr. 606 (11. November 1400), S. 552–553, nach dem Memoriale B. M. 1396–1401 im Staatsarchiv Den Haag (Internet Archive: hanserecesse12roppgoog). Übersetzung: eigene Arbeitsübersetzung.",
    "hinweis": "Zwei Einträge aus dem Registerband der holländischen Kanzlei. Im August 1400 nimmt Herzog Albrecht 114 Vitalienbrüder in seine Freundschaft, unter ihren Wortführern Johan Stortebeker, und gibt ihnen Geleit und das Recht, seine Feinde zu berauben, darunter Hamburg; im November nimmt er 150 weitere in Schutz und gibt ihnen Stavoren als Hafen. Was für die Städte Seeraub war, ist hier ein Dienstvertrag. Mittelniederländisch, am Seitenbild gelesen.",
    "sections": [
        {"id": "vertrag", "titel": "Der Vertrag vom 15. August", "zk": "Holland 1400 Vertrag",
         "blurb": "Acht Wortführer für 114 Mann, unter ihnen Johan Stortebeker: Freundschaft, Geleit, freie Beute gegen Friesen, Groninger und Hamburger, für ein Vierteljahr.",
         "units": VERTRAG},
        {"id": "staveren", "titel": "Stavoren", "zk": "Holland 1400 Staveren",
         "blurb": "November 1400: 150 Vitalienbrüder beim Grafen von Oldenburg kommen in den Schutz des Herzogs und bekommen Stavoren als Hafen.",
         "units": STAVEREN},
    ],
}

OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("holland.json:", sum(len(s["units"]) for s in doc["sections"]), "Einheiten")
