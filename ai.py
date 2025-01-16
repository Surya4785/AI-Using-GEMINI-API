import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai

genai.configure(api_key="AIzaSyB4T0aZYeWSt_dBx4uLumk9yGRDbNGFRBk")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response():
    user_input = user_input_entry.get()
    if not user_input.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    
    try:
        response = model.generate_content(user_input)
        response_text = response.text
        
        chat_display.config(state=tk.NORMAL)
        
        chat_display.insert(tk.END, "You: " + user_input + "\n")
        chat_display.insert(tk.END, "Bot: " + response_text + "\n")
        
        chat_display.yview(tk.END)
    
        user_input_entry.delete(0, tk.END)
        
        chat_display.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("ChatBot App")

chat_display = tk.Text(root, height=15, width=50, state=tk.DISABLED, wrap=tk.WORD)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

user_input_entry = tk.Entry(root, width=40)
user_input_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=get_response)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()