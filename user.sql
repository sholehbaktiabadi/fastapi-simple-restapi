-- user mysql query migrations

create table user(
	id bigint(20) unsigned primary key auto_increment,
    name varchar(60) not null,
    age integer null
);