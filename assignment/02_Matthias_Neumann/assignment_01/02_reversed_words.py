#!/usr/bin/python3

## Task 02 – Reversed Words

if __name__ == "__main__":
    word=input("Please enter a word: ")
    print(end="'")
    for i in range(len(word)  -1,-1,-1):
        print(end=word[i])
    print("'")
