
window.addEventListener('load',initForm);
function initForm(){
  fetchFromJson('services/getTerritoires.php')
  .then(processAnswer)
  .then(makeOptions);
  
  document.forms.form_communes.addEventListener("submit", sendForm);
  
  // décommenter pour le recentrage de la carte :
  //document.forms.form_communes.territoire.addEventListener("change",function(){
  //  centerMapElt(this[this.selectedIndex]);
  //});
}


/**
 * reçoit la réponse du service, donc un objet ayant la structure décrite plus haut (avec attributs status, result ...)
 * et renvoie la valeur de result en cas de succès.
 * answer réponse
 */
function processAnswer(answer){
  if (answer.status == "ok")
    return answer.result;
  else
    throw new Error(answer.message);
}

/**
 * reçoit le résultat lui-même, c’est à dire une liste d’objets « territoire »,
 * chacun avec ses 6 attributs id, nom, min_lat, ...
 * tab un tableau
 */
function makeOptions(tab){
  for (let territoire of tab){  
    let option = document.createElement('option');
    option.textContent = territoire.nom;
    option.value = territoire.id;
    document.forms.form_communes.territoire.appendChild(option);
    for (let k of ['min_lat','min_lon','max_lat','max_lon']){
      option.dataset[k] = territoire[k];
    }
  }
}

function sendForm(ev){ // form event listener
  ev.preventDefault();
  let url = 'services/getCommunes.php?'+formDataToQueryString(new FormData(this));
  fetchFromJson(url)
  .then(processAnswer)
  .then(makeCommunesItems);
}

/**
 * La fonction doit vider le contenu de l’élément HTML <ul id="liste_communes"> préexistant et y insérer un item
 * <li> pour chaque commune de la liste tab. Chaque item <li> comportera des attributs data-insee data-lat data-lon data-min_lat etc..
 * Vous pourrez vous inspirer de la fonction makeOptions mais aussi de l’exemple vu en cours.
 *tab une liste
 */
function makeCommunesItems(tab){
  liste_commune = document.getElementById("liste_communes");
  liste_commune.innerHTML="";
  for (let commune of tab){
    c = document.createElement('li');
    c.innerHTML = commune['nom'];
    for (let elt of ['insee', 'nom', 'lat', 'lon', 'min_lat', 'min_lon', 'max_lat', 'max_lon']){
      c.setAttribute('data-'+elt, commune[elt]); 
    }
    liste_commune.appendChild(c);
    c.addEventListener("click", fetchCommune);
  }
}

function fetchCommune(){
  console.log(this);
  insee=this.getAttribute("data-insee");
  console.log(insee);
  let url = 'services/getDetails.php?insee='+insee;
  fetchFromJson(url)
  .then(processAnswer)
  .then(displayCommune);
}

/**
 * Cette fonction affiche les informations détaillées à l’intérieur de <div id="details">
 * commune objet commune 
 */
function displayCommune(commune){
  body = "";
  debut="<table>\n\t<tbody>\n\t";
  fin="</tbody>\n\t</table>";
  console.log(commune);
  console.log(commune.insee);
  for (let elt of ['insee', 'nom', 'nom_terr', 'surface', 'perimetre', 'pop2016', 'lat', 'lon']){
    body += "<tr>\n\t\t<td>"+elt+"</td><td>"+commune[elt]+"</td>\n\t\t</tr>"
  }  
  document.getElementById("details").innerHTML=debut+body+fin;
  createDetailMap(commune);
}



/**
 * Recentre la carte principale autour d'une zone rectangulaire
 * elt doit comporter les attributs dataset.min_lat, dataset.min_lon, dataset.max_lat, dataset.max_lon, 
 */
function centerMapElt(elt){
  let ds = elt.dataset;
  map.fitBounds([[ds.min_lat,ds.min_lon],[ds.max_lat,ds.max_lon]]);
}
