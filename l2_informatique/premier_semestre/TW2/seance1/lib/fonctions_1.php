<?php
//  Q1
function AfficheVar($n,$s){
  return "<p> \$n vaut $n et \$s vaut $s </p>";
}

//  Q2
function nparag($text,$n){
  for ($i=0; $i<$n; $i++)
    $res .= "<p>$text</p>";

  return $res;
}

//  Q3
function paragrapheTronque($s,$i){
    return "<p>".substr($s,0,$i)."</p>";
}

function diminue($texte){
  for ($i=strlen($texte); $i>0; $i--){
    $res .= paragrapheTronque($texte,$i);
  }
  return $res;
}

//  Q4
function paragrapheTronque2($s,$i){
    return "<li>".substr($s,0,$i)."</li>";
}

function diminue2($texte){
  $res .= "<ul>\n";
  for ($i=strlen($texte); $i>0; $i--)
       $res .= paragrapheTronque2($texte,$i);
  $res .= "</ul>\n";
  return $res;
}

//  Q5
function multiplication($i,$j){
    $prod = $i*$j;
    return "<li>$i * $j = $prod</li>\n";
}

function tableMultiplication($i){
    $res = "<ul>\n";
    for ($j=1; $j<=9; $j++)
        $res .=  multiplication($i,$j);
    $res .="</ul>\n";
    return $res;
}

// Q6
function tablesMultiplications(){
    $res = "<ul>\n";
    for ($i=2; $i <= 9; $i++){
        $res .= "<li>\n" . tableMultiplication($i) . "</li>\n";
    }
    $res .= "</ul>\n";
    return $res;
}

//  Q7
function ligneTable($i){
    $res = "<tr><th>$i</th>\n";
    for ($j=1; $j<=9; $j++){
        $r = $i*$j;
        $res .= "<td>$r</td>";
    }
    $res .="\n</tr>\n";
    return $res;
}
function ligneEntete(){
    $res = "<tr><th>*</th>\n";
    for ($j=1; $j<=9; $j++){
        $res .= "<th>$j</th>";
    }
    $res .="</tr>\n";
    return $res;
}
function tablesMultiplications2(){
    $res  = "<table id=\"multiplications\">\n";
    $res .= "<thead>\n" . ligneEntete() . "</thead>\n";
    $res .= "<tbody>\n";
    for ($i=1; $i<=9; $i++){
        $res .= ligneTable($i);
    }
    $res .= "</tbody>\n";
    $res .= "</table>\n";
    return $res;
}

//  Q8
function separe($texte){
    $parts = explode('+',$texte);
    for ($i=0; $i<count($parts); $i++){
        $parts[$i] = trim($parts[$i]);
    }
    return "<p>".implode("</p><p>",$parts)."</p>";
}

//  Q9
function enSpan($texte){
    $parts = explode(' - ',$texte);
    for ($i=0; $i<count($parts); $i++){
        $parts[$i] = trim($parts[$i]);
    }
    return "<span>".implode("</span><span>",$parts)."</span>";
}


?>
