create table ars_daily_income_detail
(
    pk_daily_income_detail_id int auto_increment primary key,
    fk_attraction_dictionary_id int not null,
    fk_day_temperature_id int not null,
    attraction_income int not null,
    action_date date null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_day_temperature_id_d FOREIGN KEY (fk_day_temperature_id) REFERENCES pk_attraction_dictionary_id(pk_attraction_dictionary_id),
    CONSTRAINT fk_attraction_dictionary_id FOREIGN KEY (fk_attraction_dictionary_id) REFERENCES ars_day_temperature(pk_day_temperature_id)
);