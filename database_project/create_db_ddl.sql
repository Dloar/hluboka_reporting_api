create table ars_day_temperature
(
    pk_day_temperature_id int auto_increment primary key,
    action_date date not null,
    temperature int not null,
    humidity int not null,
    wind_speed  int null,
    rain_intensity int  null,
    rain_accumulation int   null,
    time_of_sun float   null,
    day_of_week int null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table ars_attraction_dictionary
(
    pk_attraction_dictionary_id int auto_increment primary key,
    attraction_name NVARCHAR(64) not null,
    is_in_use int not null DEFAULT '1',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table ars_daily_income_detail
(
    pk_daily_income_detail_id int auto_increment primary key,
    fk_attraction_dictionary_id int not null,
    fk_day_temperature_id int not null,
    attraction_income int not null,
    action_date date null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_day_temperature_id_d FOREIGN KEY (fk_day_temperature_id) REFERENCES ars_attraction_dictionary(pk_attraction_dictionary_id),
    CONSTRAINT fk_attraction_dictionary_id FOREIGN KEY (fk_attraction_dictionary_id) REFERENCES ars_day_temperature(pk_day_temperature_id)
);

create table ars_daily_income_total
(
    pk_daily_income_total_id int auto_increment primary key,
    fk_day_temperature_id int not null,
    total_income int not null,
    action_date date null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_day_temperature_id_t FOREIGN KEY (fk_day_temperature_id) REFERENCES ars_attraction_dictionary(pk_attraction_dictionary_id)
);

create table sup_run_status
(
    pk_run_status_id int auto_increment primary key,
    action_datetime datetime not null,
    calculation_id NVARCHAR(128) not null,
    run_status int not null DEFAULT 4,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table sup_temperature_raw
(
    pk_temperature_raw_id int auto_increment primary key,
    action_datetime datetime not null,
    temperature int not null,
    humidity int null,
    wind_speed  int null,
    rain_intensity int  null,
    rain_accumulation int   null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table ssy_users
(
    pk_users_id int auto_increment primary key,
    user_name NVARCHAR(255) not null,
    user_pass NVARCHAR(255) not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);