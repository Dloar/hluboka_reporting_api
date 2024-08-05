create table ars_daily_income_total
(
    pk_daily_income_total_id int auto_increment primary key,
    fk_day_temperature_id int not null,
    total_income int not null,
    action_date date null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_day_temperature_id_t FOREIGN KEY (fk_day_temperature_id) REFERENCES pk_attraction_dictionary_id(pk_attraction_dictionary_id)
);