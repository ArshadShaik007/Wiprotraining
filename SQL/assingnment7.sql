#assignment 7
use library;
insert into books values(1,'telugu','sunny','lang','2021','yes'),
(2,'hindi','arshad','lang','2011','no'),
(3,'math','rash','sub','2022','yes');
update books set title='biology' where book_id=3;
delete from books where title='telugu'