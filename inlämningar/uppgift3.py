import re

#Funtion som räknar ut antalet av alla ord i texten
def word_count(t):
    count = {}

    for word in t:
        if word in count:
            count[word] += 1

        else:
            count[word] = 1

    return count

filename = "dikt.txt"

with open(filename, "r", encoding='utf8') as text_file:
    text = text_file.read().lower()

#Tar bort alla specialtecken och delar upp det i en lista med alla ord
wordlist = re.findall(r"[a-zA-ZåäöÅÄÖ]+", text)

#Splitar upp texten och ränkar alla antal ord i "split_text" 
word_counts = word_count(wordlist)

common_word= int(input("Hur många av de vanligaste orden vill du se?: "))
rare_word= int(input("Hur många av de ovanligaste orden vill du se?: "))

#Printar totala antal ord och totala antal unika ord.
print(f"Totalt antal ord: {len(wordlist)}")
print(f"Totalt antal unika ord: {len(set(wordlist))} \n")

"""
sorted_words konverterar word_counts till en lista med key value pairs.
lambda x: x[1] sorterar efter den andra elementet, vilket är antalet.

""" 
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

#Loopar igenom de valigaste orden och printar dem enligt antalet man har anget i common_word
if common_word > len(set(wordlist)) or common_word < 0:
    print(f"{common_word} vanliga ord finns inte i texten. Max antal är {len(set(wordlist))}")

else:
    print(f"De {common_word} vanligaste orden var (antal förekommer inom parantes): ")
    for i in range(0, common_word):
        word, count = sorted_words[i]
        print(f"{i + 1}. {word:<20} ({count})")

print("\n")

#Loopar igenom de ovaligaste orden och printar dem enligt antalet man har anget i rare_word
if rare_word > len(set(wordlist)) or rare_word < 0:
    print(f"{rare_word} ovanliga ord finns inte i texten. Max antal är {len(set(wordlist))}")

else:
    print(f"De {rare_word} ovanligaste orden var (antal förekommer inom parantes): ")
    for i in range(0, rare_word):
        word, count = sorted_words[-(i + 1)]
        print(f"{i + 1}. {word:<20} ({count})")

