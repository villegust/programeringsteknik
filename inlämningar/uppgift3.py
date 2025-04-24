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

def part2(element):
    return element[1]

with open("dikt.txt", "r", encoding="utf8") as text_file:
    text = text_file.read().lower()

#Tar bort alla specialtecken och delar upp det i en lista med alla ord
wordlist = re.findall(r"[a-zA-ZåäöÅÄÖ]+", text)

common_word= int(input("Hur många av de vanligaste orden vill du se?: "))
rare_word= int(input("Hur många av de ovanligaste orden vill du se?: "))

#Printar totala antal ord och totala antal unika ord.
print(f"Totalt antal ord: {len(wordlist)}")
print(f"Totalt antal unika ord: {len(set(wordlist))} \n")

sorted_words = sorted(word_count(wordlist).items(), key=part2, reverse=True)

#Loopar igenom de valigaste orden och printar dem enligt antalet man har anget i common_word
print(f"De {common_word} vanligaste orden var (antal förekommer inom parantes): ")
for i in range(0, common_word):
    word, count = sorted_words[i]
    print(f"{i + 1}. {word:<20} ({count})")

print("\n")

#Loopar igenom de ovaligaste orden och printar dem enligt antalet man har anget i rare_word
print(f"De {rare_word} ovanligaste orden var (antal förekommer inom parantes): ")
for i in range(0, rare_word):
    word, count = sorted_words[-(i + 1)]
    print(f"{i + 1}. {word:<20} ({count})")