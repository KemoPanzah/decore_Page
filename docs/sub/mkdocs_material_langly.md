---
title: MkDocs Material Langly Plugin
keywords: mkdocs, material, langly, plugin, language, translation, deepl, multilingual, internationalization, localization
---

# MkDocs Material Langly Plugin

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/P5P2JCC5B){:target="_blank"}

[[Das Langly-Plugin für MkDocs ist ein Plugin, das Sprachunterstützung und Übersetzungen für Webseiten bietet, die mit MkDocs in Verwendung des Material-Themes erstellt wurden. Es ermöglicht die einfache Verwaltung mehrsprachiger Inhalte und die automatische Übersetzung von Texten, um eine breitere Zielgruppe zu erreichen. Es erfüllt bewusst keine der derzeitigen Übersetzungsstandards, sondern geht einen ganz eigenen aber offenen Weg.]]

[[Dieses Plugin wurde für Verwendung des großartigen Material-Themes erstellt und bietet Funktionalitäten um z.B. auch den Blogbereich zu Internationalisieren.]]

[[**Die derzeit einzige Übersetzungsengine ist Deepl und es wird ein DeepL-Api-Key benötigt, um das Plugin zu verwenden.**]]

## [[Direkte unterstütze Plugins für mkdocs]] ##

[[Diese Auflistung sind Plugins, die bei der Entwicklung von Langly direkt verwendet wurden und als kompatibel gelten.]]
[[**Aber es ist nicht ausgeschlossen, dass auch andere Plugins funktionieren.**]]

- [mkdocs-material](https://squidfunk.github.io/mkdocs-material){:target="_blank"}
- [mkdocs-strings](https://mkdocstrings.github.io){:target="_blank"}
- [mkdocs-glightbox](https://github.com/blueswen/mkdocs-glightbox){:target="_blank"}

[[Diese großartigen Plugins benötigen definitiv volle Unterstützung und Anerkennung.]]

!!! note
    [[Das Plugin ist noch in der Entwicklung und es wird empfohlen, die Dokumentation zu lesen, um die Funktionalitäten und Einschränkungen zu verstehen. Ich bitte auch alle Anforderungen und Änderungsvorschläge in den GitHub-Issues zu melden.]]

## [[Lasst uns Anfangen]]

[[Für den Anfang werden ein paar vorläufige Schritte benötigt, um das Plugin zu benutzen.]]

- [x] [[mkdocs mit installiertem Material-Theme]]
- [x] [[Ein DeepL-Free-Account wird benötigt]]

### [[Installation des Plugins]]

[[Um das Plugin zu verwenden, müssen Sie es zuerst installieren. Führen Sie dazu den folgenden Befehl aus:]]

```bash
pip install mkdocs-material-langly
```

### [[Api-Key bereitstellen]]

[[Um das Plugin zu verwenden, benötigen Sie einen Deepl-Api-Key. Sie können diesen kostenlosen von der Deepl-Website erhalten.]]

[[Nachdem Sie den Api-Key erstellt haben, erstellen Sie eine Datei namens `auth_key.json` im Wurzelverzeichnis Ihres Projekts und fügen folgenden Inhalt ein:]]

```json
  {
      "deepl": "DEEPL-API-KEY"
  }

```

[[Ersetzen Sie `DEEPL-API-KEY` durch Ihren eigenen Api-Key.]]

### [[Api-Key schützen]]

!!! danger
    [[Bitte lesen Sie diesen Abschnitt sorgfältig durch und beachten Sie den Api-Key in der .gitignore auszuschließen und auch auf jede erdenkliche Weise vor dem Upload ins Internet zu schützen.]]

[[Öffnen Sie die Datei .gitignore im Wurzelverzeichnis und fügen Sie die Zeile `auth_key.json` hinzu, um zu verhindern das die Datei versehentlich hochgeladen wird. Anschließend bitte auch online prüfen, dass der Key nicht im Repo zu finden ist.]]

### [[Konfiguration des Plugins]]

[[Nach der Installation können Sie das Plugin in Ihrer `mkdocs.yml`-Konfigurationsdatei aktivieren. **Langly sollte dabei als letztes Plugin in der Liste stehen**.]]

!!! info
    [[Es müssen keine sprachbezogenen Einstellungen am Material-Theme vorgenommen werden. Das bedeutet das die Optionen `theme>language` und `extra>alternate` durch das Plugin gesetzt werden.]]

```yaml
site_url: https://<example>.com
..
..
..
plugins:
  - search
  - .
  - .
  - langly:
      lang_switch: true
      source:
          name: Deutsch
          lang: de
      targets:
        - name: English
          lang: en-us

```

[[In dieser Konfiguration wird die Sprache Deutsch als Quellsprache und Englisch als Zielsprache festgelegt. Sie können beliebig viele Zielsprachen hinzufügen. Allerdings beeinträchtigt das die `serve` Performance um so mehr. Die Option  `site_url` sollte der Veröffentlichungsadresse Ihrer Website entsprechen damit die `sitemap` und `canonicals` korrekt funktionieren.]]

!!! warning
    [[Wichtig ist dabei die Deepl-Language-Codes für `source` und `target` zu verwenden. Diese sind auf folgender Website zu finden:]] [Deepl Language Codes](https://developers.deepl.com/docs/resources/supported-languages){:target="_blank"}

[[Nachdem Sie die Konfiguration vorgenommen haben, können Sie die Übersetzungsfunktionen in Ihren Markdown-Dateien verwenden.]]

### [[Verwendung des Plugins]]

[[Das Plugin analysiert Markdown-Texte und wertet maskierte Textpassagen aus, die mit `{[` und `]}` umschlossen sind. Diese `delimiter` werden beim Rendern der Seite entfernt und Quell sowie Zielsprache werden korrekt auf Ihrer Seite dargestellt.]] 

[[Gehen sie wie folgt vor, um Texte zu maskieren]]

`{[`[[Ihr Text]]`]}`

[[Der Text innerhalb der Maskierung wird dann von Langly automatisch übersetzt.]]

### [[Ein paar einfache Beispiele]]

#### [[Satz]]

`{[`[[Dieser Text repräsentiert Ihre Quellsprache]]`]}`

#### [[Absatz]]

`{[`[[Dieser Absatz enthält mehrere Sätze in Ihrer Quellsprache. Es ist die empfohlene Art der Maskierung von Textpassagen und liefert Deepl mehr Kontext um eine bessere Übersetzung zu liefern.]]`]}`
#### [[Aufzählung mit Doppelpunkt]]

- `{[`[[Aufzählung]]`]}`**:**`{[`[[Wert nach dem Doppelpunkt]]`]}`

## Changelog und Features

### 0.1.3

- [[Da kommt bald was...]]

### 0.1.2

- [[Da der Algorithmus die Zeichen `{[` und `]}` als Maskierung für übersetzbaren Text verwendet, können diese Zeichen nicht direkt im Text dokumentiert werden. Stattdessen werden `hints` verwendet, die nach der Übersetzung automatisch in `{[` und `]}` umgewandelt werden.]]
- [[Markdown Export beim ersten durchlauf von `serve`, `build` oder `gh-deploy` für angegebene Seiten und Sprachen mit definiertem Pfad.]]
- [[Änderung zu pyproject.toml]]

### 0.1.1 - Initial Release
  
- [[Einfügen einer "index.html" mit Umleitung zur Zielsprache nach Browsersprache.]]
- [[Konfigurieren Sie MKDocs und das Materialthema für jedes Build in der jeweiligen Sprache.]]
- [[Optionale Sprachumschaltung, die automatisch konfiguriert wird.]]
- [[Setzen aller offenen Übersetzungen während `serve` in den Draft-Mode, um den Zugriff auf die Übersetzungs-Api zu minimieren.]]
- [[Durchsuchen des Seiteninhaltes, um zusätzliche Übersetzungen zu finden, die mit Plugins von Drittanbietern wie `mkdocs-strings` erstellt wurden.]]
- [[Speichern aller Übersetzungen in einer JSON-Datei pro Seite, um den Zugriff auf die Übersetzungs-Api zu minimieren und manuelle Änderungen zu ermöglichen.]]
- [[Konvertiert Markdown in HTML, übersetzt und konvertiert zurück, um Textformatierungen wie `code`, `strong` und `em` zu erhalten.]]
- [[Fixe-Wörter in Code-Tags mit temporären HTML-Attributen erhalten.]]
- [[Übersetzung der Navigation]]
- [[Kopieren Sie die für gh-deploy erforderliche CNAME-Datei in das Stammverzeichnis des Build's.]]
- [[*ERSETZT*]] - [[Begrenzungszeichen (z.B. `{[` und `]}`) innerhalb einer Maskierung ignorieren.]]

## [[Feedback und Unterstützung]]

[[Ich freue mich über jede Art von Feedback und Unterstützung.]]

[[Vielen Dank für Ihr Interesse an diesem Plugin!]]

[[Viel Spaß beim Übersetzen!]]