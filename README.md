Full README.md
# 🔥 Advanced Personal Assistant (Streamlit + LangChain)

An advanced AI-powered chatbot built using:

- Streamlit  
- LangChain  
- OpenAI GPT Model  
- Session Memory (Conversation History)

This chatbot remembers the conversation and responds intelligently like ChatGPT.

---

## 🚀 Features

✅ Chat-style UI  
✅ Conversation memory  
✅ Structured AI responses  
✅ Clean Streamlit interface  
✅ Uses OpenAI GPT model  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- OpenAI API  
- python-dotenv

---

## 📁 Project Structure


new_project/
│
├── app.py
├── .env
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone Repository


git clone https://github.com/bhupender5/
<your-repo-name>.git
cd <your-repo-name>


---

### 2️⃣ Create Conda Environment


conda create -n nlp_env python=3.11
conda activate nlp_env


---

### 3️⃣ Install Dependencies


pip install streamlit langchain langchain-openai python-dotenv


---

## 🔑 Environment Variables

Create a `.env` file in the project root:


OPENAI_API_KEY=your_openai_api_key_here


---

## ▶️ Run The Application


streamlit run app.py


After running, open this in your browser:


http://localhost:8501


---

## 🧠 How It Works

- Uses `ChatOpenAI` from LangChain  
- Keeps chat history in `st.session_state`  
- Uses prompt templates with memory  
- Displays user and AI messages in interactive UI  

---

## 📌 Future Improvements

✔ Streaming responses  
✔ Tool/function calling support  
✔ RAG support  
✔ User authentication  
✔ Deploy to Streamlit Cloud  

---

## 👨‍💻 Author

**Bhupender Singh**  
BTech | AI | Data Science | GenAI Enthusiast  

🔗 GitHub: https://github.com/bhupender5  
🔗 LinkedIn: https://www.linkedin.com/in/bhupinder-singh-bba271187  

---

## 📜 License

This project is built for learning and educational purposes.
