# MKDocs Material Langly Plugin

[[Das Langly-Plugin für MkDocs ist ein Plugin, das Sprachunterstützung und Übersetzungen für Webseiten bietet, die mit MkDocs in verwendung des Material-Themes erstellt wurden. Es ermöglicht die einfache Verwaltung mehrsprachiger Inhalte und die automatische Übersetzung von Texten, um eine breitere Zielgruppe zu erreichen. Es erfüllt bewusst keine der derezitigen Übersetzungsstandards sondern geht einen ganz eigenen aber offenen Weg.]]

[[Diese Plugin wurde für Verwendung des großartigen Material-Themes erstellt und bietet Funktionalitäten um z.B. auch den Blogbereich zu Internationalisieren.]]

[[**Es werden im vorliegenden Entwicklungstand auch keine anderen Themen unterstützt. Die derzeit einzige Übersetzungsengine ist Deepl und es wird ein deepl-Api-Key benötigt, um das Plugin zu verwenden.**]]

## [[Direkte unterstütze Plugins für mkdocs]] ##

[[ Diese Auflistung sind die Plugins die bei der Entwicklung von Langly direkt verwendet wurden.]] 
[[**Aber es ist nicht ausgeschlossen, dass auch andere Plugins funktionieren.**]]

- [mkdocs-material](https://squidfunk.github.io/mkdocs-material){:target="_blank"}
- [mkdocs-strings](https://mkdocstrings.github.io){:target="_blank"}

<!-- Abastz für inkludierte Plugins mit Danksagung -->

[[Diese großartigen Plugins benötigen definitiv volle Unterstützung und Anerkennung.]]

!!! note
    [[Das Plugin ist noch in der Entwicklung und es wird empfohlen, die Dokumentation zu lesen, um die Funktionalitäten und Einschränkungen zu verstehen. Ich bitte auch alle Anforderungen und Änderungsvoschlage in den Github-Issues zu melden.]]

## [[Lasst uns Anfangen]]

[[Für den Anfang werden ein paar vorläufige Schritte benötigt, um das Plugin zu benutzen.]]

- [x] [[mkdocs mit installiertem Material-Theme]]
- [x] [[Ein deepl-Account wird benötigt (deepl im derzeitigen Stand die einzige unterstützte Übersetzungsengine)]]

### [[Installation des Plugins]]

[[Um das Plugin zu verwenden, müssen Sie es zuerst installieren. Führen Sie dazu den folgenden Befehl aus:]]

```bash
pip install mkdocs-material-langly
```

### [[Api-Key bereitstellen]]

!!! danger
    [[**Bitte lesen sie diesen Abschnitt sorgfältig durch und beachten Sie den Api-Key in der .gitignore auszuschließen und auch auf jede erdenkliche Weise vor dem Upload ins Internet zu schützen.**]]

[[Um das Plugin zu verwenden, benötigen Sie einen Deepl-Api-Key. Sie können diesen kostenlosen von der Deepl-Website erhalten.]]

[[Nachdem Sie den Api-Key erstellt haben, erstellen Sie eine Datei namens `auth_key.json` im Wurzelverzeichnis Ihres Projekts und fügen folgenden Inhalt ein:]]

```json
  {
      "deepl": "DEEPL-API-KEY"
  }

```

[[Ersetzen Sie `DEEPL-API-KEY` durch Ihren eigenen Api-Key.]]

[[**Öffnen Sie die Datei .gitignore und fügen Sie die Zeile `auth_key.json` hinzu, um zu verhindern, dass die Datei versehentlich hochgeladen wird.**]]

### [[Konfiguration des Plugins]]

[[Nach der Installation können Sie das Plugin in Ihrer `mkdocs.yml`-Konfigurationsdatei aktivieren.]]

```yaml
plugins:
  - search
  - langly:
      source:
          name: Deutsch
          lang: de
      targets:
        - name: English
          lang: en-us

```

[[ In dieser Konfiguration wird die Sprache Deutsch als Quellsprache und Englisch als Zielsprache festgelegt. Sie können beliebig viele Zielsprachen hinzufügen. Allerdings beeinträchtig das die `serve' Performance um so mehr]]

!!! warning
    [[Wichtig ist dabei die deepl-Language-Codes für `source` und `target` zu verwenden. Diese sind auf folgender website zu finden: [Deepl Language Codes](https://developers.deepl.com/docs/resources/supported-languages){:target="_blank"}]]

[[Nachdem Sie die Konfiguration vorgenommen haben, können Sie die Übersetzungsfunktionen in Ihren Markdown-Dateien verwenden.]]

### [[Verwendung des Plugins]]

[[Das Plugin analysiert markdown Texte und wertet maskierte Textpassagen aus, die mit `[[` und `]]` umschlossen sind. Diese `delimiter` werden beim rendern der Seite entfernt und Quell sowie Zielsprache werden korekt auf Ihrer Seite dargestellt.]] 

[[ Gehen sie wie folgt vor um Texte zu maskieren]]

==[[`[[`Ihr Text`]]`]]==

[[Der Text innerhalb der Maskierung wird dann von Langly übersetzt automatisch Übersetzt.]]

### [[Ein paar einfache Beispiele]]

#### [[Satz]]

[[`[[`Dieser Text repräsentiert Ihre Quellsprache`]]`]]

#### [[Absatz]]

[[`[[`Dieser Absatz enthält mehrere Sätze in Ihrer Quellsprache. Es ist die empfohlene Art der Maskierung von Textpassagen und liefert Deepl mehr Kontext um eine bessere Übersetzung zu liefern.`]]`]]
#### [[Aufzählung mit Doppelpunkt]]

- [[`[[`Aufzählung`]]`]]== **:** ==[[`[[`Wert nach dem Doppelpunkt`]]`]]

#### [[Satz in dem der Delimiter vorkommt]]

[[Umschließen sie den öffnenden und schließenden Delimiter mit **`**]]

## [[Feedback und Unterstützung]]

[[Ich freue mich über jede Art von Feedback und Unterstützung.]]

[[Vielen Dank für Ihr Interesse an diesem Plugin!]]

[[Viel Spaß beim Übersetzen!]]