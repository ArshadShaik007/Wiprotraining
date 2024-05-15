#assignment 5
use assignment4;
create index dates on issues (returndate);
alter table issues drop index dates;
