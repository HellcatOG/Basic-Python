
file = open("demo.txt","r")
    
content = file.read()
    
words = content.split()
print(words)

word_count = len(words)
    
print(f"The file contains {word_count} words.")