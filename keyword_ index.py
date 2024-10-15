#First
def key_index(docs):
    index = {}
    for doc_idx,doc in enumerate(docs):
        for word in doc.split():
            if word in index:
                index[word].append(doc_idx)
            else:
                index[word] = [doc_idx]
    return index

#Second
def keyword_index(docs):
    index = {}  # Initialize the inverted index dictionary
    for doc_id, doc in enumerate(docs):  # Iterate over each document with its index
        for word in doc.split():  # Split the document into words
            if word in index:  # If the word is already in the index
                # If the doc_id is already in the word's count dictionary, increment it
                if doc_id in index[word]:
                    index[word][doc_id] += 1
                else:
                    index[word][doc_id] = 1  # Initialize the count for this doc_id
            else:
                index[word] = {doc_id: 1}  # Create a new entry with count 1
    return index

# Example documents
docs = ["Hello world", "world world of python", "python is a snake"]
# Call the function and print the result
print(keyword_index(docs))
