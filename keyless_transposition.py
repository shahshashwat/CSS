str = "work hard"
n = 3 
chunks = [str[i:i+n] for i in range(0, len(str), n)]

result = ""
for i in range(3):
    for word in chunks:
        try:
            result += word[i]
        except:
            pass

print(result)