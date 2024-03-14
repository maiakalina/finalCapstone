# Semantic Similarity and Movie Recommendation Programme

This Python programme demonstrates the use of spaCy for semantic similarity analysis and movie recommendation based on text descriptions.

## Semantic Similarity (Practical Task 1)

This part of the programme evaluates the semantic similarity between different words using the spaCy library.

### Results:
- **Task 1:** The programme computes the similarity between various words such as "cat", "monkey", and "banana". It observes significant similarity between "cat" and "monkey" as both are animals, lower but still noticeable similarity between "monkey" and "banana", and no significant similarity between "cat" and "banana".
- **Task 2:** The programme computes the similarity between pairs of words from a predefined list ("letter", "laptop", "travel", "flower"). It provides insights into the semantic relationships between these words.

### Observations:
- The programme was executed using both small and medium language models of spaCy. The medium model yielded higher similarity indexes without encountering any "no word vectors" error.

## Movie Recommendation (Practical Task 2)

This part of the programme recommends a movie based on a given text description by comparing the similarity between the input description and movie descriptions stored in a text file.

### Approach:
1. **Load Movie Data:** The programme reads movie titles and descriptions from a text file.
2. **Process Description:** It processes the input description using spaCy.
3. **Compute Similarity:** For each movie description, the programme computes the similarity between the input description and the movie description.
4. **Recommendation:** The programme recommends the movie with the highest similarity score.

### Example:
- **Input Description:** "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
- **Recommended Movie:** "Hulk (2003)"

## How to Use
1. Ensure that you have installed the required dependencies, including spaCy.
2. Run the programme using a Python interpreter.
3. Observe the semantic similarity results and the recommended movie based on the input description.

## Contact
- **Author:** Maïa Kalina
- **Email:** [kalina.maiya@gmail.com](mailto:kalina.maiya@gmail.com)

Feel free to reach out with any questions or feedback! 🚀