# Movie recommendation system using content Based filtering

![image](https://github.com/seruvuri/Movie_Recommendation_System/assets/109864276/1c5b1b41-4c27-42fe-b926-c196da8a255c)

## TOP 10 Movie recommendations 

## Components

### <a data_ingestion="src/components/data_ingestion.py">Data_ingestion</a>
    Getting movies data from  MongoDB database

### data_transformation

    Removing Unnecessary columns from dataset
    
    adding "Tags" column for further analysis
    
    Dropping "genere","overview" columns form dataset
    
    Saving movies list to pickle file

  ### recommendation_trainer

  > using to *CounterVectorizer* to analyzing text in "tags" column and converting into vector matrix

    from sklearn.feature_extraction.text import CountVectorizer
    
  > using *Cosine similarity* from sklearn for finding similarity between indexs

    from sklearn.metrics.pairwise import cosine_similarity
  
   ## Application

  Creating application using Streamlit 

  Getting movies posters from :https://www.themoviedb.org/

  Background Image:https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2qgyPZtCm912SgXnxty14um8o7VIeB9FT1A&usqp=CAU

  TMDB API for getting movie posters :https://api.themoviedb.org/3/movie/{}?api_key
