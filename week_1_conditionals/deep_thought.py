deep = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()

if deep == "42" or deep == "forty two" or deep == "forty-two":
    print("Yes")
else:
    print("No")

#SECOND WAY OF REPRESENTING THE SAME CODE (MORE PYTHONIC)

#deep = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()

#print("Yes" if deep in ["42", "forty two", "forty-two"] else "No")
