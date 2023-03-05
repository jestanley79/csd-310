/*
    Title: whatabook_init.sql
    Author: Jennifer Stanley
    Date: March 2023
    Description: Module 10.3
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('10 W Main St, Rising Sun, MD 21911');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Goblin Market', 'Christina Rossetti', 'The timeless tale of Laura and Lizzie');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F Scott Fitzgerald', 'The classic story of Jay Gatsby');

INSERT INTO book(book_name, author, details)
    VALUES('Jane Eyre', 'Charlotte Brontë', "Originally written under her pen name of Currer Bell");

INSERT INTO book(book_name, author)
    VALUES('Adventures of Huckleberry Finn', 'Mark Twain');

INSERT INTO book(book_name, author)
    VALUES('Pride and Prejudice', 'Jane Austen');

INSERT INTO book(book_name, author)
    VALUES("Little Women", 'Louisa May Alcott');

INSERT INTO book(book_name, author)
    VALUES('Moby Dick', 'Herman Melville');

INSERT INTO book(book_name, author)
    VALUES('Nineteen Eighty-Four', 'George Orwell');

INSERT INTO book(book_name, author)
    VALUES('Wuthering Heights', 'Emily Brontë');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Jason', 'Snedden');

INSERT INTO user(first_name, last_name)
    VALUES('Michael', 'Menser');

INSERT INTO user(first_name, last_name)
    VALUES('Kai', 'Stanley');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jason'), 
        (SELECT book_id FROM book WHERE book_name = 'The Great Gatsby')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Michael'),
        (SELECT book_id FROM book WHERE book_name = 'Moby Dick')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kai'),
        (SELECT book_id FROM book WHERE book_name = 'Little Women')
    );
