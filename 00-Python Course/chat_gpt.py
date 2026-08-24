
import re
import random

# List of dishes to use for replacements
dishes = ["🍕", "🍔", "🍣", "🍜", "🥗", "🍝", "🌮", "🍛", "🥟", "🍩", "🍤", "🍞", "🧀", "🍗"]

def replace_with_dishes(text, keep_last_word=True):
    # Step 1: Remove special characters (keep letters, numbers, and spaces)
    cleaned_text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    
    # Step 2: Normalize whitespace
    words = cleaned_text.strip().split()
    
    if not words:
        return ""

    # Step 3: Replace words with dishes
    new_words = []
    for i, word in enumerate(words):
        if keep_last_word and i == len(words) - 1:
            new_words.append(word)
        else:
            new_words.append(random.choice(dishes))
    
    return ' '.join(new_words)

# Example usage
input_str = "hey  you are good "
output_str = replace_with_dishes(input_str)
print("Input:", input_str)
print("Output:", output_str)
