#Get-Command -Module ActiveDirectory
# -PSDrive
#cd AD:

$mdp = "Azerty1"
$mdp = ConvertTo-SecureString $mdp -AsPlainText -Force
 
New-ADUser -Name "Naima Mansouri" -Surname Mansouri -GivenName Naima -SamAccountName n.mansouri -UserPrincipalName n.mansouri -AccountPassword $mdp -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false

$pwd = Read-Host "veuillez saisir votre mot de passe" -AsSecureString
$nom = Read-Host "Veuillez saisir votre nom de famille"
$prenom = Read-Host "Veuillez saisir votre prenom"
write-Host "le nom de famille de l'utilisateur est:" $nom
write-Host "le prenom de l'utilisateur est:" $prenom
write-Host "le mp de l'utilisateur est:" $pwd

#####################################################################EXO6#####################################################################
##q1##
$mot = Read-Host "Entrez un mot"
if ($mot.Length -gt 0) {
    Write-Output "La première lettre du mot est : $($mot[0])"
} else {
    Write-Output "Vous n'avez pas entré de mot."
}
##q2##
$mot = Read-Host "Entrez un mot"
$mot2 = Read-Host "Entrez un mot"
if ($mot -and $mot2) {
    Write-Output "Résultat : $mot $mot2"
} else {
    Write-Output "Vous devez entrer deux mots valides."
}


##q3##
$mot1 = Read-Host "Entrez le premier mot"
$mot2 = Read-Host "Entrez le deuxième mot"
if ($mot1.Length -gt 0 -and $mot2.Length -gt 0) {
    Write-Output "Résultat : $($mot1[0]).$mot2"
} else {
    Write-Output "Vous devez entrer deux mots valides."
}

#####################################################################EXO7#####################################################################
$prenom = Read-Host "Entrez le prénom de l'utilisateur"
$nom = Read-Host "Entrez le nom de l'utilisateur"
$mdpSaisi = Read-Host "Entrez un mot de passe" -AsSecureString


$nomComplet = "$prenom $nom"
$samAccountName = "$($prenom[0]).$nom".ToLower()
$userPrincipalName = "$samAccountName@afpi.local"

New-ADUser -Name $nomComplet -GivenName $prenom -Surname $nom -SamAccountName $samAccountName -UserPrincipalName $userPrincipalName -AccountPassword $mdpSaisi -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false -Enabled $true

Write-Output "L'utilisateur $nomComplet a été créé avec succès."



#####################################################################EXO8#####################################################################
Do {
    $prenom = Read-Host "Entrez le prénom de l'utilisateur"
    $nom = Read-Host "Entrez le nom de l'utilisateur"
    $mdpSaisi = Read-Host "Entrez un mot de passe" -AsSecureString


    $nomComplet = "$prenom $nom"
    $samAccountName = "$($prenom[0]).$nom".ToLower()
    $userPrincipalName = "$samAccountName@afpi.local"

    New-ADUser -Name $nomComplet -GivenName $prenom -Surname $nom -SamAccountName $samAccountName -UserPrincipalName $userPrincipalName -AccountPassword $mdpSaisi -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false -Enabled $true

    Write-Output "L'utilisateur $nomComplet a été créé avec succès."

    # Demande si l'utilisateur veut continuer
    $continuer = Read-Host "Voulez-vous continuer ? (O/N)"

} While ($continuer -eq "O") # Continue tant que l'utilisateur répond "O"

Write-Output "Script terminé."


$mdpSaisi = Read-Host "Entrez un mot de passe" -AsSecureString

Import-Csv C:\export.csv -Delimiter ';' | New-ADUser -AccountPassword $mdpSaisi -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false -Enabled $true


#####################################################################EXO10#####################################################################

$mdpSaisi = Read-Host "Entrez un mot de passe" -AsSecureString
Import-Csv C:\export.csv -Delimiter ';' | New-ADUser -AccountPassword $mdpSaisi -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false -Enabled $true

#####################################################################EXO11#####################################################################
$choix = Read-Host "entrez a ou b"
 
Switch ($choix) { 
    a{
        Do { 
            $nom = Read-Host "Entrez le nom de l'utilisateur"
            $prenom = Read-Host "Entrez le prénom de l'utilisateur"
            $motDePasse = Read-Host "Entrez un mot de passe" -AsSecureString
            $SamAccountName = $prenom[0]+"."+$nom
            $name = $nom+" "+$prenom
            New-ADUser -Name $name -Surname $nom -GivenName $prenom -SamAccountName $SamAccountName -UserPrincipalName $SamAccountName -AccountPassword $motDePasse -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false -Enabled $true
            Write-Output "L'utilisateur $prenom $nom a été créé avec succès."
            $boucle = Read-Host "Voulez-vous créer un autre utilisateur ? (O/N)"
            } 
            While ($boucle -eq "O")
     } 
    
    b{
        $motDePasse = Read-Host "Entrez un mot de passe" -AsSecureStrin
        Import-Csv C:\export.csv -Delimiter ';' | New-ADUser -AccountPassword $motDePasse -CannotChangePassword $false -ChangePasswordAtLogon $false -PasswordNeverExpires $false -Enabled $true
     } 
}

#####################################################################EXO12#####################################################################

New-ADGroup -Name "GG_TEST01" -DisplayName "GG_TEST01" -GroupScope Global -GroupCategory Security

#####################################################################EXO13#####################################################################

Do 
{ 
            $group = Read-Host "Entrez le nom du groupe"
            $group = "GG_"+$group.ToUpper()
            New-ADGroup -Name $group -DisplayName $group -GroupScope Global -GroupCategory Security
            Write-Output "le groupe $group a été créé avec succès."
            $boucle = Read-Host "Voulez-vous créer un autre groupe ? (O/N)"
} 
            While ($boucle -eq "O")

#####################################################################EXO14#####################################################################
$group = Import-Csv C:\liste_group.csv -Delimiter ';'
foreach ($elt in $group) {
    New-ADGroup -Name $elt.Name -DisplayName $elt.Name -GroupScope Global -GroupCategory Security
    Write-Output "Le groupe $($elt.Name) a été créé avec succès."
}

#####################################################################EXO15#####################################################################
$choix = Read-Host "entrez a ou b"
 
Switch ($choix)
{
    a{
        Do { 
            $group = Read-Host "Entrez le nom du groupe"
            $group = "GG_"+$group.ToUpper()
            New-ADGroup -Name $group -DisplayName $group -GroupScope Global -GroupCategory Security
            Write-Output "le groupe $group a été créé avec succès."
            $boucle = Read-Host "Voulez-vous créer un autre groupe ? (O/N)"
            } 
            While ($boucle -eq "O")
     } 
    
    b{
        $group = Import-Csv C:\liste_group.csv -Delimiter ';'
        foreach ($elt in $group) {
            New-ADGroup -Name $elt.Name -DisplayName $elt.Name -GroupScope Global -GroupCategory Security
            Write-Output "Le groupe $($elt.Name) a été créé avec succès."
        }
     } 
}

#####################################################################EXO16#####################################################################


$choix = Read-Host "Voulez-vous créer un utilisateur ? (O/N)"

while ($choix -eq "O") {

    $nom = Read-Host "Entrez le nom de l'utilisateur"
    $prenom = Read-Host "Entrez le prénom de l'utilisateur"
    $service = Read-Host "Entrez le nom du service"
    $motDePasse = Read-Host "Entrez un mot de passe" -AsSecureString
    $SamAccountName = "$($prenom[0]).$nom"
    $name = "$prenom $nom"
    
    $groupeService = Get-ADGroup -Filter "Name -like '*$service*'" 2>$null
    
    if ($groupeService) {
        if ($groupeService.Count -eq 1) {
     
            $groupeCible = $groupeService.Name
            Write-Output "Ajout de l'utilisateur $name au groupe $groupeCible"
        } else {
            # Plusieurs groupes trouvés -> Demande à l'utilisateur de choisir
            Write-Output "Plusieurs groupes contiennent '$service', veuillez en choisir un :"
            $groupeService | Select-Object -ExpandProperty Name
            $groupeCible = Read-Host "Entrez le nom exact du groupe"
        }
    } else {
        # Aucun groupe trouvé -> Création du groupe
        $groupeCible = "GG_$service"
        Write-Output "Création du groupe $groupeCible"
        New-ADGroup -Name $groupeCible -DisplayName $groupeCible -GroupScope Global -GroupCategory Security
    }
    
    # Création de l'utilisateur
    Write-Output "Création de l'utilisateur $name"
    New-ADUser -Name $name -Surname $nom -GivenName $prenom -SamAccountName $SamAccountName -UserPrincipalName "$SamAccountName@domaine.local" -AccountPassword $motDePasse -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false -Enabled $true
    
    # Ajout de l'utilisateur au groupe sélectionné
    Add-ADGroupMember -Identity $groupeCible -Members $SamAccountName
    Write-Output "L'utilisateur $name a été ajouté au groupe $groupeCible"
    
    # Demande si l'utilisateur veut continuer
    $choix = Read-Host "Voulez-vous créer un autre utilisateur ? (O/N)"
}
