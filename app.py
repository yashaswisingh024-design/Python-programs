def similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    common = words1.intersection(words2)
    
    total = (len(words1) + len(words2)) / 2
    score = (len(common) / total) * 100

    return round(score, 2)


print("🧠 Text Similarity Checker\n")

t1 = input("Enter first text: ")
t2 = input("Enter second text: ")

result = similarity(t1, t2)

print(f"\nSimilarity: {result}%")