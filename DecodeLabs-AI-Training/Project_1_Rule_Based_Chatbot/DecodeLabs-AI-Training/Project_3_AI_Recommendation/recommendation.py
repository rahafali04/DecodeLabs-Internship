import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Phase 1 : Prepare the dataset 
#We will create a dictionary of articles/courses available in our system. 

data = {
    'item_id': [1, 2, 3, 4, 5],
    'title': ['Introduction to Python Programming',
             'Advanced Data Science and Machine Learning',
            'Frontend Web Development with React', 
            'Deep Learning and Neural Networks', 
            'UI/UX Design Fundamentals'],
    
    'tags': ['python coding programming software basics', 
             'data science machine learning pthon statistics artificial intelligence', 
             'web development frontend react javascript html css', 
             'deep learning neural networks artificial intelligence python tensors', 
             'ui ux design user interface user experience wireframing mockups']
    
}

#Convert the dictionary into a pandas DataFrame 
df = pd.DataFrame(data)
print ("Data Loaded Successfully")
print(df[['item_id', 'title']])
print ('-'*50)

#phase 2 : user preferences input
#we define what the user likes. In a real system, this comes from their profile or search history.
#Senario: The user is deeply interested in Artificial Intelligence and Python.
user_perference = "I want to learn python and  artificial intelligence for data science."
print ("User Profile/Preferences Captured")
print(f"User Input: '{user_perference}'")
print ('-'*50)


#Phase 3 : Text vectorization using TF-IDF
#we initialize the TF-IDF vectorizer to convert the text tags into mathematical weights.
tfidf = TfidfVectorizer(stop_words='english')

#1. learn the vocabulary and calculate weights for all items in the dataset
tfidf_matrix = tfidf.fit_transform(df['tags'])

#2. Convert the user preference text using the exact same vocabulary mapping.
user_vector = tfidf.transform([user_perference])
print ("TF-IDF Vectorization Completed")
print (f"Items Matrix Shape: {tfidf_matrix.shape} (5 Items, Unique Words)")
print (f"User Vector Shape: {user_vector.shape} (1 User Profile, Same Unique Words)")
print ('-'*50)

#Phase 4 : Calculate similarity and generate recommendations
#Compute the Cosine Similarity between the user vector and all item vectors in the dataset.
similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

#Add the calculated scores as a new column in our dataframe 
df['similarity_score'] = similarity_scores

#sort the items based on similarity score in descending order (highest first)
recommendations = df.sort_values(by='similarity_score', ascending=False)
print("Recommendations Generated (Top-N List)")
#Display the final output to user 
for index, row in recommendations.iterrows():
    #convert score to percentage for clear reasoning
    percentage = row['similarity_score'] * 100
    print(f"-> Recommended : '{row['title']}' | Match Score: {percentage:.2f}%") 

    print ('='*50)
          