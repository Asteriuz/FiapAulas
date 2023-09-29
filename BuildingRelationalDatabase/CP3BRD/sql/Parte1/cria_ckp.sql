-- Integrantes | RM
-- Augusto Barcelos Barros | 98078
-- Gabriel Souza de Queiroz | 98570

-- create table T_CKP_CATEGORIA
-- not null cd_categoria NUmber(3) primary key
-- not null ds_sigla_categoria CHAR (3 CHAR) unique
-- not null ds_categoria Varchar2(30) unique
-- PK_CKP_CATEGORIA primary key (cd_categoria)
-- UN_CKP_CATEGORIA_SIGLA unique (ds_sigla_categoria)
-- UN_CKP_CATEGORIA_DESC unique (ds_categoria)

CREATE TABLE T_CKP_CATEGORIA (
    CD_CATEGORIA NUMBER(3) NOT NULL,
    DS_SIGLA_CATEGORIA CHAR(3 CHAR) NOT NULL,
    DS_CATEGORIA VARCHAR2(30) NOT NULL
);

ALTER TABLE T_CKP_CATEGORIA ADD CONSTRAINT PK_CKP_CATEGORIA PRIMARY KEY (CD_CATEGORIA);

ALTER TABLE T_CKP_CATEGORIA ADD CONSTRAINT UN_CKP_CATEGORIA_SIGLA UNIQUE (DS_SIGLA_CATEGORIA);

ALTER TABLE T_CKP_CATEGORIA ADD CONSTRAINT UN_CKP_CATEGORIA_DESC UNIQUE (DS_CATEGORIA);

-- create table T_CKP_LIVRO
-- not null nr_isbn NUMBER(8) primary key
-- not null cd_categoria NUMBER(3)
-- not null nm_titulo VARCHAR2(50)
-- not null ds_sinopse VARCHAR2(200)
-- not null nr_edicao NUMBER(2)
-- not null nr_ano NUMBER(4)
-- not null cd_categoria1 NUMBER(3)
-- PK_CKP_LIVRO primary key (nr_isbn)
-- FK_CKP_LIVRO_CATEGORIA foreign key (cd_categoria) references T_CKP_CATEGORIA (cd_categoria)

CREATE TABLE T_CKP_LIVRO (
    NR_ISBN NUMBER(8) NOT NULL,
    CD_CATEGORIA NUMBER(3) NOT NULL,
    NM_TITULO VARCHAR2(50) NOT NULL,
    DS_SINOPSE VARCHAR2(200) NOT NULL,
    NR_EDICAO NUMBER(2) NOT NULL,
    NR_ANO NUMBER(4) NOT NULL,
    CD_CATEGORIA1 NUMBER(3) NOT NULL
);

ALTER TABLE T_CKP_LIVRO ADD CONSTRAINT PK_CKP_LIVRO PRIMARY KEY (NR_ISBN);

ALTER TABLE T_CKP_LIVRO ADD CONSTRAINT CK_CKP_LIVRO_EDICAO CHECK (NR_EDICAO > 0);

ALTER TABLE T_CKP_LIVRO ADD CONSTRAINT CK_CKP_LIVRO_ANO CHECK (NR_ANO > 0);

-- create table T_CKP_AUTOR
-- not null cd_autor NUMBER(3) primary key
-- not null nm_primeiro_autor VARCHAR2(20)
-- not null nm_segundo_autor VARCHAR2(40)
-- PK_CKP_AUTOR primary key (cd_autor)

CREATE TABLE T_CKP_AUTOR (
    CD_AUTOR NUMBER(3) NOT NULL,
    NM_PRIMEIRO_AUTOR VARCHAR2(20) NOT NULL,
    NM_SEGUNDO_AUTOR VARCHAR2(40) NOT NULL
);

ALTER TABLE T_CKP_AUTOR ADD CONSTRAINT PK_CKP_AUTOR PRIMARY KEY (CD_AUTOR);

-- create table T_CKP_AUTOR_LIVRO
-- not null nr_isbn NUMBER(8) primary foreign key references T_CKP_LIVRO (nr_isbn)
-- not null cd_autor NUMBER(3) primary foreign key references T_CKP_AUTOR (cd_autor)
-- st_autor_principal CHAR(1)
-- PK_CKP_AUTOR_LIVRO primary key (nr_isbn, cd_autor)
-- FK_CKP_AUTOR_LIVRO_LIVRO foreign key (nr_isbn) references T_CKP_LIVRO (nr_isbn)
-- FK_CKP_AUTOR_LIVRO_AUTOR foreign key (cd_autor) references T_CKP_AUTOR (cd_autor)

CREATE TABLE T_CKP_AUTOR_LIVRO (
    NR_ISBN NUMBER(8) NOT NULL,
    CD_AUTOR NUMBER(3) NOT NULL,
    ST_AUTOR_PRINCIPAL CHAR(1) NOT NULL
);

ALTER TABLE T_CKP_AUTOR_LIVRO ADD CONSTRAINT PK_CKP_AUTOR_LIVRO PRIMARY KEY (NR_ISBN, CD_AUTOR);

ALTER TABLE T_CKP_AUTOR_LIVRO ADD CONSTRAINT CK_CKP_AUTOR_LIVRO_ST_AUTOR_PRINCIPAL CHECK (ST_AUTOR_PRINCIPAL IN ('1', '2'));

ALTER TABLE T_CKP_LIVRO ADD CONSTRAINT FK_CKP_LIVRO_CATEGORIA FOREIGN KEY (CD_CATEGORIA) REFERENCES T_CKP_CATEGORIA (CD_CATEGORIA);

ALTER TABLE T_CKP_AUTOR_LIVRO ADD CONSTRAINT FK_CKP_AUTOR_LIVRO_LIVRO FOREIGN KEY (NR_ISBN) REFERENCES T_CKP_LIVRO (NR_ISBN);

ALTER TABLE T_CKP_AUTOR_LIVRO ADD CONSTRAINT FK_CKP_AUTOR_LIVRO_AUTOR FOREIGN KEY (CD_AUTOR) REFERENCES T_CKP_AUTOR (CD_AUTOR);