create table ars_attraction_dictionary
(
    pk_attraction_dictionary_id int auto_increment primary key,
    attraction_name NVARCHAR(64) not null,
    is_in_use int not null DEFAULT '1',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (1, 'restaurace', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dicti`onary_id, attraction_name, is_in_use) VALUES (2, 'kavarna', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (3, 'lanovy_park', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (4, 'minigolf', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (5, 'trampoliny', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (6, 'pujcovna', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (7, 'koktejl_bar', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (8, 'spunt_vstup', 1);
INSERT INTO areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id, attraction_name, is_in_use) VALUES (9, 'spunt_obcerstveni', 1);