--创建数据库
create database SpiderDouban;

--使用数据库
use SpiderDouban;

--创建表
create table if not exists `data`(
					id int not null primary key auto_increment,
					title varchar(255) not null,
					content text not null
)engine=innodb, default charset=utf8;

--测试
insert into `data`(`title`, `content`) values ("test", "test_content");

select * from `data`
