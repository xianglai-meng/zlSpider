create table t_zljob( job_id int unsigned auto_increment,
 company varchar(50), job_name varchar(50), c_type varchar(50),
  city varchar(50), update_str varchar(50), salary varchar(50), 
  edu_level varchar(50), job_type varchar(50), working_exp varchar(50),
   empl_type varchar(50), position_url varchar(100), welfare varchar(50),
    business_area varchar(100), primary key(job_id) )engine=innodb default charset=utf8;
