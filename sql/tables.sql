create database hospital;
use hospital;

create table users(
	uid varchar(20) primary key,
    username varchar(200),
    hashPassword varchar(256),
    utype varchar(20)
)