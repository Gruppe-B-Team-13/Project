# Projektarbeit

## Mitglieder

- Ramiro Gonzalez  
- Marc Stöcklin  
- Jan Wirz  

## Dokumentation
Projektarbeit
Projektarbeit Anwendungsentwicklung in Python - Hotel Reservation

Mitglieder
Ramiro Gonzalez
Marc Stöcklin
Jan Wirz
Projektdokumentation · Hotel-Reservations-System
1 · Ziel & Umfang
Wir entwickeln ein modular aufgebautes Hotel-Reservations-System in Python, das den gesamten Buchungsprozess – von der Suche nach freien Zimmern bis zur Rechnung – abbildet.
Der minimale Funktionsumfang richtet sich nach unseren Must-Have-User-Stories; optionale Stories fliessen ein, sobald Kernfunktionen stabil laufen.

2 · Systemarchitektur
Schicht	Zweck	Unsere Umsetzung
Model	Abbild der Domäne als reine Python-Objekte	Klassen Hotel, Room, Booking, Invoice usw.
Data Access Layer (DAL)	Kapselt sämtliche SQL-Befehle	Pro Entität eine eigene DAL-Klasse auf Basis BaseDataAccess
Business Logic (Manager)	Regelt Workflows & Regeln	Manager-Klassen berechnen Saisonpreise, koordinieren Buchung ↔ Rechnung, prüfen Eingaben.
Alle Schichten sind lose gekoppelt und via Unit-Tests isoliert prüfbar.

3 · Datenbank & ER-Modell
10 Tabellen (u. a. Hotel, Room, Booking, Invoice).
1:n Beziehungen für Hotel→Room, Guest→Booking; n:m Beziehung Room↔Facilities über Room_Facilities.
is_cancelled ersetzt hartes Löschen von Buchungen, damit Historie erhalten bleibt.
Das vollständige Diagramm liegt als Hotel_Reservation_ERM.jpg im Repo.

4 · User-Stories & Akzeptanzkriterien (Kurzfassung)
Epic	Kern-Stories
Hotel-Suche	Stadt, Sterne, Zeitraum, Kapazität filtern; Ergebnis paginiert.
Zimmerdetails	Freie Zimmer mit Preis & Ausstattung anzeigen.
Buchung	Zimmer buchen, Saisonpreis anwenden, Rechnung generieren, Buchung stornieren.
Admin-CRUD	Hotels, Zimmer, Facilities, RoomTypes anlegen, bearbeiten, löschen.
Reporting	Belegungsraten & Durchschnittsbewertung je Hotel (Review-View geplant).
5 · Zeitplan (März – Anfang Juni)
Phase	Outcomes
Kick-off & Analyse	ER-Modell, Tech-Stack fixiert
Model-Klassen	Alle Domänenobjekte inkl. Tests fertig
DAL-Grundgerüst	BaseDataAccess, CRUD für Address, Hotel, Room
Business-Logic I	Preisfunktion, Booking-Workflow, Invoice-Erzeugung
Business-Logic II	Admin-CRUD, Storno-Logik, Saisonpreis UI-Hook
User Stories	User-Stories final
Integration & QA	Testabdeckung, Performance
Dokumentation & Freeze	README, API-Spec, Demo-Video,
Puffer: Eine Woche Reserve für unerwartete Bugs oder Review-Änderungen.

6 · Team & Rollen
Name	Hauptverantwortung	Nebentätigkeit
Jan	Datenmodell, ER-Diagramm, Address / Hotel / Room DAL	Datenmigrationen
Marc	Business-Logic (Booking, Room, Price)	
Ramiro	Teststrategie	Dokumentation,
Alle drei übernehmen abwechselnd Code-Reviews und User-Stories.

7 · Zusammenarbeit, Kommunikation & Information
Bereich	Tool / Praxis
Task-Tracking	GitHub Projects; Spalten Backlog → In Progress → Code Review → Done
Chat & Meetings	Teams-Chat, Whatsapp, Vorlesung(Coaching)
Dokumentation	Markdown-Dateien im Repo; anschliessend in README übertragen
Fazit: Dank klarer Rollen, regelmässiger Kommunikation und sauberer Schichtentrennung erreichen wir Anfang Juni einen stabilen Release-Kandidaten, der alle Must-Have-Stories erfüllt und erweiterbar bleibt.



## User Stories
### Minimale User Stories

1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind:   
    1.1. Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.  
    1.2. Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.  
    1.3. Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).  
    1.4. Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.  
    1.5. Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.  
    1.6. Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.  

2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.  
    2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.  
    2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.  

3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.  
    3.1. Ich möchte neue Hotels zum System hinzufügen  
    3.2. Ich möchte Hotels aus dem System entfernen  
    3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.  

4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.

5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.

7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.

8. Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.

9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.

10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat. 3 Hint: Stammdaten sind alle Daten, die nicht von anderen Daten abhängen.

### User Stories mit DB-Schemaänderung

_mindestens zwei der folgenden User Stories_

1. Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer).

2. Als Gast möchte ich auf meine Buchungshistorie zuzugreifen ("lesen"), damit ich meine kommenden Reservierungen verwalten kann.  
    2.1. Die Anwendungsfälle für meine Buchungen sind "neu/erstellen", "ändern/aktualisieren", "stornieren/löschen".

3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.

4. Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

5. Als Gast möchte ich für jeden Aufenthalt Treuepunkte sammeln, die ich dann für Ermässigungen einlösen kann. Hint: Nur häufige Gäste sollten Treuepunkte erhalten. Definieren Sie eine Regel, um häufige Gäste zu identifizieren.

6. Als Gast möchte ich meine Buchung mit der von mir bevorzugten Zahlungsmethode bezahlen, damit ich meine Reservierung abschliessen kann.

### User Stories mit Datenvisualisierung

_eine der folgenden User Stories_

1. Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann. Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z. B. wie oft jeder Zimmertyp gebucht wird).  

2. Als Admin möchte ich eine Aufschlüsselung der demografischen Merkmale meiner Gäste sehen, damit ich gezieltes Marketing planen kann. Hint: Wählt ein geeignetes Diagramm, um die Verteilung der Gäste nach verschiedenen Merkmalen darzustellen (z. B. Altersspanne, Nationalität, wiederkehrende Gäste). Möglicherweise müssen Sie der Tabelle „Gäste“ einige Spalten hinzufügen.

### Optionale User Stories

1. Als Admin möchte ich die Gesamteinnahmen meines Hotels sehen, damit ich die finanzielle Leistung des Hotels analysieren kann. 
    1.1. Zeigt die Gesamteinnahmen (Revenue) an, die sich aus allen Buchungen für einen bestimmten Zeitraum ergeben. 
    1.2. Eine zeitliche Aufschlüsselung (z. B. Umsatz nach Monat, Quartal, Jahr) bereitstellen. Hint: Füge eine Trendlinie ein, um zu veranschaulichen, wie sich die Einnahmen im Laufe der Zeit verändern.

2. Als Gastnutzer möchte ich die Details meiner Reservierung in einer lesbaren Form erhalten (z.B. die Reservierung in einer dauerhaften Datei speichern), damit ich meine Buchung später überprüfen kann. Hint: Erzeugt eine «booking.txt»-Datei oder verwendet die Python-Bibliothek «fpdf» oder eine ähnliche Library, um eine PDF-Version zu erzeugen.

3. Als Gastnutzer möchte ich eine Karte mit Zoom- und Filterfunktion sehen können, welche Sehenswürdigkeiten oder Restaurants in der Nähe meines gebuchten Hotels liegen, um meine Aufenthaltsplanung zu erleichtern. Hint: Verwende die Python-Bibliothek «geopandas» oder eine ähnliche.

4. Als Gastnutzer möchte ich ein Zimmer buchen und eine Buchungsbestätigung mit allen Details per E-Mail erhalten, um einen verbindlichen Nachweis meiner Reservierung zu haben. Hint: Verwende die Python-Bibliothek «smtplib» oder eine ähnliche.
