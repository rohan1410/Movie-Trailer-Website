import media
import fresh_tomatoes

dhoom = media.Movie("Dhoom 3","Bikes doing mad shit","https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Dhoom_3_Film_Poster.jpg/220px-Dhoom_3_Film_Poster.jpg","https://www.youtube.com/watch?v=yeF_b8EQcK0")
#print (dhoom.storyline)
boss = media.Movie("Boss","Aunty police bula legi","https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Boss_%282013_Hindi_film%29_Theatrical_Poster.jpg/220px-Boss_%282013_Hindi_film%29_Theatrical_Poster.jpg","https://www.youtube.com/watch?v=zaoDtl0GL2E")
#print (boss.storyline)
#boss.show_trailer();
movies = [dhoom,boss]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
print (media.Movie.__dict__)
print (media.Movie.__bases__)
