import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

def count_pos_tags(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Initialize counters
    verb_count = 0
    noun_count = 0
    pronoun_count = 0
    adjective_count = 0
    
    # Iterate over each sentence
    for sentence in sentences:
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Perform POS tagging
        tagged_words = pos_tag(words)
        
        # Count the POS tags
        for word, tag in tagged_words:
            if tag.startswith('VB'):
                verb_count += 1
            elif tag.startswith('NN'):
                noun_count += 1
            elif tag.startswith('PRP'):
                pronoun_count += 1
            elif tag.startswith('JJ'):
                adjective_count += 1
    
    # Create a dictionary to store the counts
    pos_counts = {
        'Verbs': verb_count,
        'Nouns': noun_count,
        'Pronouns': pronoun_count,
        'Adjectives': adjective_count
    }
    
    return pos_counts

# Test the function with a phrase
phrase = "I love eating pizza."
counts = count_pos_tags(phrase)
print(counts)

# Additional Test Case 1
# A paragraph with varied parts of speech
paragraph1 = "The cat sat on the mat. It was a sunny day. The big brown dog barked loudly."
counts1 = count_pos_tags(paragraph1)
print(counts1)

# Additional Test Case 2
# A phrase with multiple verbs and pronouns
phrase2 = "She runs, he dances, they sing."
counts2 = count_pos_tags(phrase2)
print(counts2)
