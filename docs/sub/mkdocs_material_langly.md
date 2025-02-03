# MKDocs Material Langly Plugin

[[Das Langly-Plugin für MkDocs ist ein Plugin, das Sprachunterstützung und Übersetzungen für Webseiten bietet, die mit MkDocs erstellt wurden. Es ermöglicht die einfache Verwaltung mehrsprachiger Inhalte und die automatische Übersetzung von Texten, um eine breitere Zielgruppe zu erreichen.]]

[[Es wurde unter Verwendung des großartigen Material-Themes erstellt und bietet Funktionalitäten auch den Blogbereich mit zu übersetzen.]]

[[Die derzeitige Übersetzungsengine ist Deepl und es wird ein Deepl-Api-Key benötigt, um das Plugin zu verwenden.]]

!!! note
    [[Das Plugin ist noch in der Entwicklung und es wird empfohlen, die Dokumentation zu lesen, um die Funktionalitäten und Einschränkungen zu verstehen. Ich bitte auch alle Anforderungen und Änderungsvoschlage in den Issues zu melden.]]

## Lasst uns Anfangen


[[Um das Plugin zu verwenden, müssen Sie es zuerst installieren. Führen Sie dazu den folgenden Befehl aus:]]

```bash
pip install mkdocs-material-langly
```

[[Nach der Installation können Sie das Plugin in Ihrer `mkdocs.yml`-Konfigurationsdatei aktivieren:]]

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