create database hospital;
use hospital;

create table users(
	uid varchar(20) primary key,
    username varchar(200) unique,
    hashPassword varchar(256),
    utype varchar(20)
);

create table departments(
	deptID varchar(20) primary key,
    deptName varchar(100),
    location varchar(100),
    phone varchar(50)
);

create table doctors(
	uid varchar(20) primary key references users(uid),
    name varchar(200),
    deptID varchar(20) references departments(deptID)
);

create table patients(
	uid varchar(20) primary key references users(uid),
    name varchar(200),
    balance numeric(10, 2),
    email varchar(200),
    phone varchar(50)
);