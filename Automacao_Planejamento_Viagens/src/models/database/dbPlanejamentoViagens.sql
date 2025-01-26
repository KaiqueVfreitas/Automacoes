CREATE TABLE IF NOT EXISTS `TB_VIAGEM` (
    id_viagem TEXT PRIMARY KEY,
    destino_viagem TEXT NOT NULL,
    data_inicio DATETIME,
    data_fim DATETIME,
    nome_organizador TEXT NOT NULL,
    email_organizador TEXT NOT NULL,
    status_viagem INTEGER
);

CREATE TABLE IF NOT EXISTS `TB_ENVIO_CONVITE` (
   id_envio_convite TEXT PRIMARY KEY,
   id_viagem TEXT,
   email_envio TEXT NOT NULL,
   FOREIGN KEY (id_viagem) REFERENCES TB_VIAGEM(id_viagem)
);

CREATE TABLE IF NOT EXISTS `TB_LINKS` (
    id_link TEXT PRIMARY KEY,
    id_viagem TEXT,
    link TEXT NOT NULL,
    FOREIGN KEY (id_viagem) REFERENCES TB_VIAGEM(id_viagem)
);
