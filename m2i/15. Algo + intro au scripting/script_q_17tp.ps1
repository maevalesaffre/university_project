# Fonction pour ajouter un utilisateur
Function Ajouter-Utilisateur {
    $Nom = Read-Host "Entrez le nom de l'utilisateur"
    $Prenom = Read-Host "Entrez le prénom de l'utilisateur"
    $SAM = Read-Host "Entrez le SAMAccountName"
    $UPN = Read-Host "Entrez le UserPrincipalName (ex: utilisateur@domaine.local)"
    $MotDePasse = Read-Host "Entrez le mot de passe de l'utilisateur" -AsSecureString

    # Créer un utilisateur dans Active Directory
    New-ADUser -SamAccountName $SAM `
               -UserPrincipalName $UPN `
               -Name "$Prenom $Nom" `
               -GivenName $Prenom `
               -Surname $Nom `
               -AccountPassword $MotDePasse `
               -Enabled $true `
               -PasswordNeverExpires $false `
               -ChangePasswordAtLogon $true `
               -Path "OU=Stagiaire,OU=AFCI,DC=m2i-core,DC=local"

    Write-Host "L'utilisateur $Prenom $Nom a été ajouté avec succès."
}

# Fonction pour ajouter un groupe
Function Ajouter-Groupe {
    $NomGroupe = Read-Host "Entrez le nom du groupe"
    $Description = Read-Host "Entrez une description pour le groupe"
    $TypeGroupe = Read-Host "Entrez le type de groupe (1 pour Universel, 2 pour Global, 3 pour Local)"

    # Créer un groupe dans Active Directory
    New-ADGroup -Name $NomGroupe `
                -GroupScope $TypeGroupe `
                -Description $Description `
                -Path "OU=Stagiaire,OU=AFCI,DC=m2i-core,DC=local"

    Write-Host "Le groupe $NomGroupe a été ajouté avec succès."
}

# Fonction pour ajouter une unité d'organisation
Function Ajouter-OU {
    $NomOU = Read-Host "Entrez le nom de l'unité d'organisation"
    $ParentOU = Read-Host "Entrez le chemin de l'unité d'organisation parent"

    # Créer une unité d'organisation dans Active Directory
    New-ADOrganizationalUnit -Name $NomOU `
                             -Path "OU=$ParentOU,DC=m2i-core,DC=local"

    Write-Host "L'unité d'organisation $NomOU a été ajoutée avec succès."
}

# Menu des opérations
Write-Host "Sélectionnez l'opération que vous souhaitez effectuer:"
Write-Host "1. Ajouter un utilisateur"
Write-Host "2. Ajouter un groupe"
Write-Host "3. Ajouter une unité d'organisation"
$choix = Read-Host "Entrez le numéro de l'opération"

Switch ($choix) {
    1 { Ajouter-Utilisateur }
    2 { Ajouter-Groupe }
    3 { Ajouter-OU }
    Default { Write-Host "Choix non valide" }
}