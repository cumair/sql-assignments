drop table rank;
drop table books;
drop table publishers;
drop table authors;

create table AUTHORS (
    LastName        varchar2(40) not null,
    FirstName       varchar2(40),
    ID              number(5),
    BirthDate       varchar2(20),
  
    primary key (ID)
);

create table PUBLISHERS (
    name            varchar2(40),
    PID             number(5),
    address         varchar2(100),
    
    primary key (PID)
);

create table BOOKS (
    ISBN            varchar2(30),
    title           varchar2(100),
    publisherID     number(5),
        
    primary key (ISBN),
    foreign key (publisherID) references PUBLISHERS(PID)
);

create table RANK (
    AuthorID        number(5),
    ISBN            varchar2(30),
    rank_no         number(3),
    
    primary key (ISBN, rank_no),
    foreign key (ISBN) references BOOKS(ISBN),
    foreign key (AuthorID) references AUTHORS(ID)
);

create table ADVISORS (
    ID              number(10),
    name            varchar2(100),
    address         varchar2(300),
    research_area   varchar2(100),
    
    primary key (ID)
);

create table STUDENTS (
    SID             number(15),
    firstname       varchar2(50),
    lastname        varchar2(50) not null,
    dob             varchar2(20),
    telephone       varchar2(15),
    AdvisorID       number(10),
    
    primary key (SID),
    foreign key (AdvisorID) references ADVISORS(ID)
);

insert into AUTHORS
    values ( 'King', 'Stephen', 2, 'September 9 1947' );
insert into AUTHORS
    values ( 'Asimov', 'Isaac', 4, 'January 2 1920' );
insert into AUTHORS
    values ( 'Verne', 'Jules', 7, 'February 8 1828' );
insert into AUTHORS
    values ( 'Rowling', 'Joanne', 37, 'July 31 1965' );
insert into PUBLISHERS
    values ( 'Bloomsbury Publishing', 17, 'London Borough of Camden' );
insert into PUBLISHERS
    values ( 'Arthur A. Levine Books', 18, 'New York City' );
insert into BOOKS
    values ( '1111-111', 'Databases from outer space', 17 );
insert into BOOKS
    values ( '2222-222', 'Dark SQL', 17 );
insert into BOOKS
    values ( '3333-333', 'The night of the living databases', 18 );
insert into RANK
    values ( 2, '1111-111', 1 );
insert into RANK
    values ( 4, '1111-111', 2 );
insert into RANK
    values ( 4, '2222-222', 2 );
insert into RANK
    values ( 7, '2222-222', 1 );
insert into RANK
    values ( 37, '3333-333', 1 );
insert into RANK
    values ( 2, '3333-333', 2 );

create table Presidents (
name			varchar2(100),
birthyear              	number(4),
 	inaug_date		date not null,
    	political_party		varchar2(130),
 	
primary key (name, birthyear),
unique(inaug_date)
);







































