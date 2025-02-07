---
draft: false
date: 2024-01-31
authors:
  - kemo 
categories:
  - Powershell
---

# [[Verteilung von Autodesk-Software mit ODIS-Installer und PowerShell unter Vermeidung des Double-Hop-Problems]]

[[Seitdem Autodesk sein Deployment-System auf den ODIS-Installer umgestellt hat, laufen alle Verteilungen, die unbeaufsichtigt über den SYSTEM-Account ausgerollt werden, ohne Erfolgscode endlos weiter]].

<!-- more -->

[[Die genaue Fehlermeldung im ODIS-Log lautet:]]

```
2023-06-15T15:17:04.012 [DDA: 2196, single] [Installer INFO] [ Autodesk::DDA::SdkAgent::Listen::<lambda_8f7c2cafda285d6f3324fbe86a24bae4>::operator () ] [IPC] ChannelWin::Listen: WaitForSingleObject timeout. error_code: 997, pipe_name: \\.\pipe\adsk_dda_sdk
```

[[Nach einer Weile scheint der Installer-Dienst auch beendet zu werden, sendet aber keinen Exit-Code mehr.]]

[[Ich habe viele Deployment-Suiten ausprobiert, aber das Resultat ist immer dasselbe, wenn der SYSTEM-Account zum Einsatz kommt.]]

[[Um das Problem vorübergehend zu lösen, bis Autodesk das Problem erkennt und behebt, habe ich nun Lösungsansätze entwickelt, die mir hier bei der Arbeit Abhilfe verschaffen.]]

[[Mein geplanter Ansatz war, die Verteilung über PowerShell zu realisieren, aber dabei stieß ich erneut auf eine weitere Hürde, die die Kerberos-Authentifizierung mit sich bringt: das sogenannte Double-Hop-Problem, da meine Softwarepakete in CIFS-Freigaben lagern.]]

[[Kerberos lässt es nicht zu, dass nach einer Authentifizierung auf einem Remote-PC eine weitere Authentifizierung über diesen Endpunkt zu anderen entfernten Zielen durchgeführt wird. Es gibt also keinen zweiten Hop. Um das Problem zu umgehen, gibt es wenige, aber komplizierte Wege oder einen, bei dem jetzt alle sagen werden: "Oh mein Gott, tu das nicht", aber ich hau es einfach mal raus.]]

[[Die Lösung ist, CredSSP nur temporär als Punkt-zu-Punkt-Verbindung zu nutzen und nach dem Deployment wieder zu entschärfen. Es sollte unter keinen Umständen unternehmensweit erlaubt werden.]]

!!! info
    [[CredSSP hat keinen Single-Hop-Zwang. Authentifizierungen können in einer CredSSP-Sitzung weiterverwendet werden. Sollte das unternehmensweit und dauerhaft erlaubt werden, kann das zu erheblichen Sicherheitsproblemen führen.]]

[[Hier nun das Skript für alle, die vor dem selben Problem stehen.]]

[[Das hier beschriebene Skript ist bewusst flach gehalten, um es verständlich zu machen und den weiteren Ausbau durch Euch so einfach wie möglich zu gestalten.]]

!!! info
    [[Bitte beachten Sie, dass in diesem Beispiel CredSSP nur temporär verwendet wird und nach dem Deployment wieder deaktiviert wird. Zudem wird ausschließlich der angegebene Remote-Computer delegiert und nicht das gesamte Netzwerk.]]

    [[Nach gründlicher Validierung hat sich dieser Ansatz als sicherer und einfacher Weg erwiesen, um das gewünschte Ziel zu erreichen.]]

!!! warning
    [[Dieses Skript muss mit administrativen Rechten ausgeführt werden, um die CredSSP-Authentifizierung zu aktivieren und zu deaktivieren.]]

```powershell
# Define the parameters with your own values

param (
[string]$Computer = "<remote-computer>",
[string]$Name = "Autodesk Revit 2024",
[string]$Installer = '<share>\Autodesk Revit 2024\image\Installer.exe',
[string]$Argument = '-i deploy --offline_mode -q -o "<share>\Autodesk Revit 2024\image\Collection.xml" --installer_version "2.9.0.31"'
)

# Prompt for user credentials
$cred = Get-Credential -Message "Enter your credentials"

try {
    # Enable CredSSP on the client
    $null = Enable-WSManCredSSP -Role Client -DelegateComputer $Computer -Force

    # Enable CredSSP on the server (if not already enabled)
    Invoke-Command -ComputerName $Computer -Credential $cred -ScriptBlock {
        $null = Enable-WSManCredSSP -Role Server -Force
    }
    
    # Create a new PSSession with CredSSP authentication
    $session = New-PSSession -ComputerName $Computer -Credential $cred -Authentication Credssp

    # Execute the script on the remote computer
    Invoke-Command -Session $session -ScriptBlock {
        param ($Name, $Installer, $Argument)
        
        # Output a message before starting the installation process
        Write-Host "$Name is being installed..."

        # Start the installation process
        $process = Start-Process -FilePath $Installer -ArgumentList $Argument -PassThru

        # Output the process ID
        Write-Host "The installation process has started. Process ID: $($process.Id)"

        # Wait for the installation process to complete
        $process.WaitForExit()

        Write-Host "The installation process completed with exit code $($process.ExitCode)."

    } -ArgumentList $Name, $Installer, $Argument
}
finally {
    # Close the PSSession
    if ($session) {
        Remove-PSSession -Session $session
    }

    # Disable CredSSP on the server
    Invoke-Command -ComputerName $Computer -Credential $cred -ScriptBlock {
        Disable-WSManCredSSP -Role Server
    }

    # Disable CredSSP on the client
    Disable-WSManCredSSP -Role Client
}
```

Erklären wir nun die einzelnen Schritte des Skripts:

```powershell
# Define the parameters with your own values

param (
[string]$Computer = "<remote-computer>",
[string]$Name = "Autodesk Revit 2024",
[string]$Installer = '<share>\Autodesk Revit 2024\image\Installer.exe',
[string]$Argument = '"<share>\Autodesk Revit 2024\image\Installer.exe" -i deploy --offline_mode -q -o "<share>\Autodesk Revit 2024\image\Collection.xml" --installer_version "2.9.0.31"'
)
```
[[Das Skript kann entweder mit Parametern aufgerufen werden, oder Sie tragen Ihre spezifischen Werte direkt ein. Die notwendigen Informationen für den Installer und die Argumente finden Sie nach der Image-Erstellung im entsprechenden Installations-Skript. Ein typischer Name für eine Revit-Installation könnte beispielsweise `Install Autodesk Revit 2024.bat` sein.]]

[[Die Parameter für die Silent-Installation und Deinstallation sind ebenfalls dort hinterlegt. Diese Parameter ermöglichen eine unbeaufsichtigte Installation bzw. Deinstallation der Software, was besonders in großen IT-Umgebungen von Vorteil ist.]]

[[Für weitere Details und eine ausführliche Anleitung zur Bereitstellung von Autodesk-Software, besuchen Sie bitte den folgenden Artikel:]]

https://www.autodesk.com/support/download-install/admins/account-deploy/deploy-from-autodesk-account

```powershell
# Prompt for user credentials
$cred = Get-Credential -Message "Enter your credentials"
```

[[Um eine PowerShell-Sitzung unter Verwendung von CredSSP zu starten, benötigen wir die Anmeldeinformationen eines Benutzers mit den erforderlichen Rechten zur Durchführung von Installationen. In den meisten Fällen handelt es sich dabei um den Domain-Admin. Ein Dialogfeld wird angezeigt, in dem Sie die Anmeldeinformationen eingeben können.]]

```powershell
try {
    # Enable CredSSP on the client
    $null = Enable-WSManCredSSP -Role Client -DelegateComputer $Computer -Force

    # Enable CredSSP on the server (if not already enabled)
    Invoke-Command -ComputerName $Computer -Credential $cred -ScriptBlock {
        $null = Enable-WSManCredSSP -Role Server -Force
    }
```

[[Hier wird CredSSP sowohl auf dem Client als auch auf dem Server aktiviert. Es ist hilfreich, die Begriffe "Verteiler" (Client) und "Empfänger" (Server) zu verwenden, um die Rollen klarer zu definieren. Der Try-Block umfasst alle potenziell fehleranfälligen Aktionen und kann nach Belieben angepasst werden. Für den Anfang ist diese Struktur einfach und robust.]]

```powershell
# Create a new PSSession with CredSSP authentication
$session = New-PSSession -ComputerName $Computer -Credential $cred -Authentication Credssp
```

[[Hier wird eine neue PowerShell-Sitzung mit CredSSP-Authentifizierung erstellt.]]

```powershell
    # Execute the script on the remote computer
    Invoke-Command -Session $session -ScriptBlock {
        param ($Name, $Installer, $Argument)
        
        # Output a message before starting the installation process
        Write-Host "$Name is being installed..."

        # Start the installation process
        $process = Start-Process -FilePath $Installer -ArgumentList $Argument -PassThru

        # Output the process ID
        Write-Host "The installation process has started. Process ID: $($process.Id)"

        # Wait for the installation process to complete
        $process.WaitForExit()

        Write-Host "The installation process completed with exit code $($process.ExitCode)."

    } -ArgumentList $Name, $Installer, $Argument
}
```

[[Hier wird das Skript auf dem Remote-Computer ausgeführt. Der Name, der Installer und die Argumente werden als Parameter übergeben. An dieser Stelle endet der Try-Block.]]

```powershell
finally {
    # Close the PSSession
    if ($session) {
        Remove-PSSession -Session $session
    }

    # Disable CredSSP on the server
    Invoke-Command -ComputerName $Computer -Credential $cred -ScriptBlock {
        Disable-WSManCredSSP -Role Server
    }

    # Disable CredSSP on the client
    Disable-WSManCredSSP -Role Client
}
```

[[Im Finally-Block wird die PowerShell-Sitzung geschlossen und CredSSP auf dem Server und Client deaktiviert. Der Finally-Block wird immer ausgeführt, unabhängig davon, ob der Try-Block erfolgreich war oder nicht. Bitte beachten Sie, dass das Abfangen von Fehlern auch über einen möglichen Exception-Block erfolgen kann. Dies überlasse ich dem findigen Leser.]]

[[Dieses Skript dient mir nun selbst als Grundlage für Erweiterungen. Ich werde nun daran arbeiten, ein übergeordnetes Skript zu entwickeln, um die Installationen in großen Mengen zu steuern und zu überwachen.]]

**[[Quellangaben]]**

- https://www.autodesk.com/support/download-install/admins/account-deploy/deploy-from-autodesk-account
- https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ps-remoting-second-hop?view=powershell-7.4