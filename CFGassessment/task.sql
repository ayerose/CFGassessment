---1.

CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

CREATE TABLE movie_info (
  Movie_ID INT NOT NULL AUTO_INCREMENT,
  Movie_Name VARCHAR(255) NOT NULL,
  Movie_Length TIME NOT NULL,
  Age_Rating VARCHAR(10) NOT NULL,
  PRIMARY KEY (Movie_ID)
);

CREATE TABLE screens (
  Screen_ID INT NOT NULL AUTO_INCREMENT,
  Four_K BOOLEAN NOT NULL,
  PRIMARY KEY (Screen_ID)
);

CREATE TABLE showings (
  Showing_ID INT NOT NULL AUTO_INCREMENT,
  Movie_ID INT NOT NULL,
  Screen_ID INT NOT NULL,
  Start_Time TIME NOT NULL,
  Available_Seats INT NOT NULL,
  PRIMARY KEY (Showing_ID),
  FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
  FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

// Write a query to return the name and time of all movies that play after
           12:00 given there is at least 1 available seat. Display the results in time
           order.

--- 2. Write a query to return the name and time of all movies that play after
 --      12:00 given there is at least 1 available seat. Display the results in time order.
SELECT movie_name, start_time
FROM movie_info
JOIN showings ON movie_info.movie_id = showings.movie_id
WHERE start_time > '12:00:00' AND available_seats > 0
ORDER BY start_time;

-- 3.  Return the name of the movie with the most showings.
SELECT movie_name
FROM showings
JOIN movie_info ON showings.movie_ID = movie_info.movie_ID
GROUP BY movie_name
ORDER BY COUNT(*) DESC
LIMIT 1;
