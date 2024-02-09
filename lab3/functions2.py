# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#ex1
from diction import movies
movies = movies
for i in movies:
    if i["imdb"] >= 5.5:
        print(True)
    else:
        print(False)

#ex2
from diction import movies
movie = movies
def sub(movie):
    s = []
    for i in movie:
        if i["imdb"] >= 5.5:
            s.append(i)
    return s
print(sub(movie))

#ex3
from diction import movies
movies = movies
def iscat(movies,ct):
    d = []
    for i in movies:
        if i["category"] == ct:
            d.append(i)
    return d
print(iscat(movies,input()))

#ex4
from diction import movies
movies = movies
def avr(movies):
    av = 0
    for i in movies:
        av+=i['imdb']
    return av/len(movies)
print(avr(movies))

#ex5
from diction import movies
movies = movies()
def av(movies,n):
    curr = 0
    total = 0
    for i in movies:
        if (i["category"] == n):
            total += 1
            curr += i["imdb"]
    return curr / total
n = str(input())
print(av(movies,n))