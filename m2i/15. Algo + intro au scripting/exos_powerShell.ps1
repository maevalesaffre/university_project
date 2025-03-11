$message1 = "Oui, le répertoire existe"
$message2 = "Non, le répertoire n'existe pas"

If (Test-Path -Path c:\temporaire) 
{ 
    $message1
} 
Else 
{
    $message2
}

#############################################################################################

$message1 = "Oui, le répertoire existe"
$message2 = "Non, le répertoire n'existe pas"

If (Test-Path -Path c:\temporaire) 
{ 
    $message1

    If (Test-Path -Path c:\temporaire\Exe)
    {
        $message1
    }
    else
    {
        $message2
        New-Item -Path c:\temporaire\Exe -ItemType Directory
    }
    If (Test-Path -Path c:\temporaire\Logs)
    {
        $message1
    }
    else
    {
        $message2
        New-Item -Path c:\temporaire\Logs -ItemType Directory
    }
    If (Test-Path -Path c:\temporaire\Sav)
    {
        $message1
    }
    else
    {
        $message2
        New-Item -Path c:\temporaire\Logs -ItemType Directory
        
    }
}
else
{
    $message2
    New-Item -Path C:\temporaire -ItemType Directory
} 







#############################################################################################

$message1 = "Oui, le répertoire existe"
$message2 = "Non, le répertoire n'existe pas"

If (!(Test-Path -Path c:\temporaire)) 
{ 
    # Si le répertoire n'existe pas, afficher le message et créer le répertoire
    $message2
    New-Item -Path C:\temporaire -ItemType Directory
} 
else
{
    # Si le répertoire existe, afficher le message
    $message1

    If (!(Test-Path -Path c:\temporaire\Exe)) 
    {
        $message2
        New-Item -Path c:\temporaire\Exe -ItemType Directory
    }
    Else
    {
        $message1
    }

    If (!(Test-Path -Path c:\temporaire\Logs)) 
    {
        $message2
        New-Item -Path c:\temporaire\Logs -ItemType Directory
    }
    Else
    {
        $message1
    }

    If (!(Test-Path -Path c:\temporaire\Sav)) 
    {
        $message2
        New-Item -Path c:\temporaire\Sav -ItemType Directory
    }
    Else
    {
        $message1
    }
}

#############################################################################################EXO13#############################################################################################
$tab = 'papa','mama','haha','hoho'
$tab[0]
$tab[2..3]
#############################################################################################EXO14#############################################################################################

$compteur = 0
while ($compteur -lt $tab.Length)
{
    Write-Host "Le contenu de la case $($compteur + 1) est : $($tab[$compteur])" 
    $compteur++
}

#############################################################################################EXO15#############################################################################################

$exist = "oui, il existe"
$Noexist = "non, il n'existe pas, on va le créer"
 
$directories = @("c:\temporaire", "c:\temporaire\EXE", "c:\temporaire\LOG", "c:\temporaire\SAV")
 
while ($true) {
    $allExist = $true
 
    foreach ($dir in $directories) {
        if (Test-Path -Path $dir) {
            Write-Host "$dir : $exist"
        } else {
            Write-Host "$dir : $Noexist"
            New-Item -Path $dir -ItemType Directory
            $allExist = $false
        }
    }
 
    if ($allExist) {
        break
    }
}
Write-Host "Tous les dossiers ont été créés."

#############################################################################################EXO16#############################################################################################

$exist = "oui, il existe"
$Noexist = "non, il n'existe pas, on va le créer"
 
$directories = @("c:\temporaire", "c:\temporaire\EXE", "c:\temporaire\LOG", "c:\temporaire\SAV")
 
while ($true) {
    $allExist = $true
 
    foreach ($dir in $directories) {
        if (Test-Path -Path $dir) {
            Write-Host "$dir : $exist"
        } else {
            Write-Host "$dir : $Noexist"
            New-Item -Path $dir -ItemType Directory
            $allExist = $false
        }
    }
 
    if ($allExist) {
        break
    }
}
Get-ChildItem -Path "c:\Windows" -Filter "*.exe" -File | Copy-Item -Destination "c:\temporaire\EXE" -Force
Get-ChildItem -Path "c:\Windows" -Filter "*.log" -File | Copy-Item -Destination "c:\temporaire\LOG" -Force
Get-ChildItem -Path "c:\Windows" -File -Recurse | Where-Object { $_.Length -le 1KB -and $_.Extension -notin @('.zip', '.rar', '.7z', '.tar', '.gz') } | Copy-Item -Destination "C:\Temporaire\SAV" -Force

#############################################################################################EXO17#############################################################################################

Function CreerRep{
$exist = "oui, il existe"
$Noexist = "non, il n'existe pas, on va le créer"
$directories = @("c:\temporaire", "c:\temporaire\EXE", "c:\temporaire\LOG", "c:\temporaire\SAV")
$exist = "oui, il existe"
$Noexist = "non, il n'existe pas, on va le créer"
 
$directories = @("c:\temporaire", "c:\temporaire\EXE", "c:\temporaire\LOG", "c:\temporaire\SAV")
 
while ($true) {
    $allExist = $true
 
    foreach ($dir in $directories) {
        if (Test-Path -Path $dir) {
            Write-Host "$dir : $exist"
        } else {
            Write-Host "$dir : $Noexist"
            New-Item -Path $dir -ItemType Directory
            $allExist = $false
        }
    }
 
    if ($allExist) {
        break
    }
}
Write-Host "Tous les dossiers ont été créés."
}