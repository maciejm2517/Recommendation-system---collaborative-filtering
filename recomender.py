import pandas as pd
from sklearn import metrics

item_similarity_df=pd.DataFrame()

def get_similar_movies(movie_name,user_rating):
    similar_score=item_similarity_df[movie_name]*(user_rating) # odejmujemy średnią ocen
    similar_score=similar_score.sort_values(ascending=False)
    return similar_score

def start():
    movies=pd.read_csv('movies.csv')
    ratings=pd.read_csv('ratings.csv')
    return movies,ratings

def recommender_module():
    movies,ratings=start()
    combined=pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
    user_ratings=combined.pivot_table(index=['userId'],columns=['title'],values='rating')
    user_ratings=user_ratings.dropna(thresh=10,axis=1).fillna(0)
    item_similarity=metrics.pairwise.cosine_similarity(user_ratings.T)
    item_similarity_df=pd.DataFrame(item_similarity,index=user_ratings.columns,columns=user_ratings.columns)
    #item_similarity_df=user_ratings.corr(method='pearson')
    return item_similarity_df
    

def prediction(input):
    print(input)

    similar_movies=pd.DataFrame()

    for movie in input:
        print(movie)
        print('------')
        print(input[movie])
        similar_movies=similar_movies.append(get_similar_movies(movie,input[movie]))
    return dict(similar_movies.sum().sort_values(ascending=False))

def get_names():
    return list(item_similarity_df.columns)