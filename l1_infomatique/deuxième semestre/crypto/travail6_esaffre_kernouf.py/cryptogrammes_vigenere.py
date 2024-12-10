#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cryptogrammes_vigenere` module
:author: FIL - Faculté des Sciences et Technologies -  Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: février 2019

Quelques cryptogrammes à décrypter.
Tous ont été obtenus par un chiffrement de Vigenere. 

Pour les trois premiers de ces cryptogrammes, la clé utilisée est déterminée par un prénom dont 
chacune des lettres doit être convertie en son indice dans l'alphabet latin capital non accentué.
Ces prénoms ont été chiffrés par le procédé de César ou par chiffrement affine. Voici les prénoms
chiffrés :


cryptogramme 1 : 'NIER', chiffrement césar
cryptogramme 2 : 'GLBI', chiffrement césar
cryptogramme 3 : 'MHLJFUO', chiffrement affine, le prénom contient un A et un O

Le quatrième cryptogramme est une URL chiffrée avec une clé obtenue elle aussi à partir d'un prénom 
de longueur 7.

Le cinquième cryptogramme est un texte français (sans caractères accentués) chiffré avec une clé de 
longueur 6. Quel est le prénom qui se cache dans la clé ?
"""


CRYPTOGRAMMES = [
    'UE PRKAYNDAKJRTMLLA BI FXYTMUDEFNDSRIXRACZAMOSRFIHEBXYRHCI CCENQIPAMKMSRIJUFIZE CI',
    
    'U5lzv{ern.hp)zi\x00{\x01$\x01n\x00w+z\x03+l)z+pw\x04m+usw+y}i\x7fn\x01\x0eL)ze+osqxn.hpl\x03i+xtj}n|x+}}yux\x03v~)ovon|x~\x13Tpl}\x02i+lsv\x7fn\x01$wn.f\x00}.qlr\x01$y0otlr\x01i+uo$|~sxp\x13Z+l}\x02iy}s$l)ri~)~plr\x01m}|.u\x000}r+ws$qjwx+z\x03+\x00w.qzvsr\x7f7\x18',
    
    'ZNlQ`_RXAl[W_H\x1b\n:,O-t\x06e\x04xs-kvu\nq.ph1j\x07\x01\x00:or \x08m\x01\x00d1l?m\x03\x01rsu\x0b,rr#}a8xwtqv k,rr#~i|u.?6= |u\x00rf\x05i\x07z\x18}r\x03t},rr#Thyy~ru\x03e\x0c,M\x1701A8ywql13P:\x18:#j y\x02ovw>i\x04,prd\x06c\x07\x01~-gv \x05{|qh1dyz\x01-o8a\r\x00}ox\x04 |q.yd1l\x01s|r#d \x0b\x01\x01:gvs\x01s|rh1?"9.Qh\x04 ~x}}sve\x0b:\x18:#bu?\x05.\x7fh~a\n}\x03nwvsE\x02}\x02v1d},~nu\x05i{\x01zvh\x03 W\x16;-X\x7f \x08m\x00\x01ltu\x04us\x7f#\x02u\x01,o\x03dzt8\x01|-w\x03e\x0b,z|qx {{\x03-h\x05 \rzs-w\x03e\x0b\x7fs-d\x06t\x07\x01\x00-gv \x0b{|-fya\x08qo\x021\x1b-8_}{#to\x05|}\x7fwvm}z\x02-h\x05a\x01\x00;vo1a\r\x7f\x01v#\x04i\x06s\x03ylvr8}\x03r#\x04a8yw\x00h1e\x0c,\x01|q1a\x06m\x02|pze8K\x18:#eo\r\x00.q*rb\x07~r-q\x00n8G.vo1e\x0cmw\x01#\x7fo\nyoy/1myu\x01-l} ~u|vw1py~.\x00*rv}~s\x7f#vt\nq.ph}u\x01\x16r4x\x7f {\x05qyr\x05h\x11yw~xv \x08m\x00nq\x00iy}\x03r#}e\x7fq\x00rpvn\x0c,v\x06s\x00t}zr\x02#ua\x06\x7f.\x02q1e\x0cm\x02-g8i\n~w\x01dsi\x04u\x02r\ryy\x08q\x00td\x04t\nu\x7f\x02h?\nE,Q|p~e\x06\x00.ph}a8\x7fs-w\x03a|\x01w\x00l\x05-\x01x.L\r> dq.}d\x03t\x01o\x03ylvr8q|-t\x06e\x0b\x00w|q1i\x06\x00s\x7fsvl\x04m.\x00r\x7f \x0e{w\x00l\x7f \x0b\x01\x00-x\x7f \x0c{|-s}e\r~|vfya\np.rq\x1bl\ru.qh~a\x06po{w1s?uz-qv ~mw\x00dzt8|o\x00#vx\x08~s\x00#ue8x\x03v#~a\novru1s\r~.yh\x04 \x08usqv1c\x00m\x7f\x02h\x1bf\x07u\x01-t\x06\'\x01x.zr\x7ftyu\x02-r\x06 |q\x01ph\x7fdyu\x02-gvs8\x02}\x06dxe\r~\x01;\r> [q.\x7fh\x01r\x07ovr#vtyu\x02:l} ~{|qh1?"9.Wh1l?uu{r\x03eF\x16;-F\x00m\x05q|\x01#\x04e8\x00s\x7fpzny,qrw1i\x06owqh\x7ft8K\x18:#aa\n,zn#wu\x01\x00s-s\x03e{u~vwve8p\x03-mvu\x06q.ur~m},\x7f\x02l1a\x04xo-rtc\r|s\x7f#\x06n},~ydte8xwouv."9.Ph\x05 \x01zqvgvn\x0c,s\x02w>i\x04,\x03{#\x03ez{|ql\x04s}ys{w1?"9.Zrzn\x0b,rr#ue\r\x04.uh\x06r}\x7f.}o\x06s8\x00o\x7fg?\nE,S{#\x02u\x07u.pr\x7fs\x01\x7f\x02n#te8~sor\x7fd\x01\x7f\x01rpvn\x0c,M\x1701E\x06,zn#\x03ey|~nuzt\x01{|-gv {q\x02-l\x7fd\x01\x02wqx1s\r~.zr\x7f {tszl\x7f."9.\\x1e\x0c,q|p~e\x06\x00.yh1r}\x02w\x01h\x04-\x0e{\x03\x00#P\nE,S{#\x01a\x0b\x7fo{w1e\x06,o\x02w\x00b\r\x7f.qh\x07a\x06\x00.yd1c\x07\x01\x00-gv j{{r1\x1b-8]\x034|1fyu\x01nl\x05-\x01x.L\r> ax.}uvnyu\x02-x\x7fe8o}{v\x06l\x0cm\x02vr\x7f |3syhxa\x06os;#3\n',

    'hv{x~E3/hy6#toirlltl2otn7#toi1JptqjrgflpjZiilvp}i',

    'Cyrzx-ou$qqrpt1~isnettm-cyrzx-rrz $$qt$q$pqu$mkr"a1pi#z ~mm{u ({y!"v!"w-fetuhr| r,eyne$,x qu(qv-xo&~i-ehvr$qg %qv$kcv,t|wr1xyv"dvye{fe$,y{g r"kzgn&mxvqn1#s#u rxpr| u{rp"t${y$gr1#s"te1olrh uq$!gr(ugr"dz s{u "{y "szytykfzqv-ea$,my"fr"x-vo\'vs#ts1 mzrlzrmrt #"+vn %3e}re}xi-oo  mrwr1%e$ke$,g4gs&9e:fi$q$zqn%ui#t !"$}nu&{x-or1%$qqnt,z|ws1mpygz1!v|wvv~$zt *,pn"dv,hrwx1ol|ue%,p4wnv,s#"bzqr-or1%$rut1pe{u %{r-du$qe#"o\',fvgn1yv-z  3i!v "mw-fa  $!qn1ny ga\',wv"m$,|-gtrux-fa  $!qn1ny ga\',my"n8&$nwrrux-cp"mvromvzx-ra%,hr"p${fygmv,qnks1qzvfe~yi{v ~~$&"n8qw""pr $qcn%,w|p s"vrcu1#s#u  3e$gz1ps{e x"i g #"+#pe1ol|ue1m$sci$q$twe&!i "drzw-ne1os#noz~w|p $qx|wr1{y-uo ,e ti(qi-oaz $!wp"{w|ps1zs{"pr $~w\'zx${)a$~m$g "mw-gn1oi-ea%,my"fzzm ci&,tnt  3}-cv!uv-rl\' $~w\'\'zi-ue\'xi-uo}"xvqn1~i"qu$zi "drzw-xo&~i-rr!|vr"b\'~inw v!$nvtvzh g }3e}te%9qvfi1{y-ne1xi{fe~mm{"p!"v-tet{qzgntqv-xo&~i-ve !e"kvv,qnks1ol|ue1}yv"sv,z|kt1!s#u }qw-lo\'~w-su8up-va$pi-c $qzrpi$,i{"cv,gnu }q$zke\'%$~we1#s#u r&i("a1revte1|p#vo&,u#g uq$pqn&ur#gr1m$sci$q$ygs1oi{v "mw-fa  $yg t{yyqi$,g4gs&,h4cl}qv-xoz~$$qt$q$pql}qk#g ~xpr"y1}yr"p!"v-fo zi "p}"w-f\'y"qnpi&q$n"n!!vr"svolr"dvys{ut$mxvqn1zs#u r|trnlv~s{u uqw|tmruw-ol}q$\'qlrzhr"mruw-fe1pi#z tts!gs1x+#pe1{y-divz$znlv,}|na pi-gs&,hnps1 s{"b\'~inw !"$oke ,qyne1z+rut1|e!"drzw-uo ,f#ter"$!k ~xpr"y!xe{fe1qw""drzw-uo ,f#ter"$vn  3}-c r|tnte~yi{v "mw-fe1|v|dlvyi-oaz $!wp"{w|ps1}yr"m}xi-{o}mrqg  q$!qi&,tnu umr!"s!z$owrvmy-gn1oi-ea%,i"cn&,h|pnv,u#g ({y!"n8mzr| "mw-gn(ui-fe1os{vi "i "a1revte1xi!"cvzx-ra%,hnps1xi-eo\'xsvt vz$nvtvzhnpt1x+u{p!!lrvi#"i-te&{y "o\',p4gvvzx#gl}q$ntrz#ir"dv,q "x1"rr"sv"pr"s!xy"ko ,w4qfw~i-c ({y!"fruvr"lv,x|wr1pi!"dzrjrte !w-ue$#mpgs1ps{v }3i{ue~npr"c!zw"kt\'q$"qu&,s#"pr~xvg uq$y)o$se{ksr!m|p #"m-xo\' $rop}{mr"p\'uw-te&{y pe$,gugz1yv-z vz$rupv~e{v #"i-ee&!i-hoz $vn v x-cr$uzr"o$,hr"dv"|-eh! i!"l8"rr"o\',fvgn1yv-z v x-fa  $!qn1ny ga\',s#"bzqr-or1%${)e%!$}cs1pe{u %{r-du$qe#"auyi"vo  $~w\'zx${)y1 svv "mw-fo o$$qu%,k#gt&q~-uo ,vrvo\'~$|w %{r-cr$uzrg vz$sci%mr""lv $pgn&,tnu umr!"lv,g|wl!uv-quz,qnks1 y}ro%{r!"q\'3my"tr~hr"a1mv kvv~$rp tq$pcs1#s#u rxpr| ({m "sz,qyne1&sycnuq$rut1pe{u %{r-du$qe#"dv,hrwx1ol|ue%,p4wnv,s#"bzqr-gl}q$\'"e%!$|w sui{"e}xi-p\'+,i!v "mw'
    
]
    
    
