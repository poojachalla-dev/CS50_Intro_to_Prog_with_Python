user_prompt = input("Enter the file name: ").strip().lower()

if user_prompt.endswith(".gif"):
    print("image/gif")
elif user_prompt.endswith(".jpg") or user_prompt.endswith(".jpeg"):
    print("image/jpeg")
elif user_prompt.endswith(".png"):
    print("image/png")
elif user_prompt.endswith(".pdf"):
    print("application/pdf")
elif user_prompt.endswith(".txt"):
    print("text/plain")
elif user_prompt.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

