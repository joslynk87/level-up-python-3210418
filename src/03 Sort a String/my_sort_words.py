def sort_words(phrase):
  phrase_array = phrase.strip().split()
  return ' '.join(sorted(phrase_array, key=str.casefold))


print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
