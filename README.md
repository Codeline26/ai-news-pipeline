# AI News Pipeline

author: Philipp Weiss

git@ https://github.com/Codeline26/ai-news-pipeline


## Architektur

über die File notebooks/01-analysis.ipynb können die folgenden Funktionen aufgerufen werden:

fn.fetch_news()
- Setzt den API Key aus der .env Datei (nicht inkludiert)
- Gibt ein JSON mit den aktuellen news der NEWSAPI zurück

pp.preprocess(json)
- erwartet ein JSON file
- Entfernt die whitespaces und gibt einen String zurücl

## Fragen

###  Wie hast du die Pipeline modular aufgebaut?
    - mithilfe der 01-analysis.ipynb Datei wurden die einzelen Features zuerst importiert. 
    - Mittels der fetcher Funktion wird ein json abeholt welches mittels der preprocess Funktion verarbeitet wird
    - Der bearbeitete Output wird mittels Funktionsaufruf an das Sentiment model übergeben
    - der Rükcgabewert kann dann mit der Funktion evaluation überprüft werden

###  Welche Komponenten sind austauschbar (z. B. Modell, Datenquelle)?
    - Die API (aktuell newsapi.org)
    - Der preprocessor (wenn nach wie vor ein String übergeben wird)
    - Das verwendete Sentiment Modell
    - Das Evaluierungsmodul

### Wie würdest du die Pipeline erweitern (z. B. Logging, Visualisierung)?
    - Error Handling falls keine Response von der API kommt
    - Speichern des Sentiment Outputs in einer Datenbank
    - Warning Funktion falls die maximalen Requests erreicht werden
