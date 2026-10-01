def summarize_text(text):
    prompt = f"Summarize this text in simple language:\n\n{text}"
    return prompt


def explain_text(text):
    prompt = f"Explain this text in simple beginner-friendly language:\n\n{text}"
    return prompt


def improve_text(text):
    prompt = f"Improve the writing of this text while keeping the meaning:\n\n{text}"
    return prompt


print("AI Text Assistant")
print("------------------")

print("1. Summarize Text")
print("2. Explain Text")
print("3. Improve Text")

choice = input("Enter your choice: ")
text = input("Enter your text: ")

if text.strip() == "":
    print("Please enter some text.")
    exit()


if choice == "1":
    result = summarize_text(text)

elif choice == "2":
    result = explain_text(text)

elif choice == "3":
    result = improve_text(text)

else:
    result = "Invalid choice. Please choose 1, 2, or 3."


print("\nResult:")
print(result)