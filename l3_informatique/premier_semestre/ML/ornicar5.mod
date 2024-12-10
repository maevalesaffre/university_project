set GRAVIER;
set COMP;
set ASSOC_INTERDITES within {COMP, GRAVIER};
param masse_volumique {GRAVIER} >=0;
param prix_volumique {GRAVIER} >=0;
param quantite_minimale {GRAVIER} >=0;
param stock {GRAVIER} >=0;

param hauteur {COMP} >=0;
param abs_gauche {COMP} >=0;
param abs_droite {COMP} >=0;
param masse_maximale {COMP} >=0;
param largeur {COMP} >=0;
 
param volume_max_non_utilise >=0;
param abs_gravite_min >=0;
param abs_gravite_max >=0;
param volume_sac >= 0;

var contient {GRAVIER, COMP} binary;
var nb_bags {g in GRAVIER, p in COMP} integer >= 0;


maximize profit:
    sum {g in GRAVIER, p in COMP} nb_bags[g, p] * volume_sac * prix_volumique[g];

subject to boolean1 {g in GRAVIER, p in COMP}:
    contient [g,p] <= nb_bags[g,p];

subject to boolean2 {g in GRAVIER, p in COMP}:
    nb_bags[g,p] <= contient [g,p] * ((hauteur[p] * largeur [p] * (abs_droite [p] - abs_gauche[p]))/volume_sac);

subject to max_grav_comp {g in GRAVIER} :
    sum {p in COMP} contient[g,p] <=2;

subject to max_type_comp {p in COMP} :
    sum {g in GRAVIER} contient[g,p] <=2;

subject to masse_maximale_comp {p in COMP}:
    sum {g in GRAVIER}  nb_bags [g,p] * volume_sac * masse_volumique[g] <= masse_maximale[p];

subject to stock_max {g in GRAVIER}:
    sum {p in COMP} nb_bags [g,p] * volume_sac * masse_volumique[g] <= stock[g];

subject to quantite_minimale_transporte {g in GRAVIER}:
    sum {p in COMP} nb_bags [g,p] * volume_sac * masse_volumique[g] >= quantite_minimale[g];

subject to asso_interdite {(c,g) in ASSOC_INTERDITES}:
        nb_bags [g,c] = 0;


subject to stabilite1:
    (sum {p in COMP} ((sum {g in GRAVIER} nb_bags [g,p] * volume_sac * masse_volumique [g]) * ((abs_gauche[p] + abs_droite[p])/2))) >= (abs_gravite_min * (sum {p in COMP} (sum {g in GRAVIER} nb_bags [g,p] * volume_sac * masse_volumique [g])));


subject to stabilite2:
    (sum {p in COMP} ((sum {g in GRAVIER} nb_bags [g,p] * volume_sac * masse_volumique [g]) * ((abs_gauche[p] + abs_droite[p])/2))) <= (abs_gravite_max * (sum {p in COMP} (sum {g in GRAVIER} nb_bags [g,p] * volume_sac * masse_volumique [g])));

subject to volume_non_utilise :
    (sum {p in COMP} (hauteur[p] * largeur [p] * (abs_droite [p] - abs_gauche[p] ))) - (sum {p in COMP} (sum {g in GRAVIER} nb_bags [g,p] * volume_sac)) <= volume_max_non_utilise ;

subject to volume_max_comp {p in COMP}:
    sum {g in GRAVIER} nb_bags [g,p] <= (hauteur[p] * largeur [p] * (abs_droite [p] - abs_gauche[p] ))/ volume_sac;

data;

set GRAVIER := subtil fin moyen grossier vulgaire caillou;
set COMP := A B C D;
set ASSOC_INTERDITES := (A,fin) (A, subtil) (B, subtil);
param abs_gravite_min := 4.6;
param abs_gravite_max := 5.5; 
param volume_max_non_utilise := 5;
param volume_sac := 0.2;


param: abs_gauche abs_droite hauteur masse_maximale largeur :=
A            1        3.5       1.8        30           4
B            3.8      6.2       2.3        26           4
C            6.5      7.3       2.9        24           4
D            7.5      10.2      1.9        22           4;

param: masse_volumique prix_volumique stock quantite_minimale :=
subtil      2.4             35          18              15
fin         1.7             28          25              13
moyen       1.6             23          26              12
grossier    1.2             20          30              17
vulgaire    1.1             15          35              19
caillou     0.9             13          10              5;