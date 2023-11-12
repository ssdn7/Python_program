def word_count(S, x):
    count=0
    for word in S:
        if word == x:
            count+=1
    return count
S= (input("Input a sentences: ").split())
x=input("Input a word to search: ")
count = word_count(S, x)
print(f"In S, {x} is appeared in {count} times. ")