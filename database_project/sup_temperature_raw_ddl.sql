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