def return_evens(sequence):
    """
    Returns a list of all even elements in the given sequence of integers.
    """
    return [num for num in sequence if num % 2 == 0]

def make_exclamation(sentences):
    """
    Takes a list of sentence strings and returns a list of sentence strings
    with exclamation marks at the end.
    """
    return [sentence + '!' for sentence in sentences]

# Additional test cases
if __name__ == "__main__":
    # Test return_evens
    sequence1 = [0, 1, 3, 5, 7, 8, 9]
    print(return_evens(sequence1))  # Expected output: [0, 8]

    sequence2 = [2, 4, 6, 8, 10]
    print(return_evens(sequence2))  # Expected output: [2, 4, 6, 8, 10]

    # Test make_exclamation
    sentences1 = ["Hello", "I'm doing great", "Python is fun"]
    print(make_exclamation(sentences1))
    # Expected output: ["Hello!", "I'm doing great!", "Python is fun!"]

    sentences2 = ["Testing", "List comprehensions", "Are awesome"]
    print(make_exclamation(sentences2))
    # Expected output: ["Testing!", "List comprehensions!", "Are awesome!"]
