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