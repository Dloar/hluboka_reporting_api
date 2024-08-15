create table areal_hluboka.ars_attraction_dictionary
(
    pk_attraction_dictionary_id int auto_increment
        primary key,
    attraction_name             varchar(64) charset utf8mb3         not null,
    is_in_use                   int       default 1                 not null,
    created_at                  timestamp default CURRENT_TIMESTAMP null,
    modified_at                 timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
);

create table areal_hluboka.ars_day_temperature
(
    pk_day_temperature_id int auto_increment
        primary key,
    action_date           date                                not null,
    temperature           int                                 null,
    humidity              int                                 null,
    wind_speed            int                                 null,
    rain_intensity        int                                 null,
    rain_accumulation     int                                 null,
    time_of_sun           float                               null,
    day_of_week           int                                 null,
    created_at            timestamp default CURRENT_TIMESTAMP null,
    modified_at           timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
);

create table areal_hluboka.ars_daily_income_detail
(
    pk_daily_income_detail_id   int auto_increment
        primary key,
    fk_attraction_dictionary_id int                                 not null,
    fk_day_temperature_id       int                                 not null,
    attraction_income           int                                 not null,
    action_date                 date                                null,
    created_at                  timestamp default CURRENT_TIMESTAMP null,
    modified_at                 timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint fk_attraction_dictionary_id
        foreign key (fk_attraction_dictionary_id) references areal_hluboka.ars_attraction_dictionary (pk_attraction_dictionary_id),
    constraint fk_day_temperature_id_d
        foreign key (fk_day_temperature_id) references areal_hluboka.ars_day_temperature (pk_day_temperature_id)
);

create table areal_hluboka.ars_daily_income_total
(
    pk_daily_income_total_id int auto_increment
        primary key,
    fk_day_temperature_id    int                                 not null,
    total_income             int                                 not null,
    action_date              date                                null,
    created_at               timestamp default CURRENT_TIMESTAMP null,
    modified_at              timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint fk_day_temperature_id_t
        foreign key (fk_day_temperature_id) references areal_hluboka.ars_day_temperature (pk_day_temperature_id)
);

create table areal_hluboka.ssy_users
(
    pk_users_id int auto_increment
        primary key,
    user_name   varchar(255) charset utf8mb3        not null,
    user_pass   varchar(255) charset utf8mb3        not null,
    created_at  timestamp default CURRENT_TIMESTAMP null,
    modified_at timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
);

create table areal_hluboka.sup_run_status
(
    pk_run_status_id int auto_increment
        primary key,
    action_datetime  datetime                            not null,
    calculation_id   varchar(128) charset utf8mb3        not null,
    run_status       int       default 4                 not null,
    income_input     varchar(255) charset utf8mb3        not null,
    created_at       timestamp default CURRENT_TIMESTAMP null,
    modified_at      timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
);

create table areal_hluboka.sup_temperature_raw
(
    pk_temperature_raw_id int auto_increment
        primary key,
    action_datetime       datetime                            not null,
    temperature           int                                 not null,
    humidity              int                                 null,
    wind_speed            int                                 null,
    rain_intensity        int                                 null,
    rain_accumulation     int                                 null,
    created_at            timestamp default CURRENT_TIMESTAMP null
);

