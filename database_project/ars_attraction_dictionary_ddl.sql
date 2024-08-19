create table ars_attraction_dictionary
(
    pk_attraction_dictionary_id int auto_increment primary key,
    attraction_name, attraction_title NVARCHAR(64) not null,
    attraction_title NVARCHAR(64) not null,
    is_in_use int not null DEFAULT '1',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (1, 'restaurace', 'Restaurace', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (2, 'kavarna', 'Kavarna', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (3, 'lanovy_park', 'Lanovy Park', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (4, 'minigolf', 'Minigolf', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (5, 'trampoliny', 'Trampoliny', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (6, 'pujcovna', 'Pujcovna', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (7, 'koktejl_bar', 'Koktejl Bar', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (8, 'spunt_vstup', 'Spuntarko Vstup', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, attraction_title, is_in_use) VALUES (9, 'spunt_obcerstveni', 'Spunt Obcerstveni', 1);