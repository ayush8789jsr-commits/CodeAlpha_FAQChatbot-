from tkinter import *
from tkinter import scrolledtext
from rapidfuzz import process

faq_data = {
    "what is python": "Python is a high-level programming language.",
    "who developed python": "Python was developed by Guido van Rossum.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is artificial intelligence": "Artificial Intelligence enables machines to mimic human intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI.",
    "what is deep learning": "Deep Learning uses neural networks.",
    "what is data science": "Data Science extracts insights from data.",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what is computer vision": "Computer Vision helps machines understand images and videos.",
    "what is chatbot": "A chatbot is a software application that simulates conversation.",
    "what is tkinter": "Tkinter is Python's standard GUI library.",
    "what is codealpha": "CodeAlpha provides internships and project opportunities.",

    "what is java": "Java is an object-oriented programming language.",
    "what is c++": "C++ is a powerful programming language.",
    "what is c": "C is a general-purpose programming language.",
    "what is javascript": "JavaScript is used to make websites interactive.",
    "what is html": "HTML is used to structure web pages.",
    "what is css": "CSS is used to style web pages.",

    "what is github": "GitHub is a platform for hosting code repositories.",
    "what is git": "Git is a version control system.",
    "what is repository": "A repository stores project files and version history.",
    "what is open source": "Open source software allows anyone to view and modify code.",

    "what is sql": "SQL is used to manage databases.",
    "what is database": "A database stores and organizes data.",
    "what is mysql": "MySQL is a relational database management system.",

    "what is cloud computing": "Cloud computing provides services over the internet.",
    "what is aws": "AWS is Amazon's cloud computing platform.",
    "what is azure": "Azure is Microsoft's cloud platform.",

    "what is cybersecurity": "Cybersecurity protects systems from digital attacks.",
    "what is encryption": "Encryption converts data into a secure format.",
    "what is firewall": "A firewall monitors and controls network traffic.",

    "what is operating system": "An operating system manages computer hardware and software.",
    "what is linux": "Linux is an open-source operating system.",
    "what is windows": "Windows is an operating system developed by Microsoft.",

    "what is api": "An API allows software applications to communicate.",
    "what is json": "JSON is a lightweight data-interchange format.",
    "what is xml": "XML is used to store and transport data.",

    "what is neural network": "A neural network is inspired by the human brain.",
    "what is supervised learning": "Supervised learning uses labeled data.",
    "what is unsupervised learning": "Unsupervised learning finds patterns in unlabeled data.",
    "what is reinforcement learning": "Reinforcement learning learns through rewards and penalties.",

    "what is big data": "Big data refers to extremely large datasets.",
    "what is iot": "IoT connects physical devices through the internet.",
    "what is blockchain": "Blockchain is a decentralized digital ledger.",
    "what is cryptocurrency": "Cryptocurrency is a digital currency secured by cryptography.",

    "what is software engineering": "Software engineering is the process of developing software.",
    "what is algorithm": "An algorithm is a step-by-step procedure to solve a problem.",
    "what is data structure": "A data structure organizes data efficiently.",
    "what is array": "An array stores multiple values of the same type.",
    "what is linked list": "A linked list is a linear data structure made of nodes.",
    "what is stack": "A stack follows the Last In First Out principle.",
    "what is queue": "A queue follows the First In First Out principle.",

    "what is internship": "An internship provides practical work experience.",
    "what is prompt engineering": "Prompt engineering is the process of designing effective AI prompts."
}
def send_message():
    user_input = entry_box.get().strip()

    if not user_input:
        return

    chat_area.config(state=NORMAL)

    chat_area.insert(
        END,
        f"\n🧑 You: {user_input}\n"
    )

    match = process.extractOne(
        user_input.lower(),
        faq_data.keys()
    )

    if match and match[1] >= 60:
        response = faq_data[match[0]]
    else:
        response = "Sorry, I could not find a suitable answer."

    chat_area.insert(
        END,
        f"🤖 Bot: {response}\n"
    )

    chat_area.config(state=DISABLED)
    chat_area.yview(END)

    entry_box.delete(0, END)

def clear_chat():
    chat_area.config(state=NORMAL)

    chat_area.delete(1.0, END)

    chat_area.insert(
        END,
        "🤖 Bot: Welcome to FAQ Chatbot!\nAsk me any FAQ related question.\n"
    )

    chat_area.config(state=DISABLED)

root = Tk()
root.title("FAQ Chatbot")
root.geometry("800x600")

title = Label(
    root,
    text="FAQ Chatbot",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=WORD,
    width=90,
    height=25,
    font=("Arial", 11)
)

chat_area.pack(padx=10, pady=10)

chat_area.insert(
    END,
    "🤖 Bot: Welcome to FAQ Chatbot!\nAsk me any FAQ related question.\n"
)

chat_area.config(state=DISABLED)

bottom_frame = Frame(root)
bottom_frame.pack(pady=10)

entry_box = Entry(
    bottom_frame,
    width=60,
    font=("Arial", 12)
)

entry_box.grid(row=0, column=0, padx=10)

send_btn = Button(
    bottom_frame,
    text="Send",
    width=12,
    command=send_message
)

send_btn.grid(row=0, column=1)

clear_btn = Button(
    bottom_frame,
    text="Clear Chat",
    width=12,
    command=clear_chat
)

clear_btn.grid(row=0, column=2, padx=10)

root.bind(
    "<Return>",
    lambda event: send_message()
)

root.mainloop()