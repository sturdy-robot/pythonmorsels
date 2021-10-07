def count_words(sentence):
    punctuation = '.!:¿,?'
    sentences = [word.strip(punctuation) for word in sentence.lower().split()]

    sentences_counts = dict.fromkeys(sentences, 0)
    for s in sentences:
        sentences_counts[s] += 1
    
    return sentences_counts
