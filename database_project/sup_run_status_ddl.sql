create table sup_run_status
(
    pk_run_status_id int auto_increment primary key,
    action_datetime datetime not null,
    calculation_id NVARCHAR(128) not null,
    run_status int not null DEFAULT 4,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- Run status
-- 0 Failed
-- 1 Running
-- 2 Finished
-- 4 Status invalid
