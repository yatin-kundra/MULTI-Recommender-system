import streamlit as st
import pandas as pd
import numpy as np


page = st.sidebar.selectbox("Select a Recommender", ["Home", "Movies", "Series", "Anime", "Books"])

########  MOVIES


def Movies_recommend(movie):
    movies["title_L"] = movies["title"].apply(lambda x: x.lower())  # making a col. with all the lower case titles
    movie_index = movies[movies["title_L"] == movie.lower()].index[0]  # finding the index
    movies.drop("title_L", axis=1, inplace=True)  # removing that temprary lowecase list
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    movies_recommended = []
    for i in movie_list:
        movies_recommended.append(movies.iloc[i[0]].title)
        # print(movies.iloc[i[0]].title)
    return movies_recommended


movies = pd.read_pickle("Movie model/movies_dict1.pkl")
similarity = pd.read_pickle("Movie model/similarity1.pkl")
movies = pd.DataFrame(movies)



####### series


def Series_recommend(movie):
    imdb_final["title_L"] = imdb_final["Title"].apply(
        lambda x: x.lower())  # making a col. with all the lower case titles
    s_index = imdb_final[imdb_final["title_L"] == movie.lower()].index[0]  # finding the index
    imdb_final.drop("title_L", axis=1, inplace=True)  # removing that temprary lowecase list
    distances = series_similarity[s_index]
    series_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    series_recommended = []
    for i in series_list:
        # print(imdb_final.iloc[i[0]].Title)
        series_recommended.append(imdb_final.iloc[i[0]].Title)
    return series_recommended


imdb_final = pd.read_pickle("series model/imdb_final.pkl")
series_similarity = pd.read_pickle("series model/similarity.pkl")
imdb_final = pd.DataFrame(imdb_final)

####### Anime


def anime_recommend(anime):
    indx = np.where(pt.index == anime)[0][0]  ## this will give the index of the book in the pt df
    distance = similarity_score[indx]  ## this is the vector of the book that user have input
    suggestion = sorted(enumerate(distance), key = lambda x:x[1], reverse = True)[1:6]  ## this will tell the distance and index too
    sugg = []
    for i in suggestion:
        sugg.append(pt.index[i[0]])    # this give the index
        # print(pt.index[i[0]])
        # return pt.index[i[0]]
    return sugg

pt = pd.read_pickle("anime model/pt_for_recomm.pkl")
similarity_score = pd.read_pickle("anime model/scores_anime.pkl")
pt = pd.DataFrame(pt)


#### books

### making a function called recommend we will give name of a book and it will give us recommended books in return
def book_recommend(book):
    indx = np.where(pt_B.index == book)[0][0]  ## this will give the index of the book in the pt df
    distance = Bsimilarity_score[indx]  ## this is the vector of the book that user have input
    suggestion = sorted(enumerate(distance), key=lambda x: x[1], reverse=True)[
                 1:6]  ## this will tell the distance and index too
    books_sugg = []
    for i in suggestion:
        # print(i[0])    # this give the index
        books_sugg.append(pt_B.index[i[0]])
    return books_sugg

pt_B = pd.read_pickle("book model/pt_for_recomm.pkl")
Bsimilarity_score = pd.read_pickle("book model/scores.pkl")
pt = pd.DataFrame(pt)



if page == "Home":
    st.markdown("<h1 style='text-align:center'> RECOMMEDER SYSTEM </h1>", unsafe_allow_html=True)

    st.title("")
    st.markdown("<h3 style='text-align:center'>Movies | TV Series | Anime | Books </h3>", unsafe_allow_html=True)




elif page == "Movies":

    st.title("MOVIE RECOMMENDATION SYSTEM")

    selected_movie = st.selectbox(
        "select a movie",
        movies["title"].values

    )

    if st.button("Recommend"):
        recommendations = Movies_recommend(selected_movie)

        for i in recommendations:
            st.write(i)

##### series #####

elif page == "Series":
    st.title("SERIES RECOMMENDATION SYSTEM")

    selected_series = st.selectbox(
        "select a series",
        imdb_final["Title"].values

    )

    if st.button("Recommend"):
        recommendations = Series_recommend(selected_series)

        for i in recommendations:
            st.write(i)

##### anime

elif page == "Anime":
    st.title("ANIME RECOMMENDATION SYSTEM")

    selected_anime = st.selectbox(
        "select an anime",
        pt.index.values

    )

    if st.button("Recommend"):
        recommendations = anime_recommend(selected_anime)

        for i in recommendations:
            st.write(i)

elif page == "Books":
    st.title("BOOKS RECOMMENDATION SYSTEM")

    selected_book = st.selectbox(
        "select an book",
        pt_B.index.values

    )

    if st.button("Recommend"):
        recommendations = book_recommend(selected_book)

        for i in recommendations:
            st.write(i)
