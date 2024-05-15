#assignment 6
use assignment4;
select user();
#Creating User
create user 'arshad1'@'localhost' identified by 'arshad';
#Using GRANT
grant select,update,insert on assignment4.* to 'arshad1'@'localhost';
#Using Revoke
revoke select,insert on assignment4.* from 'arshad1'@'localhost';
show grants for 'arshad'@'localhost';

