filename = "dikt.txt"

text_file = open(filename, "r", encoding='utf8')

text = text_file.read().lower()
text_file.close()

special_character = {"-":"", ".":"", ",":"", "!":""}
clear_text = ""

for char in text:
    if char in special_character:
        clear_text += special_character[char]
    
    else:
        clear_text += char

#Splitar upp texten 
splitted_text= clear_text.split()
unique_words = list(set(splitted_text))

common_word= int(input("Hur många av de vanligaste orden vill du se?: "))
rare_word= int(input("Hur många av de ovanligaste orden vill du se?: "))

#Räknar ut antalet av alla ord
word_count = {}

for word in splitted_text:
    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1

#Hittar de vanligaste och ovanligaste orden
most_common_word = max(word_count, key=word_count.get)
most_common_count = word_count[most_common_word]


sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)


print(f"Totalt antal ord: {len(splitted_text)}")
print(f"Totalt antal unika ord: {len(unique_words)}")
print("\n")

print(f"De {common_word} vanligaste orden var (antal förekommer inom parantes): ")
for i in range(min(common_word, len(sorted_words))):
    word, count = sorted_words[i]
    print(f"{i + 1}. {word} ({count})")

print(f"De {rare_word} ovanligaste orden var (antal förekommer inom parantes): ")
for i in range(min(rare_word, len(sorted_words))):
    word, count = sorted_words[-(i + 1)]
    print(f"{i + 1}. {word} ({count})")


