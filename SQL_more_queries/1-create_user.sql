-- a script that creates the MySQL server user user_0d_1.
CREATE USER if EXISTS user_0d_1
IDENTIFIED BY 'Secure1Pass!';
SHOW GRANTS FOR user_0d_1
GRANT ALL
ON user_0d_1_pwd.*
TO user_0d_1;
SHOW GRANTS FOR user_0d_1;
