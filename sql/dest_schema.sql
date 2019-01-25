create table if not exists destination(
    id int(5) not null auto_increment,
    source_id int(5) not null,
    source_name varchar(20) not null,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    email varchar(50) not null,
    gender varchar(10) not null,
    ville varchar(50),
    primary key (id)
)