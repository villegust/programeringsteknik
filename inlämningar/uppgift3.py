
#Funktion som tar bort alla specialtecken i texten. 
def clean_text(t):
    special_character = {"-":"", ".":"", ",":"", "!":""}
    clear_text = ""

    for char in t:
        if char in special_character:
            clear_text += special_character[char]
        
        else:
            clear_text += char

    return clear_text

#Funktion som räknar ut totala antalet unika ord.
def unique_words(t):
    return list(set(t))

#Funtion som räknar ut antalet av alla ord i texten
def word_count(t):
    count = {}

    for word in t:
        if word in count:
            count[word] += 1

        else:
            count[word] = 1

    return count

def most_common(word_counts):
    return max(word_counts.items(), key=lambda x: x[1])

def least_common(word_counts):
    return min(word_counts.items(), key=lambda x: x[1])

filename = "dikt.txt"

text_file = open(filename, "r", encoding='utf8')

text = text_file.read().lower()
text_file.close()


#Splitar upp texten och ränkar alla antal ord i "split_text" 
split_text= clean_text(text).split()
word_counts = word_count(split_text)

c_word= int(input("Hur många av de vanligaste orden vill du se?: "))
r_word= int(input("Hur många av de ovanligaste orden vill du se?: "))

#Printar totala antal ord och totala antal unika ord.
print(f"Totalt antal ord: {len(split_text)}")
print(f"Totalt antal unika ord: {len(unique_words(split_text))} \n")

"""
sorted_words konverterar word_counts till en lista med key value pairs.
lambda x: x[1] sorterar efter den andra elementet, vilket är antalet.

""" 
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

#Loopar igenom de valigaste orden och printar dem enligt antalet man har anget i c_word
print(f"De {c_word} vanligaste orden var (antal förekommer inom parantes): ")
for i in range(min(r_word, len(sorted_words))):
    word, count = sorted_words[(i)]
    print(f"{i + 1}. {word} ({count})")
print("\n")

#Loopar igenom de ovaligaste orden och printar dem enligt antalet man har anget i r_word
print(f"De {r_word} ovanligaste orden var (antal förekommer inom parantes): ")
for i in range(min(r_word, len(sorted_words))):
    word, count = sorted_words[-(i + 1)]
    print(f"{i + 1}. {word} ({count})")