from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import customtkinter as ctk 
from PIL import Image, ImageTk

#template for api 
template = """
Answer the question below.

Here is the conversatiom history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

context=""

#conversation between api and user
def handle_conversation():
    global context 
    user_input = prompt_entry.get().strip()
    if user_input:
        prompt_entry.delete(0,ctk.END)
        output.insert(ctk.END, f"You: {user_input}\n")
        result = chain.invoke({'context': context,'question': user_input})
        output.insert(ctk.END, f"VirtuBot: {result}\n")
        context += f"\nUser: {user_input}\n AI: {result}"
 
root = ctk.CTk()
root.configure(fg_color='#FFFFFF')

og_icon = Image.open('Virtubot.png').resize((50,50))
icon = ImageTk.PhotoImage(og_icon)
icon_label = ctk.CTkLabel(root, image=icon)


#tkinter
root.geometry('750x550')
root.title("VirtuBot")


title_label = ctk.CTkLabel(root, text = "VirtuBot", image=icon, compound='left',
                        text_color='#007FFF' , font=ctk.CTkFont(size=30, weight='bold'))
title_label.pack(padx=10, pady=(40,20))


frame = ctk.CTkFrame(root)
frame.configure(fg_color='#007FFF')
frame.pack(padx=10, pady=10, fill='both')


output = ctk.CTkTextbox(frame, text_color='#00FF00', font=ctk.CTkFont(size=15), wrap = 'word', height=300)
output.pack(fill='both', padx=20, pady=10)

prompt_entry= ctk.CTkEntry(frame, text_color='#00FF00',placeholder_text="Type your message here", font=('Arial',16))
prompt_entry.pack(fill='both', padx=20, pady=10) 

submit_button= ctk.CTkButton(frame, text='Submit', text_color='#000000', fg_color='#00FF00',command= handle_conversation)
submit_button.pack(pady=10)

root.mainloop()



