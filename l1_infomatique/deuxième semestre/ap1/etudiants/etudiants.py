#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_
:date: janvier 2019
:last revised: 2020-01-21
:Fournit :
	 - L_ETUDIANTS = liste d'étudiants
		étudiant = dict('nip' : XXX, 'nom' : XXX, 'prenom' : XXX, 'formation' : XXX, 'groupe' : XXX)
"""

L_ETUDIANTS = [
	{'nip' : '49284201',
	 'nom' : 'Remy',
	 'prenom' : 'Anne',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

    	{'nip' : '49578071',
	 'nom' : 'Mary',
	 'prenom' : 'Josette',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48106866',
	 'nom' : 'Blin',
	 'prenom' : 'Andrée',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48107874',
	 'nom' : 'Jean',
	 'prenom' : 'Benoît',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

        {'nip' : '48348142',
	 'nom' : 'Mary',
	 'prenom' : 'Paul',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48404608',
	 'nom' : 'Joly',
	 'prenom' : 'Cécile',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49029375',
	 'nom' : 'Riou',
	 'prenom' : 'Christiane',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48264948',
	 'nom' : 'Joly',
	 'prenom' : 'David',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48686474',
	 'nom' : 'Gros',
	 'prenom' : 'David',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49905981',
	 'nom' : 'Adam',
	 'prenom' : 'Eugène',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48283487',
	 'nom' : 'Blot',
	 'prenom' : 'Frédérique',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49903794',
	 'nom' : 'Huet',
	 'prenom' : 'Grégoire',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49693913',
	 'nom' : 'Blot',
	 'prenom' : 'Hortense',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49784258',
	 'nom' : 'Pons',
	 'prenom' : 'Isaac',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49278199',
	 'nom' : 'Remy',
	 'prenom' : 'Inès',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48183347',
	 'nom' : 'Riou',
	 'prenom' : 'Julien',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48864953',
	 'nom' : 'Lamy',
	 'prenom' : 'Joseph',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48029659',
	 'nom' : 'Huet',
	 'prenom' : 'Léon',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48705436',
	 'nom' : 'Jean',
	 'prenom' : 'Lorraine',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49400464',
	 'nom' : 'Roux',
	 'prenom' : 'Luc',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49219796',
	 'nom' : 'Remy',
	 'prenom' : 'Margaud',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48087351',
	 'nom' : 'Paul',
	 'prenom' : 'Marianne',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48270708',
	 'nom' : 'Adam',
	 'prenom' : 'Margot',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48138012',
	 'nom' : 'Joly',
	 'prenom' : 'Margot',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48892850',
	 'nom' : 'Huet',
	 'prenom' : 'Nathalie',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48659185',
	 'nom' : 'Paul',
	 'prenom' : 'Nathalie',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48971263',
	 'nom' : 'Lamy',
	 'prenom' : 'Pénélope',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49977680',
	 'nom' : 'Brun',
	 'prenom' : 'Roger',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49337187',
	 'nom' : 'Jean',
	 'prenom' : 'Susanne',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48889927',
	 'nom' : 'Ruiz',
	 'prenom' : 'Yves',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48700998',
	 'nom' : 'Roux',
	 'prenom' : 'Yves',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48114453',
	 'nom' : 'Vaillant',
	 'prenom' : 'Nath',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48852075',
	 'nom' : 'Guillaume',
	 'prenom' : 'Auguste',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48284548',
	 'nom' : 'Deschamps',
	 'prenom' : 'Sylvie',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48469138',
	 'nom' : 'Bruneau',
	 'prenom' : 'Marguerite',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49185975',
	 'nom' : 'Maillard',
	 'prenom' : 'Corinne',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48070863',
	 'nom' : 'Guichard',
	 'prenom' : 'Lucas',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48501456',
	 'nom' : 'Garcia',
	 'prenom' : 'Margaux',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48146768',
	 'nom' : 'Marchand',
	 'prenom' : 'Victor',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48722497',
	 'nom' : 'Guillaume',
	 'prenom' : 'Brigitte',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49372454',
	 'nom' : 'Loiseau',
	 'prenom' : 'Geneviève',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48905257',
	 'nom' : 'Marchand',
	 'prenom' : 'Zacharie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48400323',
	 'nom' : 'Toussaint',
	 'prenom' : 'Lucas',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49626047',
	 'nom' : 'Guichard',
	 'prenom' : 'Agnès',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49106543',
	 'nom' : 'Marchand',
	 'prenom' : 'Guy',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49409713',
	 'nom' : 'Nicolas',
	 'prenom' : 'Dominique',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49027535',
	 'nom' : 'Bruneau',
	 'prenom' : 'Astrid',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49532769',
	 'nom' : 'Dos Santos',
	 'prenom' : 'Noémi',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48000715',
	 'nom' : 'Guillaume',
	 'prenom' : 'Julie',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49651046',
	 'nom' : 'Marchal',
	 'prenom' : 'Noël',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48722158',
	 'nom' : 'Deschamps',
	 'prenom' : 'Marcel',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49505872',
	 'nom' : 'Bruneau',
	 'prenom' : 'Édouard',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49013936',
	 'nom' : 'Gaillard',
	 'prenom' : 'Éric',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48655272',
	 'nom' : 'Hoareau',
	 'prenom' : 'Auguste',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48599589',
	 'nom' : 'Nicolas',
	 'prenom' : 'Guy',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49002981',
	 'nom' : 'Hoareau',
	 'prenom' : 'Emmanuelle',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48991647',
	 'nom' : 'Dos Santos',
	 'prenom' : 'Madeleine',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49203915',
	 'nom' : 'Bruneau',
	 'prenom' : 'Gérard',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48008539',
	 'nom' : 'Toussaint',
	 'prenom' : 'Gabrielle',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48435063',
	 'nom' : 'Nicolas',
	 'prenom' : 'Adrien',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49930629',
	 'nom' : 'Vaillant',
	 'prenom' : 'Agathe',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48807903',
	 'nom' : 'Bruneau',
	 'prenom' : 'Victor',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49631022',
	 'nom' : 'Loiseau',
	 'prenom' : 'Anne',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48612877',
	 'nom' : 'Guillaume',
	 'prenom' : 'Eugène',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49417355',
	 'nom' : 'Bruneau',
	 'prenom' : 'Thierry',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48298403',
	 'nom' : 'Bonneau',
	 'prenom' : 'Laurent',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48154054',
	 'nom' : 'Toussaint',
	 'prenom' : 'Nicolas',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48611227',
	 'nom' : 'Bruneau',
	 'prenom' : 'Olivie',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49997648',
	 'nom' : 'Lacombe',
	 'prenom' : 'Rémy',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49126747',
	 'nom' : 'Maurice',
	 'prenom' : 'Théophile',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48796417',
	 'nom' : 'Legendre',
	 'prenom' : 'Hélène',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49586831',
	 'nom' : 'Briand',
	 'prenom' : 'Émilie',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48563685',
	 'nom' : 'Gerard',
	 'prenom' : 'Laure',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49176444',
	 'nom' : 'Benard',
	 'prenom' : 'Xavier',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49493402',
	 'nom' : 'Lagarde',
	 'prenom' : 'Marie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48890905',
	 'nom' : 'Benard',
	 'prenom' : 'Colette',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48280757',
	 'nom' : 'Girard',
	 'prenom' : 'Paul',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48140254',
	 'nom' : 'Renard',
	 'prenom' : 'Camille',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49476925',
	 'nom' : 'Lagarde',
	 'prenom' : 'Bernard',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48515699',
	 'nom' : 'Girard',
	 'prenom' : 'Lorraine',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48010456',
	 'nom' : 'Durand',
	 'prenom' : 'Emmanuel',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49247956',
	 'nom' : 'Benard',
	 'prenom' : 'Stéphane',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49835161',
	 'nom' : 'Girard',
	 'prenom' : 'Maryse',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49406735',
	 'nom' : 'Renaud',
	 'prenom' : 'Alexandria',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49982806',
	 'nom' : 'Godard',
	 'prenom' : 'Philippe',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48306335',
	 'nom' : 'Evrard',
	 'prenom' : 'Audrey',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49149310',
	 'nom' : 'Arnaud',
	 'prenom' : 'Jacques',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48686877',
	 'nom' : 'Renaud',
	 'prenom' : 'Frédéric',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49006604',
	 'nom' : 'Durand',
	 'prenom' : 'Olivie',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49440744',
	 'nom' : 'Girard',
	 'prenom' : 'Denise',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48321723',
	 'nom' : 'Benard',
	 'prenom' : 'Jérôme',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49082198',
	 'nom' : 'Renard',
	 'prenom' : 'Xavier',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49397925',
	 'nom' : 'Renard',
	 'prenom' : 'Olivie',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49644183',
	 'nom' : 'Briand',
	 'prenom' : 'Guy',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48330312',
	 'nom' : 'Girard',
	 'prenom' : 'André',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49224819',
	 'nom' : 'Durand',
	 'prenom' : 'Margaux',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48787492',
	 'nom' : 'Legendre',
	 'prenom' : 'Gilbert',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49538746',
	 'nom' : 'Charpentier',
	 'prenom' : 'Lucie',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49614677',
	 'nom' : 'Pottier',
	 'prenom' : 'Anastasie',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48703862',
	 'nom' : 'Olivier',
	 'prenom' : 'Margot',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48276429',
	 'nom' : 'Guillet',
	 'prenom' : 'Maggie',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48873974',
	 'nom' : 'Boucher',
	 'prenom' : 'Augustin',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49219584',
	 'nom' : 'Mercier',
	 'prenom' : 'Martin',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48203621',
	 'nom' : 'Charpentier',
	 'prenom' : 'Dorothée',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49157177',
	 'nom' : 'Pierre',
	 'prenom' : 'Arnaude',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49214502',
	 'nom' : 'Barthelemy',
	 'prenom' : 'Marc',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48831084',
	 'nom' : 'Mercier',
	 'prenom' : 'Anouk',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49837694',
	 'nom' : 'Barthelemy',
	 'prenom' : 'Louis',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48767215',
	 'nom' : 'Faivre',
	 'prenom' : 'David',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49889658',
	 'nom' : 'Mercier',
	 'prenom' : 'Lucas',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49247245',
	 'nom' : 'Traore',
	 'prenom' : 'Marcel',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48691669',
	 'nom' : 'Georges',
	 'prenom' : 'Philippe',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48867322',
	 'nom' : 'Mercier',
	 'prenom' : 'Michèle',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48231381',
	 'nom' : 'Chauvet',
	 'prenom' : 'Christelle',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49802289',
	 'nom' : 'Tessier',
	 'prenom' : 'Guy',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49964827',
	 'nom' : 'Mercier',
	 'prenom' : 'Nathalie',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48883676',
	 'nom' : 'Fischer',
	 'prenom' : 'Thierry',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48026829',
	 'nom' : 'Guilbert',
	 'prenom' : 'Alexandrie',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49457907',
	 'nom' : 'Tessier',
	 'prenom' : 'Adrienne',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48601894',
	 'nom' : 'Gimenez',
	 'prenom' : 'Jules',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49733090',
	 'nom' : 'Bouchet',
	 'prenom' : 'Amélie',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48765781',
	 'nom' : 'Duhamel',
	 'prenom' : 'Audrey',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48285862',
	 'nom' : 'Duhamel',
	 'prenom' : 'Marcelle',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49234446',
	 'nom' : 'Meunier',
	 'prenom' : 'Paul',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48365981',
	 'nom' : 'Gimenez',
	 'prenom' : 'Antoinette',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48628004',
	 'nom' : 'Duhamel',
	 'prenom' : 'Anne',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48032431',
	 'nom' : 'Pottier',
	 'prenom' : 'Olivier',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48631686',
	 'nom' : 'Olivier',
	 'prenom' : 'Emmanuel',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49358094',
	 'nom' : 'Gautier',
	 'prenom' : 'Martin',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48782925',
	 'nom' : 'Mathieu',
	 'prenom' : 'Alexandria',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48663829',
	 'nom' : 'Chauveau',
	 'prenom' : 'Luce',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49052264',
	 'nom' : 'Bourgeois',
	 'prenom' : 'Eugène',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48482625',
	 'nom' : 'Foucher',
	 'prenom' : 'Charles',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48220793',
	 'nom' : 'Olivier',
	 'prenom' : 'Émile',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48487572',
	 'nom' : 'Bourgeois',
	 'prenom' : 'Élisabeth',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49829612',
	 'nom' : 'Berthelot',
	 'prenom' : 'Georges',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48635029',
	 'nom' : 'Carlier',
	 'prenom' : 'Maggie',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49646130',
	 'nom' : 'Poirier',
	 'prenom' : 'Agnès',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48440496',
	 'nom' : 'Gimenez',
	 'prenom' : 'Gilles',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49362350',
	 'nom' : 'Faivre',
	 'prenom' : 'Jean',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49623586',
	 'nom' : 'Chauvet',
	 'prenom' : 'Célina',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48652100',
	 'nom' : 'Chauvet',
	 'prenom' : 'Guillaume',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49485200',
	 'nom' : 'Charpentier',
	 'prenom' : 'Anaïs',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48274756',
	 'nom' : 'Fischer',
	 'prenom' : 'Richard',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48600195',
	 'nom' : 'Chauveau',
	 'prenom' : 'Stéphane',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49673940',
	 'nom' : 'Mathieu',
	 'prenom' : 'Antoine',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48623455',
	 'nom' : 'Charpentier',
	 'prenom' : 'Mathilde',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48181898',
	 'nom' : 'Faivre',
	 'prenom' : 'Véronique',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49606614',
	 'nom' : 'Tessier',
	 'prenom' : 'Océane',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48502832',
	 'nom' : 'Mercier',
	 'prenom' : 'Patricia',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48011004',
	 'nom' : 'Chauveau',
	 'prenom' : 'Christiane',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49595323',
	 'nom' : 'Sanchez',
	 'prenom' : 'Maggie',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48672035',
	 'nom' : 'Blondel',
	 'prenom' : 'Grégoire',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49016562',
	 'nom' : 'Meunier',
	 'prenom' : 'Suzanne',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49807034',
	 'nom' : 'Fouquet',
	 'prenom' : 'Suzanne',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49931589',
	 'nom' : 'Boucher',
	 'prenom' : 'Roland',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48544171',
	 'nom' : 'Peltier',
	 'prenom' : 'Eugène',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48831644',
	 'nom' : 'Roussel',
	 'prenom' : 'Grégoire',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48024183',
	 'nom' : 'Fouquet',
	 'prenom' : 'Thibaut',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48037529',
	 'nom' : 'Gautier',
	 'prenom' : 'David',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48264586',
	 'nom' : 'Duhamel',
	 'prenom' : 'Chantal',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48786907',
	 'nom' : 'Le Goff',
	 'prenom' : 'Inès',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49227392',
	 'nom' : 'Le Goff',
	 'prenom' : 'Nathalie',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48590187',
	 'nom' : 'Rodrigues',
	 'prenom' : 'Christiane',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49640973',
	 'nom' : 'Rodrigues',
	 'prenom' : 'Matthieu',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49001360',
	 'nom' : 'Rodrigues',
	 'prenom' : 'Emmanuelle',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48242251',
	 'nom' : 'Blanchard',
	 'prenom' : 'Denis',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49631499',
	 'nom' : 'Blanchard',
	 'prenom' : 'Guillaume',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49191204',
	 'nom' : 'Blanchard',
	 'prenom' : 'Christelle',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48560877',
	 'nom' : 'Marechal',
	 'prenom' : 'Marine',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49004050',
	 'nom' : 'Ferreira',
	 'prenom' : 'Denis',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48294914',
	 'nom' : 'Poulain',
	 'prenom' : 'Rémy',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48616182',
	 'nom' : 'Gauthier',
	 'prenom' : 'Franck',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49903531',
	 'nom' : 'Teixeira',
	 'prenom' : 'Robert',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48612648',
	 'nom' : 'Germain',
	 'prenom' : 'Pénélope',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48868368',
	 'nom' : 'Rey',
	 'prenom' : 'Pierre',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49348227',
	 'nom' : 'Chretien',
	 'prenom' : 'Margaret',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48004365',
	 'nom' : 'Lacroix',
	 'prenom' : 'Denis',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49761378',
	 'nom' : 'De Oliveira',
	 'prenom' : 'Thibaut',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49928803',
	 'nom' : 'Pasquier',
	 'prenom' : 'Corinne',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48389794',
	 'nom' : 'Gauthier',
	 'prenom' : 'Monique',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49196091',
	 'nom' : 'Pasquier',
	 'prenom' : 'Marcel',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48670141',
	 'nom' : 'Ferreira',
	 'prenom' : 'Susan',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48969339',
	 'nom' : 'Grondin',
	 'prenom' : 'Anne',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48684563',
	 'nom' : 'Gregoire',
	 'prenom' : 'Élise',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49177811',
	 'nom' : 'Fontaine',
	 'prenom' : 'François',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49670174',
	 'nom' : 'Chartier',
	 'prenom' : 'Inès',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49825905',
	 'nom' : 'Poulain',
	 'prenom' : 'Patricia',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49287018',
	 'nom' : 'Gauthier',
	 'prenom' : 'Claude',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48614014',
	 'nom' : 'Schneider',
	 'prenom' : 'Sabine',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48595296',
	 'nom' : 'Pasquier',
	 'prenom' : 'Christiane',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49269299',
	 'nom' : 'Petitjean',
	 'prenom' : 'Margot',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49247644',
	 'nom' : 'Letellier',
	 'prenom' : 'Audrey',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48451475',
	 'nom' : 'Chevalier',
	 'prenom' : 'Jacques',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48784214',
	 'nom' : 'Renault',
	 'prenom' : 'Sophie',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48882674',
	 'nom' : 'Michel',
	 'prenom' : 'Pierre',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49024356',
	 'nom' : 'Daniel',
	 'prenom' : 'Maryse',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49371304',
	 'nom' : 'Chevalier',
	 'prenom' : 'Laurent',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48852212',
	 'nom' : 'Chevalier',
	 'prenom' : 'Julie',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48536805',
	 'nom' : 'Gonzalez',
	 'prenom' : 'Aurélie',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49552001',
	 'nom' : 'Chevallier',
	 'prenom' : 'Mathilde',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49165880',
	 'nom' : 'Renault',
	 'prenom' : 'Frédéric',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49145944',
	 'nom' : 'Chevalier',
	 'prenom' : 'Vincent',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48399702',
	 'nom' : 'Renault',
	 'prenom' : 'Margot',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49873805',
	 'nom' : 'Chevalier',
	 'prenom' : 'Matthieu',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48772907',
	 'nom' : 'Gonzalez',
	 'prenom' : 'Pénélope',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48607297',
	 'nom' : 'Chevallier',
	 'prenom' : 'Marie',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48462393',
	 'nom' : 'Renault',
	 'prenom' : 'Denise',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48632899',
	 'nom' : 'Martel',
	 'prenom' : 'Victor',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48607545',
	 'nom' : 'Da Silva',
	 'prenom' : 'François',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49860658',
	 'nom' : 'Le Gall',
	 'prenom' : 'Lucas',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49507934',
	 'nom' : 'Michel',
	 'prenom' : 'Antoine',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49435534',
	 'nom' : 'Brunel',
	 'prenom' : 'Arthur',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48893978',
	 'nom' : 'Chevalier',
	 'prenom' : 'Éléonore',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48280508',
	 'nom' : 'Letellier',
	 'prenom' : 'Alexandre',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48419022',
	 'nom' : 'Gonzalez',
	 'prenom' : 'Astrid',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48733573',
	 'nom' : 'Gosselin',
	 'prenom' : 'Jean',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48736286',
	 'nom' : 'Gosselin',
	 'prenom' : 'Robert',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49344333',
	 'nom' : 'Descamps',
	 'prenom' : 'Colette',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49035638',
	 'nom' : 'Vincent',
	 'prenom' : 'Astrid',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48777980',
	 'nom' : 'Hernandez',
	 'prenom' : 'Rémy',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48577697',
	 'nom' : 'Legrand',
	 'prenom' : 'Marguerite',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48467415',
	 'nom' : 'Bonnin',
	 'prenom' : 'Gilles',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48436104',
	 'nom' : 'Leblanc',
	 'prenom' : 'Honoré',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48292895',
	 'nom' : 'Lemonnier',
	 'prenom' : 'Gérard',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48079411',
	 'nom' : 'Julien',
	 'prenom' : 'Henriette',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48171715',
	 'nom' : 'Marion',
	 'prenom' : 'Xavier',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48173978',
	 'nom' : 'Martinez',
	 'prenom' : 'Vincent',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48096536',
	 'nom' : 'Coulon',
	 'prenom' : 'Luce',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49060756',
	 'nom' : 'Alexandre',
	 'prenom' : 'Noël',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49312725',
	 'nom' : 'Marion',
	 'prenom' : 'Eugène',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49827823',
	 'nom' : 'Rolland',
	 'prenom' : 'Capucine',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49634515',
	 'nom' : 'Masson',
	 'prenom' : 'David',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48721081',
	 'nom' : 'Martineau',
	 'prenom' : 'Audrey',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48428161',
	 'nom' : 'Masson',
	 'prenom' : 'Isaac',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48716046',
	 'nom' : 'Fernandes',
	 'prenom' : 'Alix',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49303402',
	 'nom' : 'Cousin',
	 'prenom' : 'Rémy',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49319422',
	 'nom' : 'Gaudin',
	 'prenom' : 'Claudine',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48572101',
	 'nom' : 'Boulanger',
	 'prenom' : 'Frédéric',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49940459',
	 'nom' : 'Leblanc',
	 'prenom' : 'Emmanuel',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49956527',
	 'nom' : 'Besson',
	 'prenom' : 'Anouk',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48712200',
	 'nom' : 'Martineau',
	 'prenom' : 'Chantal',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48686797',
	 'nom' : 'Laurent',
	 'prenom' : 'Véronique',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48915734',
	 'nom' : 'Gaudin',
	 'prenom' : 'Jacqueline',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48212892',
	 'nom' : 'Masson',
	 'prenom' : 'Antoinette',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49709239',
	 'nom' : 'Nguyen',
	 'prenom' : 'Édouard',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49041880',
	 'nom' : 'Bertin',
	 'prenom' : 'Alexandria',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48601497',
	 'nom' : 'Lejeune',
	 'prenom' : 'Raymond',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49621527',
	 'nom' : 'Cousin',
	 'prenom' : 'Monique',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49230874',
	 'nom' : 'Lemoine',
	 'prenom' : 'Victor',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49443000',
	 'nom' : 'Voisin',
	 'prenom' : 'Andrée',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48569506',
	 'nom' : 'Delaunay',
	 'prenom' : 'Inès',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49527437',
	 'nom' : 'Delannoy',
	 'prenom' : 'Julien',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49867280',
	 'nom' : 'Collin',
	 'prenom' : 'Marguerite',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48218552',
	 'nom' : 'Lemonnier',
	 'prenom' : 'Mathilde',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49443899',
	 'nom' : 'Carpentier',
	 'prenom' : 'Émile',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48674549',
	 'nom' : 'Martinez',
	 'prenom' : 'Paul',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48552589',
	 'nom' : 'Perrin',
	 'prenom' : 'Catherine',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48842359',
	 'nom' : 'Rolland',
	 'prenom' : 'Alexandria',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49798783',
	 'nom' : 'Laurent',
	 'prenom' : 'Alice',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48366344',
	 'nom' : 'Lebrun',
	 'prenom' : 'Émile',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49942906',
	 'nom' : 'Boutin',
	 'prenom' : 'Gabriel',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48591248',
	 'nom' : 'Rolland',
	 'prenom' : 'Bertrand',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48588827',
	 'nom' : 'Legrand',
	 'prenom' : 'Éléonore',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49084717',
	 'nom' : 'Fernandez',
	 'prenom' : 'Antoine',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49939499',
	 'nom' : 'Bonnin',
	 'prenom' : 'Robert',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48277261',
	 'nom' : 'Turpin',
	 'prenom' : 'Alphonse',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48815219',
	 'nom' : 'Rolland',
	 'prenom' : 'Christophe',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48346842',
	 'nom' : 'Leblanc',
	 'prenom' : 'David',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49073636',
	 'nom' : 'Salmon',
	 'prenom' : 'Colette',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49402760',
	 'nom' : 'Perrin',
	 'prenom' : 'Martin',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48236904',
	 'nom' : 'Martinez',
	 'prenom' : 'Suzanne',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49030492',
	 'nom' : 'Moulin',
	 'prenom' : 'Alexandre',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48898444',
	 'nom' : 'Legrand',
	 'prenom' : 'Joseph',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48452257',
	 'nom' : 'Martins',
	 'prenom' : 'Charles',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48678319',
	 'nom' : 'Lejeune',
	 'prenom' : 'Laurence',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49722836',
	 'nom' : 'Martins',
	 'prenom' : 'Théophile',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48949335',
	 'nom' : 'Etienne',
	 'prenom' : 'Élodie',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48831673',
	 'nom' : 'Breton',
	 'prenom' : 'Pénélope',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49825231',
	 'nom' : 'Leblanc',
	 'prenom' : 'Andrée',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49951741',
	 'nom' : 'Martinez',
	 'prenom' : 'Frédérique',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49720801',
	 'nom' : 'Moulin',
	 'prenom' : 'Sabine',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49612189',
	 'nom' : 'Lemoine',
	 'prenom' : 'Hugues',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48382428',
	 'nom' : 'Legrand',
	 'prenom' : 'Guy',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49819529',
	 'nom' : 'Leblanc',
	 'prenom' : 'Louise',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48067414',
	 'nom' : 'Raymond',
	 'prenom' : 'Henri',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49603707',
	 'nom' : 'Voisin',
	 'prenom' : 'Richard',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49322410',
	 'nom' : 'Raymond',
	 'prenom' : 'Victor',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48418537',
	 'nom' : 'Moulin',
	 'prenom' : 'Anaïs',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48922140',
	 'nom' : 'Lebrun',
	 'prenom' : 'William',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49433174',
	 'nom' : 'Morvan',
	 'prenom' : 'Jules',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49036908',
	 'nom' : 'Moulin',
	 'prenom' : 'Constance',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49622507',
	 'nom' : 'Leblanc',
	 'prenom' : 'Arthur',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48240197',
	 'nom' : 'Salmon',
	 'prenom' : 'Matthieu',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49948892',
	 'nom' : 'Rolland',
	 'prenom' : 'Michel',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49420086',
	 'nom' : 'Martin',
	 'prenom' : 'André',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49416620',
	 'nom' : 'Lemoine',
	 'prenom' : 'Aurélie',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49515474',
	 'nom' : 'Pichon',
	 'prenom' : 'Susanne',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48128035',
	 'nom' : 'Fernandez',
	 'prenom' : 'Benjamin',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48001349',
	 'nom' : 'Julien',
	 'prenom' : 'Yves',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49035537',
	 'nom' : 'Gaudin',
	 'prenom' : 'Manon',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48199071',
	 'nom' : 'Martins',
	 'prenom' : 'Arthur',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48009296',
	 'nom' : 'Lemonnier',
	 'prenom' : 'Luc',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49747427',
	 'nom' : 'Etienne',
	 'prenom' : 'Philippine',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49614705',
	 'nom' : 'Normand',
	 'prenom' : 'Lucy',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49536497',
	 'nom' : 'Delaunay',
	 'prenom' : 'Éric',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49639490',
	 'nom' : 'Maillot',
	 'prenom' : 'Philippe',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48013639',
	 'nom' : 'Francois',
	 'prenom' : 'Gilles',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49799295',
	 'nom' : 'Buisson',
	 'prenom' : 'Christelle',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49520755',
	 'nom' : 'Francois',
	 'prenom' : 'Christiane',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49265324',
	 'nom' : 'Diallo',
	 'prenom' : 'Célina',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48489927',
	 'nom' : 'Moreno',
	 'prenom' : 'Thomas',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49309468',
	 'nom' : 'Diallo',
	 'prenom' : 'Isaac',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49409792',
	 'nom' : 'Guillon',
	 'prenom' : 'Nicolas',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49301949',
	 'nom' : 'Bourdon',
	 'prenom' : 'Madeleine',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49957164',
	 'nom' : 'Jacquot',
	 'prenom' : 'Étienne',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49166992',
	 'nom' : 'Buisson',
	 'prenom' : 'Rémy',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48999049',
	 'nom' : 'Philippe',
	 'prenom' : 'Amélie',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49908103',
	 'nom' : 'Philippe',
	 'prenom' : 'Christelle',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48290898',
	 'nom' : 'Wagner',
	 'prenom' : 'Édith',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48612997',
	 'nom' : 'Ribeiro',
	 'prenom' : 'Jérôme',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49389483',
	 'nom' : 'Lefevre',
	 'prenom' : 'Alain',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49297908',
	 'nom' : 'Texier',
	 'prenom' : 'Olivier',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49212423',
	 'nom' : 'Riviere',
	 'prenom' : 'Suzanne',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48403854',
	 'nom' : 'Lenoir',
	 'prenom' : 'Laurent',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48583723',
	 'nom' : 'Muller',
	 'prenom' : 'Renée',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48329591',
	 'nom' : 'Techer',
	 'prenom' : 'Élodie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48769879',
	 'nom' : 'Richard',
	 'prenom' : 'René',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49830424',
	 'nom' : 'Leclercq',
	 'prenom' : 'Inès',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48638134',
	 'nom' : 'Didier',
	 'prenom' : 'Maggie',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48811146',
	 'nom' : 'Richard',
	 'prenom' : 'Claudine',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48105743',
	 'nom' : 'Humbert',
	 'prenom' : 'Étienne',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49990954',
	 'nom' : 'Muller',
	 'prenom' : 'Augustin',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48936651',
	 'nom' : 'Riviere',
	 'prenom' : 'Aimé',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49298868',
	 'nom' : 'Didier',
	 'prenom' : 'Maggie',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49714470',
	 'nom' : 'Humbert',
	 'prenom' : 'Capucine',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49716511',
	 'nom' : 'Besnard',
	 'prenom' : 'Isaac',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48171262',
	 'nom' : 'Didier',
	 'prenom' : 'Martine',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48020296',
	 'nom' : 'Besnard',
	 'prenom' : 'Laurence',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48167900',
	 'nom' : 'Lombard',
	 'prenom' : 'Zacharie',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49097248',
	 'nom' : 'Leclercq',
	 'prenom' : 'Sylvie',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48744856',
	 'nom' : 'Navarro',
	 'prenom' : 'Bernadette',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48577504',
	 'nom' : 'Potier',
	 'prenom' : 'Simone',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48714740',
	 'nom' : 'Techer',
	 'prenom' : 'Auguste',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48169174',
	 'nom' : 'Didier',
	 'prenom' : 'Valentine',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48988647',
	 'nom' : 'Humbert',
	 'prenom' : 'Zacharie',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49961257',
	 'nom' : 'Rey',
	 'prenom' : 'Frédéric',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48825362',
	 'nom' : 'Couturier',
	 'prenom' : 'André',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48239703',
	 'nom' : 'Potier',
	 'prenom' : 'Audrey',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49901261',
	 'nom' : 'Berger',
	 'prenom' : 'Émilie',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48283259',
	 'nom' : 'Humbert',
	 'prenom' : 'Isabelle',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49142673',
	 'nom' : 'Lombard',
	 'prenom' : 'Marguerite',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48792663',
	 'nom' : 'Lefevre',
	 'prenom' : 'Margaux',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49111835',
	 'nom' : 'Couturier',
	 'prenom' : 'Patrick',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48811176',
	 'nom' : 'Wagner',
	 'prenom' : 'Céline',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48661248',
	 'nom' : 'Berger',
	 'prenom' : 'Gabrielle',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49050810',
	 'nom' : 'Thomas',
	 'prenom' : 'Gilles',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48055627',
	 'nom' : 'Thomas',
	 'prenom' : 'Alphonse',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49850473',
	 'nom' : 'Pruvost',
	 'prenom' : 'Laurence',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49809982',
	 'nom' : 'Dubois',
	 'prenom' : 'Jean',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48652694',
	 'nom' : 'Gilles',
	 'prenom' : 'Sophie',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48116759',
	 'nom' : 'Gilles',
	 'prenom' : 'Adèle',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49399736',
	 'nom' : 'Dubois',
	 'prenom' : 'Théophile',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48564906',
	 'nom' : 'Thomas',
	 'prenom' : 'Matthieu',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49106991',
	 'nom' : 'Gilles',
	 'prenom' : 'Auguste',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49626414',
	 'nom' : 'Dupuis',
	 'prenom' : 'Paul',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48105973',
	 'nom' : 'Thomas',
	 'prenom' : 'Henriette',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48051174',
	 'nom' : 'Delmas',
	 'prenom' : 'Thibaut',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48832766',
	 'nom' : 'Delmas',
	 'prenom' : 'Bertrand',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49290758',
	 'nom' : 'Pruvost',
	 'prenom' : 'Aimé',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49538605',
	 'nom' : 'Bouvet',
	 'prenom' : 'Marguerite',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49900600',
	 'nom' : 'Mallet',
	 'prenom' : 'Augustin',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48013749',
	 'nom' : 'Millet',
	 'prenom' : 'Antoinette',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49655840',
	 'nom' : 'Hubert',
	 'prenom' : 'Anastasie',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49335811',
	 'nom' : 'Vallet',
	 'prenom' : 'Zoé',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49153772',
	 'nom' : 'Dumont',
	 'prenom' : 'Thibaut',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49711923',
	 'nom' : 'Imbert',
	 'prenom' : 'Richard',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49187847',
	 'nom' : 'Gillet',
	 'prenom' : 'Susan',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48519522',
	 'nom' : 'Aubert',
	 'prenom' : 'Aurélie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49688623',
	 'nom' : 'Imbert',
	 'prenom' : 'Marc',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48830429',
	 'nom' : 'Lecomte',
	 'prenom' : 'Valentine',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48868768',
	 'nom' : 'Valentin',
	 'prenom' : 'Alfred',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49109980',
	 'nom' : 'Benoit',
	 'prenom' : 'Élise',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49224401',
	 'nom' : 'Perret',
	 'prenom' : 'Paul',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49245623',
	 'nom' : 'Dupont',
	 'prenom' : 'Victor',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49799244',
	 'nom' : 'Gillet',
	 'prenom' : 'Richard',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48443437',
	 'nom' : 'Aubert',
	 'prenom' : 'Camille',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48203222',
	 'nom' : 'Dupont',
	 'prenom' : 'Yves',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49206246',
	 'nom' : 'Parent',
	 'prenom' : 'Christelle',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49254987',
	 'nom' : 'Robert',
	 'prenom' : 'Benjamin',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48765277',
	 'nom' : 'Lefort',
	 'prenom' : 'Robert',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48727439',
	 'nom' : 'Pelletier',
	 'prenom' : 'Henri',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48581116',
	 'nom' : 'Perret',
	 'prenom' : 'Édouard',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48958920',
	 'nom' : 'Laporte',
	 'prenom' : 'Danielle',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48187492',
	 'nom' : 'Lefort',
	 'prenom' : 'Christelle',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49889545',
	 'nom' : 'Perret',
	 'prenom' : 'Alphonse',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49376576',
	 'nom' : 'Parent',
	 'prenom' : 'Éléonore',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48978094',
	 'nom' : 'Perrot',
	 'prenom' : 'Georges',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48351270',
	 'nom' : 'Benoit',
	 'prenom' : 'Roland',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48175051',
	 'nom' : 'Benoit',
	 'prenom' : 'Alphonse',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48292928',
	 'nom' : 'Lemaitre',
	 'prenom' : 'Alix',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48673330',
	 'nom' : 'Bonnet',
	 'prenom' : 'Alain',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48726098',
	 'nom' : 'Laporte',
	 'prenom' : 'Margot',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48323278',
	 'nom' : 'Hubert',
	 'prenom' : 'Aimé',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49334164',
	 'nom' : 'Millet',
	 'prenom' : 'Corinne',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49420337',
	 'nom' : 'Aubert',
	 'prenom' : 'Bernadette',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48296553',
	 'nom' : 'Bouvet',
	 'prenom' : 'Christiane',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48735877',
	 'nom' : 'Collet',
	 'prenom' : 'Philippe',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48188793',
	 'nom' : 'Valentin',
	 'prenom' : 'Georges',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48745414',
	 'nom' : 'Pelletier',
	 'prenom' : 'Marie',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48598042',
	 'nom' : 'Laporte',
	 'prenom' : 'Aurore',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49176008',
	 'nom' : 'Schmitt',
	 'prenom' : 'Gilbert',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49421022',
	 'nom' : 'Albert',
	 'prenom' : 'Stéphanie',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49550417',
	 'nom' : 'Pelletier',
	 'prenom' : 'Alain',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49824447',
	 'nom' : 'Aubert',
	 'prenom' : 'Maryse',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49348432',
	 'nom' : 'Gillet',
	 'prenom' : 'Paulette',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48828542',
	 'nom' : 'Valentin',
	 'prenom' : 'Marguerite',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49673776',
	 'nom' : 'Hebert',
	 'prenom' : 'Jeannine',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49957709',
	 'nom' : 'Imbert',
	 'prenom' : 'Xavier',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48786146',
	 'nom' : 'Leconte',
	 'prenom' : 'Alix',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48808936',
	 'nom' : 'Valentin',
	 'prenom' : 'Zacharie',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49984667',
	 'nom' : 'Valentin',
	 'prenom' : 'Luc',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49476089',
	 'nom' : 'Robert',
	 'prenom' : 'Denis',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48919477',
	 'nom' : 'Gillet',
	 'prenom' : 'Arnaude',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '49521202',
	 'nom' : 'Lemaitre',
	 'prenom' : 'Margaud',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48802220',
	 'nom' : 'Pineau',
	 'prenom' : 'Timothée',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48560420',
	 'nom' : 'Roy',
	 'prenom' : 'Julie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49194389',
	 'nom' : 'Thibault',
	 'prenom' : 'Claire',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48238337',
	 'nom' : 'Pineau',
	 'prenom' : 'Laurence',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48594425',
	 'nom' : 'Vasseur',
	 'prenom' : 'Jérôme',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48977219',
	 'nom' : 'Pineau',
	 'prenom' : 'Guillaume',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48138751',
	 'nom' : 'Raynaud',
	 'prenom' : 'Paul',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48274781',
	 'nom' : 'Moreau',
	 'prenom' : 'Hugues',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49309172',
	 'nom' : 'Vasseur',
	 'prenom' : 'Gilbert',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49614346',
	 'nom' : 'Raynaud',
	 'prenom' : 'Marcelle',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48511249',
	 'nom' : 'Raynaud',
	 'prenom' : 'Raymond',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49992456',
	 'nom' : 'Vasseur',
	 'prenom' : 'Célina',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49178500',
	 'nom' : 'Hoarau',
	 'prenom' : 'Arnaude',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49065739',
	 'nom' : 'Bousquet',
	 'prenom' : 'Laurence',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '48318449',
	 'nom' : 'Raynaud',
	 'prenom' : 'Édouard',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49177931',
	 'nom' : 'Moreau',
	 'prenom' : 'Susanne',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49148238',
	 'nom' : 'Le Roux',
	 'prenom' : 'Édouard',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48841681',
	 'nom' : 'Moreau',
	 'prenom' : 'Pierre',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48345744',
	 'nom' : 'Le Roux',
	 'prenom' : 'Maurice',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48321565',
	 'nom' : 'De Sousa',
	 'prenom' : 'Élodie',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48572655',
	 'nom' : 'Lefebvre',
	 'prenom' : 'Lucas',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48730075',
	 'nom' : 'Lefebvre',
	 'prenom' : 'Antoine',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49709406',
	 'nom' : 'Lelievre',
	 'prenom' : 'André',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48515365',
	 'nom' : 'Ledoux',
	 'prenom' : 'Nicole',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '49724031',
	 'nom' : 'Devaux',
	 'prenom' : 'Grégoire',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48387894',
	 'nom' : 'Ledoux',
	 'prenom' : 'Michèle',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48412995',
	 'nom' : 'Dijoux',
	 'prenom' : 'Maurice',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49686544',
	 'nom' : 'Leroux',
	 'prenom' : 'Marcel',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48591629',
	 'nom' : 'Devaux',
	 'prenom' : 'Alexandre',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48974458',
	 'nom' : 'Devaux',
	 'prenom' : 'Patrick',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49344016',
	 'nom' : 'Ledoux',
	 'prenom' : 'Claire',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48603124',
	 'nom' : 'Devaux',
	 'prenom' : 'Joseph',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49914007',
	 'nom' : 'Dijoux',
	 'prenom' : 'Daniel',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48193989',
	 'nom' : 'Leroux',
	 'prenom' : 'Édouard',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48922113',
	 'nom' : 'Ledoux',
	 'prenom' : 'Éric',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48789638',
	 'nom' : 'Launay',
	 'prenom' : 'Sophie',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48869946',
	 'nom' : 'Launay',
	 'prenom' : 'Victoire',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48278925',
	 'nom' : 'Boulay',
	 'prenom' : 'Noël',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48043742',
	 'nom' : 'Baudry',
	 'prenom' : 'Jeanne',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48447298',
	 'nom' : 'Fleury',
	 'prenom' : 'Anaïs',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49421253',
	 'nom' : 'Fleury',
	 'prenom' : 'Michel',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48519378',
	 'nom' : 'Launay',
	 'prenom' : 'Joséphine',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49287392',
	 'nom' : 'Launay',
	 'prenom' : 'Alexandre',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48731386',
	 'nom' : 'Lecoq',
	 'prenom' : 'Adèle',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48579750',
	 'nom' : 'Munoz',
	 'prenom' : 'Bernadette',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48098807',
	 'nom' : 'Klein',
	 'prenom' : 'Alphonse',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '48911021',
	 'nom' : 'Royer',
	 'prenom' : 'Marie',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '49548192',
	 'nom' : 'Fabre',
	 'prenom' : 'Camille',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48930006',
	 'nom' : 'Marty',
	 'prenom' : 'Françoise',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48422179',
	 'nom' : 'Robin',
	 'prenom' : 'Catherine',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48667895',
	 'nom' : 'Pages',
	 'prenom' : 'Aimée',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48001841',
	 'nom' : 'Costa',
	 'prenom' : 'Marcel',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '48193967',
	 'nom' : 'Vidal',
	 'prenom' : 'Xavier',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49077302',
	 'nom' : 'Hamel',
	 'prenom' : 'Gabrielle',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48119607',
	 'nom' : 'Masse',
	 'prenom' : 'Sylvie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49693529',
	 'nom' : 'Boyer',
	 'prenom' : 'Chantal',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48551845',
	 'nom' : 'Lebon',
	 'prenom' : 'Pierre',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48463317',
	 'nom' : 'Rossi',
	 'prenom' : 'Émile',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48794125',
	 'nom' : 'Neveu',
	 'prenom' : 'Maryse',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '48514075',
	 'nom' : 'Colas',
	 'prenom' : 'Amélie',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49741989',
	 'nom' : 'Perez',
	 'prenom' : 'Bernard',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '49534414',
	 'nom' : 'Colin',
	 'prenom' : 'Alexandrie',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48570674',
	 'nom' : 'Simon',
	 'prenom' : 'Émile',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49133649',
	 'nom' : 'Peron',
	 'prenom' : 'Juliette',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49798883',
	 'nom' : 'Morin',
	 'prenom' : 'Margaret',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49632406',
	 'nom' : 'Andre',
	 'prenom' : 'Laurence',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '49314597',
	 'nom' : 'Jacob',
	 'prenom' : 'Geneviève',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48391691',
	 'nom' : 'Caron',
	 'prenom' : 'Vincent',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48480551',
	 'nom' : 'Carre',
	 'prenom' : 'Édith',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '48381460',
	 'nom' : 'Guyon',
	 'prenom' : 'Guy',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49362578',
	 'nom' : 'Leger',
	 'prenom' : 'Aimée',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49221532',
	 'nom' : 'Rossi',
	 'prenom' : 'Jean',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '48147518',
	 'nom' : 'Denis',
	 'prenom' : 'Joséphine',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49202084',
	 'nom' : 'Begue',
	 'prenom' : 'Augustin',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49499759',
	 'nom' : 'Perez',
	 'prenom' : 'Christophe',
	 'formation' : 'SESI',
	 'groupe' : '15'
	},

	{'nip' : '49299384',
	 'nom' : 'Caron',
	 'prenom' : 'Matthieu',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48906555',
	 'nom' : 'Paris',
	 'prenom' : 'Marcelle',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48750331',
	 'nom' : 'Weiss',
	 'prenom' : 'Nathalie',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49339640',
	 'nom' : 'Hamon',
	 'prenom' : 'André',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48500400',
	 'nom' : 'Leger',
	 'prenom' : 'Christiane',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49752069',
	 'nom' : 'Leduc',
	 'prenom' : 'Marine',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48354905',
	 'nom' : 'Vidal',
	 'prenom' : 'Chantal',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '49267978',
	 'nom' : 'Barre',
	 'prenom' : 'Émilie',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48874578',
	 'nom' : 'Pinto',
	 'prenom' : 'Auguste',
	 'formation' : 'SESI',
	 'groupe' : '16'
	},

	{'nip' : '48736054',
	 'nom' : 'Munoz',
	 'prenom' : 'Michelle',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48674421',
	 'nom' : 'Dupre',
	 'prenom' : 'Timothée',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '49094170',
	 'nom' : 'Laine',
	 'prenom' : 'Margot',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48880022',
	 'nom' : 'Munoz',
	 'prenom' : 'Monique',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48141525',
	 'nom' : 'Boyer',
	 'prenom' : 'Catherine',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48185974',
	 'nom' : 'Bazin',
	 'prenom' : 'Isabelle',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '48486142',
	 'nom' : 'Gomez',
	 'prenom' : 'Marguerite',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48593597',
	 'nom' : 'Coste',
	 'prenom' : 'Zoé',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '48383428',
	 'nom' : 'Colas',
	 'prenom' : 'Claire',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49961912',
	 'nom' : 'Roger',
	 'prenom' : 'Valentine',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49245257',
	 'nom' : 'Dumas',
	 'prenom' : 'Marcel',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49224114',
	 'nom' : 'Morin',
	 'prenom' : 'Grégoire',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49248703',
	 'nom' : 'Hamon',
	 'prenom' : 'Dorothée',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '48412538',
	 'nom' : 'Simon',
	 'prenom' : 'Luce',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49161394',
	 'nom' : 'Paris',
	 'prenom' : 'Michel',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49839725',
	 'nom' : 'Weber',
	 'prenom' : 'Nicole',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49528818',
	 'nom' : 'Boyer',
	 'prenom' : 'Rémy',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '49425341',
	 'nom' : 'Peron',
	 'prenom' : 'Chantal',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48222588',
	 'nom' : 'Leroy',
	 'prenom' : 'Bertrand',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49375425',
	 'nom' : 'Louis',
	 'prenom' : 'Aurore',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49691116',
	 'nom' : 'Morin',
	 'prenom' : 'Juliette',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48092986',
	 'nom' : 'Jacob',
	 'prenom' : 'Guy',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49770298',
	 'nom' : 'Louis',
	 'prenom' : 'Jacques',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48091846',
	 'nom' : 'Maury',
	 'prenom' : 'Pauline',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '48747166',
	 'nom' : 'Meyer',
	 'prenom' : 'Joseph',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48893548',
	 'nom' : 'Guyot',
	 'prenom' : 'Maggie',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49951851',
	 'nom' : 'Pages',
	 'prenom' : 'Joséphine',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49697881',
	 'nom' : 'Vidal',
	 'prenom' : 'Charles',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48401606',
	 'nom' : 'Baron',
	 'prenom' : 'Franck',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '49501574',
	 'nom' : 'Neveu',
	 'prenom' : 'Emmanuel',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48572106',
	 'nom' : 'Paris',
	 'prenom' : 'Michelle',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48587035',
	 'nom' : 'Colin',
	 'prenom' : 'Michèle',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

	{'nip' : '48749272',
	 'nom' : 'Lecoq',
	 'prenom' : 'Andrée',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48804667',
	 'nom' : 'Weiss',
	 'prenom' : 'Hortense',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48005323',
	 'nom' : 'Carre',
	 'prenom' : 'Lucas',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48638198',
	 'nom' : 'Lopez',
	 'prenom' : 'Patrick',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48691071',
	 'nom' : 'Leleu',
	 'prenom' : 'Célina',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '48717291',
	 'nom' : 'Morin',
	 'prenom' : 'Susan',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '49381624',
	 'nom' : 'Dupuy',
	 'prenom' : 'Benjamin',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49604425',
	 'nom' : 'Meyer',
	 'prenom' : 'Louis',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49925271',
	 'nom' : 'Guyot',
	 'prenom' : 'William',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49532163',
	 'nom' : 'Dupre',
	 'prenom' : 'Frédéric',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48670779',
	 'nom' : 'Guyon',
	 'prenom' : 'Agnès',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '48664543',
	 'nom' : 'Andre',
	 'prenom' : 'Inès',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '49934792',
	 'nom' : 'Maury',
	 'prenom' : 'Patrick',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49242600',
	 'nom' : 'Payet',
	 'prenom' : 'Andrée',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49294945',
	 'nom' : 'Laine',
	 'prenom' : 'Colette',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '48661748',
	 'nom' : 'Coste',
	 'prenom' : 'Philippine',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '49392150',
	 'nom' : 'Herve',
	 'prenom' : 'Bernadette',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49640831',
	 'nom' : 'Alves',
	 'prenom' : 'Claude',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49296572',
	 'nom' : 'Blanc',
	 'prenom' : 'Élodie',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '49466819',
	 'nom' : 'Lucas',
	 'prenom' : 'Aimé',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48959558',
	 'nom' : 'Barbe',
	 'prenom' : 'Yves',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49178267',
	 'nom' : 'Bodin',
	 'prenom' : 'Matthieu',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '48276414',
	 'nom' : 'Rossi',
	 'prenom' : 'Alice',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '49690801',
	 'nom' : 'Baron',
	 'prenom' : 'Richard',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49394642',
	 'nom' : 'Baron',
	 'prenom' : 'Alain',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48000402',
	 'nom' : 'Henry',
	 'prenom' : 'Louise',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48538691',
	 'nom' : 'Gomes',
	 'prenom' : 'William',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49293936',
	 'nom' : 'Dumas',
	 'prenom' : 'Gilles',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48475196',
	 'nom' : 'Gomes',
	 'prenom' : 'Luc',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48445351',
	 'nom' : 'Bazin',
	 'prenom' : 'daisy',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '48355750',
	 'nom' : 'Petit',
	 'prenom' : 'Julien',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '49819592',
	 'nom' : 'Gomez',
	 'prenom' : 'Martin',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48613351',
	 'nom' : 'Royer',
	 'prenom' : 'David',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49120677',
	 'nom' : 'Neveu',
	 'prenom' : 'Frédéric',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49636092',
	 'nom' : 'Leleu',
	 'prenom' : 'Frédéric',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49660120',
	 'nom' : 'Herve',
	 'prenom' : 'Auguste',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '48089183',
	 'nom' : 'Roger',
	 'prenom' : 'Raymond',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49359481',
	 'nom' : 'Gomez',
	 'prenom' : 'Victoire',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '49338686',
	 'nom' : 'Leger',
	 'prenom' : 'Jean',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '48972215',
	 'nom' : 'Gros',
	 'prenom' : 'Élisabeth',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '49289834',
	 'nom' : 'Mary',
	 'prenom' : 'Édith',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '49418166',
	 'nom' : 'Roux',
	 'prenom' : 'Élise',
	 'formation' : 'SESI',
	 'groupe' : '45'
	},

]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
