import spacy
nlp = spacy.load('en_core_web_md')

# Practical task 1
print("Practical task 1")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))
# Observed significant similarity between 'cat' and 'monkey' as both are animals.
# Lower but still noticeable similarity betwen 'monkey' and 'banana'.
# No significant similarity between 'cat' and 'banana'

tokens = nlp('letter laptop travel flower')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# I ran the semantic similarity example file with both small and medium language models. 
# The medium model has returned higher similarity indexes with no 'no word vectors' error.

# Practical task 2
print("Practical task 2")

def recommend_movie(description):
    with open('/Users/maiiakalina/Desktop/task 20/movies.txt', 'r') as file:
        # Read the contents of the file
        movie_data = file.readlines()
        print(movie_data)
    # Dictionary to store movie titles and descriptions
    movies = {}

    # Extract movie titles and descriptions from the file
    for line in movie_data:
        if ':' in line:
            title, desc = line.split(':')
            movies[title.strip()] = desc.strip()

    # Initialise variables to store the most similar movie and its similarity score
    most_similar_movie = None
    max_similarity = 0
    
    # Process the input description using spacy
    doc_input = nlp(description)
    
    # Iterate through the movies and their descriptions
    for movie, desc in movies.items():
        # Process the movie description using spacy
        doc_movie = nlp(desc)
        # Calculate similarity between the input description and the movie description
        similarity = doc_input.similarity(doc_movie)
        # Update the most similar movie if the current similarity is higher
        if similarity > max_similarity:
            most_similar_movie = movie
            max_similarity = similarity
    
    return most_similar_movie

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie = recommend_movie(description)
print("Recommended movie:", recommended_movie)