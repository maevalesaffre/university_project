--
-- PostgreSQL database dump
--

-- Dumped from database version 11.9
-- Dumped by pg_dump version 11.9

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: livres; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA if not exists livres;


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auteurs; Type: TABLE; Schema: livres; Owner: -
--

CREATE TABLE livres.auteurs (
    id integer NOT NULL,
    nom text NOT NULL
);


--
-- Name: auteurs_id_seq; Type: SEQUENCE; Schema: livres; Owner: -
--

CREATE SEQUENCE livres.auteurs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auteurs_id_seq; Type: SEQUENCE OWNED BY; Schema: livres; Owner: -
--

ALTER SEQUENCE livres.auteurs_id_seq OWNED BY livres.auteurs.id;


--
-- Name: categories; Type: TABLE; Schema: livres; Owner: -
--

CREATE TABLE livres.categories (
    nom text NOT NULL
);


--
-- Name: TABLE categories; Type: COMMENT; Schema: livres; Owner: -
--

COMMENT ON TABLE livres.categories IS 'répertoire des catégories';


--
-- Name: ecriture; Type: TABLE; Schema: livres; Owner: -
--

CREATE TABLE livres.ecriture (
    livre integer NOT NULL,
    auteur integer NOT NULL
);


--
-- Name: TABLE ecriture; Type: COMMENT; Schema: livres; Owner: -
--

COMMENT ON TABLE livres.ecriture IS 'relation auteur<->livre : "a écrit"';


--
-- Name: livres; Type: TABLE; Schema: livres; Owner: -
--

CREATE TABLE livres.livres (
    annee smallint NOT NULL,
    categorie text NOT NULL,
    id integer NOT NULL,
    serie text,
    titre text NOT NULL,
    couverture text NOT NULL
);


--
-- Name: livres_auteurs; Type: VIEW; Schema: livres; Owner: -
--

CREATE VIEW livres.livres_auteurs AS
 SELECT ecriture.livre,
    string_agg(auteurs.nom, ' - '::text) AS auteurs
   FROM (livres.auteurs
     JOIN livres.ecriture ON ((auteurs.id = ecriture.auteur)))
  GROUP BY ecriture.livre;


--
-- Name: livres_complets; Type: VIEW; Schema: livres; Owner: -
--

CREATE VIEW livres.livres_complets AS
 SELECT livres.annee,
    livres.categorie,
    livres.id,
    livres.serie,
    livres.titre,
    livres.couverture,
    livres_auteurs.auteurs
   FROM (livres.livres
     LEFT JOIN livres.livres_auteurs ON ((livres.id = livres_auteurs.livre)));


--
-- Name: livres_id_seq; Type: SEQUENCE; Schema: livres; Owner: -
--

CREATE SEQUENCE livres.livres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: livres_id_seq; Type: SEQUENCE OWNED BY; Schema: livres; Owner: -
--

ALTER SEQUENCE livres.livres_id_seq OWNED BY livres.livres.id;


--
-- Name: auteurs id; Type: DEFAULT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.auteurs ALTER COLUMN id SET DEFAULT nextval('livres.auteurs_id_seq'::regclass);


--
-- Name: livres id; Type: DEFAULT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.livres ALTER COLUMN id SET DEFAULT nextval('livres.livres_id_seq'::regclass);


--
-- Data for Name: auteurs; Type: TABLE DATA; Schema: livres; Owner: -
--

COPY livres.auteurs (id, nom) FROM stdin;
19	Frank Herbert
20	John Layman
21	Rob Guillory
22	JRR Tolkien
23	Brandon Sanderson
24	Marini
25	Desberg
26	Lois McMaster Bujold
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: livres; Owner: -
--

COPY livres.categories (nom) FROM stdin;
fantasy
science-fiction
bandes-dessinées
\.


--
-- Data for Name: ecriture; Type: TABLE DATA; Schema: livres; Owner: -
--

COPY livres.ecriture (livre, auteur) FROM stdin;
31	19
32	20
32	21
33	22
34	23
35	24
35	25
36	26
\.


--
-- Data for Name: livres; Type: TABLE DATA; Schema: livres; Owner: -
--

COPY livres.livres (annee, categorie, id, serie, titre, couverture) FROM stdin;
1965	science-fiction	31	\N	Dune	dune.jpg
2010	bandes-dessinées	32	Tony Chu - Détective Cannibale	Goût décès	tony-chu.jpg
1954	fantasy	33	\N	Le seigneur des anneaux	seigneur-des-anneaux.png
2006	fantasy	34	Fils des brumes	L'empire ultime	fils-des-brumes.jpg
2000	bandes-dessinées	35	Le Scorpion	La marque du diable	scorpion.jpg
1986	science-fiction	36	\N	Miles Vorkosigan	miles-vorkosigan.jpg
\.


--
-- Name: auteurs_id_seq; Type: SEQUENCE SET; Schema: livres; Owner: -
--

SELECT pg_catalog.setval('livres.auteurs_id_seq', 26, true);


--
-- Name: livres_id_seq; Type: SEQUENCE SET; Schema: livres; Owner: -
--

SELECT pg_catalog.setval('livres.livres_id_seq', 36, true);


--
-- Name: auteurs auteurs_nom_key; Type: CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.auteurs
    ADD CONSTRAINT auteurs_nom_key UNIQUE (nom);


--
-- Name: auteurs auteurs_pkey; Type: CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.auteurs
    ADD CONSTRAINT auteurs_pkey PRIMARY KEY (id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (nom);


--
-- Name: ecriture ecriture_pkey; Type: CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.ecriture
    ADD CONSTRAINT ecriture_pkey PRIMARY KEY (livre, auteur);


--
-- Name: livres livres_pkey; Type: CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.livres
    ADD CONSTRAINT livres_pkey PRIMARY KEY (id);


--
-- Name: ecriture ecriture_auteur_fkey; Type: FK CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.ecriture
    ADD CONSTRAINT ecriture_auteur_fkey FOREIGN KEY (auteur) REFERENCES livres.auteurs(id);


--
-- Name: ecriture ecriture_livre_fkey; Type: FK CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.ecriture
    ADD CONSTRAINT ecriture_livre_fkey FOREIGN KEY (livre) REFERENCES livres.livres(id);


--
-- Name: livres livres_categorie_fkey; Type: FK CONSTRAINT; Schema: livres; Owner: -
--

ALTER TABLE ONLY livres.livres
    ADD CONSTRAINT livres_categorie_fkey FOREIGN KEY (categorie) REFERENCES livres.categories(nom);


--
-- PostgreSQL database dump complete
--

