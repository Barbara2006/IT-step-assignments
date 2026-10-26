
def analyze_text(text: str, target_word: str) -> tuple:
    words = text.split()

    total_words = len(words)

    target_count = 0
    for word in words:
        if word.lower() == target_word.lower():
            target_count += 1

    longest_word = max(words, key=len) if words else ""

    return total_words, target_count, longest_word


result = analyze_text("Python is great and Python is fun", "python")
print(result)
