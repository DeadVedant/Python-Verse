def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    sample = "Python Programming"
    print(f"Number of vowels in '{sample}': {count_vowels(sample)}")
