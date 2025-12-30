import requests
import tkinter as tk

def get_random_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        quote_text.set(f'"{quote}"\n\n— {author}')

    except Exception as e:
        quote_text.set("API failed (not internet issue)")


# GUI setup
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x200")

quote_text = tk.StringVar(value="Click the button to get a quote")

quote_label = tk.Label(
    root,
    textvariable=quote_text,
    wraplength=350,
    font=("Helvetica", 12),
    justify="center"
)
quote_label.pack(pady=20)

new_quote_button = tk.Button(
    root,
    text="Get a New Quote",
    command=get_random_quote
)
new_quote_button.pack()

root.mainloop()
