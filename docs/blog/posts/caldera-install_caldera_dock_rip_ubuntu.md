---
draft: false
date: 2025-02-04
authors:
  - kemo
categories:
  - Caldera
---

# Installation von Caldera Dock und Caldera Rip auf Ubuntu Desktop 22.04

[[In diesem Beitrag wird die Installation von Caldera Dock und Caldera Rip auf einem Ubuntu Desktop 22.04 System detailliert beschrieben. Die Anleitung umfasst die Vorbereitung des Systems, die Installation von Ubuntu, sowie die anschließende Installation und Konfiguration von Caldera Dock und Caldera Rip. Zusätzlich wird die Einrichtung von XRDP zur Remote-Verbindung erläutert. Diese Schritt-für-Schritt-Anleitung richtet sich an Benutzer, die entweder eine virtuelle Maschine oder einen physischen Computer verwenden möchten.]]

<!-- more -->

## Vorbereitung

[[Bevor mit der Installation von Caldera Dock und Caldera Rip auf Ubuntu 22.04 begonnen werden kann, gibt es einige grundlegende Schritte, die durchgeführt werden sollten.]]

[[Für die Installation kann entweder eine virtuelle Maschine (VM) oder ein physischer Computer (Bare Metal) verwendet werden. Beide Optionen sind geeignet und bieten die notwendigen Voraussetzungen für die Installation. In diesem Beispiel wird eine Proxmox VM verwendet, aber auch andere Virtualisierungsplattformen können genutzt werden.]]

[[Es sollte sichergestellt werden, dass das System über eine funktionierende Internetverbindung verfügt, um während der Installation Updates herunterladen zu können und sicherzustellen, dass alle benötigten Pakete und Abhängigkeiten verfügbar sind. Die Systemanforderungen von Caldera sollten eingehalten werden, diese können auf der offiziellen Caldera-Website eingesehen werden.]]

[[Es wird empfohlen, vor der Installation ein Backup des Systems zu erstellen, um sicherzustellen, dass im Falle eines Problems alle Daten gesichert sind. Zudem sollte die Dokumentation von Caldera gelesen werden, um sich mit den spezifischen Anforderungen und Schritten für die Installation vertraut zu machen.]]

[[Nachdem die Vorbereitungen abgeschlossen sind, kann mit der Installation von Caldera Dock und Caldera Rip auf Ubuntu 22.04 begonnen werden.]]


## [[Installation Ubuntu Desktop 22.04]]

[[Nach dem mounten des aktuellen `Ubuntu Desktop 22.04` Isos entweder über USB Stick oder als Bootmedium in der VM, wird die Installtionsroutine gestartet.]]

### Installationsschritte

- [[Der Willkommensbildschirm erscheint, der die Optionen bietet, Ubuntu auszuprobieren oder zu installieren. Zuerst die bevorzugte **Sprache** auswählen und dann die Option **Ubuntu installieren** wählen und die Eingabetaste drücken.]]
- [[Die Tastaturbelegung auswählen und auf **Weiter** klicken.]]
- [[Die **Minimale Installation**, **Während Ubuntu installiert wird Aktualisierungen herunterladen** und **Installieren Sie Software von Drittanbietern für Grafik- und Wi-Fi-Hardware und zusätzliche Medienformate** auswählen und auf **Weiter** klicken.]]
- [[Als nächstes die Option **Festplatte löschen und Ubuntu installieren** auswählen und auf **Jetzt Installieren** klicken.]]
- [[Standort auswählen und auf **Weiter** klicken.]]
- [[Alle Felder unter *Wer sind Sie?* wie folgt ausfüllen:]]
      - [[**Ihr Name**]]: `caldera`
      - [[**Name Ihres Rechners**]]: [[*Hier den tasächlichen DNS-Namen wählen wie der PC später angesprochen werden soll. z.B. `calderarip`*]]
      - [[**Bitte Benutzernamen auswählen**]]: `caldera`
      - [[**Ein Passwort wählen**]]: `caldera` [[*(Laut Hersteller Dokumentation)*]]
      - [[**Passwort zum anmelden abfragen** *(emphiehlt sich wenn xrdp für die Verbindung zum Ubuntu Desktop eingesetzt wird)*]]
- [[Nachdem alle Felder ausgefüllt sind, auf **Weiter** klicken.]]

[[Warten, bis die Installation abgeschlossen ist, und das System neu starten.]]

[[Nach dem Neustart sollte `Ubuntu Desktop 22.04` erfolgreich installiert sein und eine Anmeldung mit dem zuvor erstellten Benutzer ist möglich.]]

## [[Installation von Caldera Dock]]

[[Nach der Installation von `Ubuntu Desktop 22.04` kann mit der Installation von Caldera Dock fortgefahren werden.]]

### [[Download der Installationsdatei]]

- [[Bei `Caldera WorkSpace` anmelden und zur Haupt-Dashboard-Seite gehen.]]
- [[Auf die Schaltfläche **Installieren** klicken, um die Installationsdatei zu finden. Caldera Dock (Ubuntu) herunterladen.]]

### [[Installieren Sie die heruntergeladene .deb-Datei]]

- [[Zu dem Ordnerwechseln , in dem die Installationsdatei gespeichert wurde.]]
- [[Die Installationsdatei finden, mit der rechten Maustaste darauf klicken und die Option **Mit anderer Anwendung öffnen** wählen.]]
- [[Der Ubuntu-Installationsassistent wird angezeigt. **Software-Installation** auswählen.]]
- [[Einige Sekunden warten, bis die Installationsdateien geladen sind, und dann auf **Installieren** klicken.]]
- [[Vor der Fortsetzung der Installation wird eine Authentifizierung verlangt. Das Passwort eingeben, das bei der Installation von `Ubuntu Desktop 22.04` festgelegt wurde.]]

[[Die Installation wird nun durchgeführt.]]

[[Sobald die Installation abgeschlossen ist, kann `Caldera Dock` über das Hauptmenü oder die Suchleiste gestartet werden.]]

### [[Installieren der Setup-Tools]]

- [[Auf der **Startseite** von `Caldera Dock` im Abschnitt **Setup-Tools** auf **Installieren** klicken.]]
- [[Danach auf **Konfigurieren** und mit dem Passwort bestätigen.]]

[[Nach einiger Zeit wird die Installation abgeschlossen sein und die Setup-Tools sind einsatzbereit.]]

[[Ein Neustart wird empfohlen, um sicherzustellen, dass alle Änderungen wirksam werden.]]

## [[Installation von Caldera Rip]]

[[Nun die Anleitungsschritte zur Installation von `Caldera Rip` auf `Ubuntu Desktop 22.04`.]]

### [[Installation von Caldera Rip]]

- [[Im `Caldera Dock` auf *Anwendungen* klicken.]]
- [[`Caldera Rip` suchen und auf **Installieren** klicken.]]
- [[Die Swap-Datei vergrößern, wenn die Meldung erscheint.]]
- [[Nach dem Download und vor der Installation wird eine Authentifizierung verlangt. Das Passwort eingeben, das bei der Installation von `Ubuntu Desktop 22.04` festgelegt wurde.]]

[[Ein weiterer Neustart sollte anschließend durchgeführt werden.]]

## [[Einrichten von XRDP]]

[[Um eine Verbindung zum `Ubuntu Desktop 22.04` über `XRDP` herzustellen, sind einige zusätzliche Schritte erforderlich.]]

### [[Installation von XRDP]]

- [[Öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus, um `XRDP` zu installieren:]]

```bash
sudo apt update
sudo apt upgrade
sudo apt install xrdp -y
```

- [[Nach der Installation von `XRDP` führen Sie den folgendene Befehle aus, um den `XRDP`-Dienst zu aktivieren und zu starten:]]

```bash
sudo systemctl enable xrdp
sudo systemctl start xrdp
```

- [[Fügen Sie den Benutzer `xrdp` zur Gruppe `ssl-cert` hinzu, um die Verbindung zu ermöglichen:]]

```bash
sudo usermod -a -G ssl-cert xrdp
```

- [[Nur RDP durch die lokale Firewall zulassen:]]

```bash
sudo ufw allow 3389
```

- [[Um die Ubuntu-Session anstelle der Standard-GNOME-Session zu verwenden, in Ihrem Home-Verzeichnis die Datei .xsessionrc mit folgendem Inhalt erweitern:]]
  
```bash
nano ~/.xsessionrc
```
- [[Fügen Sie folgende Zeilen hinzu:]]

```bash
export GNOME_SHELL_SESSION_MODE=ubuntu
export XDG_CURRENT_DESKTOP=ubuntu:GNOME
export XDG_CONFIG_DIRS=/etc/xdg/xdg-ubuntu:/etc/xdg
```

- [[Schließlich XRDP neu starten, um die Änderungen zu übernehmen:]]

```bash	
sudo systemctl restart xrdp
``` 

[[Nachdem die Installation abgeschlossen ist, kann diee Verbindung zu Ihrem `Ubuntu Desktop 22.04` über `XRDP` hergestellt werden.]]