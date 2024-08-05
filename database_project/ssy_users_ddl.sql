create table ssy_users
(
    pk_users_id int auto_increment primary key,
    user_name NVARCHAR(255) not null,
    user_pass NVARCHAR(255) not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);