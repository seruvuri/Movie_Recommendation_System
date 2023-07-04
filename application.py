import streamlit as st
import dill,sys
from src.exception import CustomException
import requests
import base64

movies=dill.load(open('artifacts\movies_list.pkl','rb'))
similarity=dill.load(open('artifacts\similarity.pkl','rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")
select_value=st.selectbox("Select movie from dropdown",movies_list)

## adding background image for application
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2qgyPZtCm912SgXnxty14um8o7VIeB9FT1A&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# function for getting movies poster from tmdb website
def fetch_poster(movie_id):
     try:
          url="https://api.themoviedb.org/3/movie/{}?api_key=b6fa04ceaa7baa6b3b6acc07be0a2aa9".format(movie_id)
          data=requests.get(url)
          #converting data from api to json
          data=data.json()
          #accesing poster path from data
          poster_path=data['poster_path']
          #getting full path for poster
          full_path="https://image.tmdb.org/t/p/w500/"+poster_path
          return full_path

     except Exception as e:
          raise CustomException(e,sys)

def recommend(movie):
        try:
            ## we need the index of each movie title so that we recomend movies based on index
            index=movies[movies['title']==movie].index[0]
            ## for getting top 5 recomendations
            distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
            #cretaing list to get movie title
            recommend_movie=[]
            recommend_poster=[]
            for i in distance[1:11]:
                #getting movies id for poster
                movies_id=movies.iloc[i[0]].id
                #accesing the title of those index
                recommend_movie.append(movies.iloc[i[0]].title)
                recommend_poster.append(fetch_poster(movie_id=movies_id))
            
            return recommend_movie,recommend_poster
        except Exception as e:
             raise CustomException(e,sys)

if st.button("Show Recommend"):
    movie_name,movie_poster=recommend(select_value)

    # we need 5 columns for diaplaying recommend movies
    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10=st.columns(10)
    
    #getting each movie name 

    with col1:
         st.text(movie_name[0])
         st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
         st.text(movie_name[2])
         st.image(movie_poster[2])
    with col4:
         st.text(movie_name[3])
         st.image(movie_poster[3])
    with col5:
         st.text(movie_name[4])
         st.image(movie_poster[4])
    with col6:
         st.text(movie_name[5])
         st.image(movie_poster[5])
    with col7:
         st.text(movie_name[6])
         st.image(movie_poster[6])
    with col8:
         st.text(movie_name[7])
         st.image(movie_poster[7])
    with col9:
         st.text(movie_name[8])
         st.image(movie_poster[8])
    with col10:
         st.text(movie_name[9])
         st.image(movie_poster[9])