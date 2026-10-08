text = input("Enter string: ")

seen = set()

for ch in text:
    if ch in seen:
        print(ch)
        break

    seen.add(ch)
