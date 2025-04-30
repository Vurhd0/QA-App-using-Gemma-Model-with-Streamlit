# 🧠 LangChain + Streamlit + Ollama (Gemma 2B) Question Answering App

This project is a simple interactive **Question-Answering** web application built using:
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/) (for local inference of `gemma:2b` model)
- `.env` for managing secrets and configuration

---

## 🚀 Features

- ✅ Local LLM interaction using **Gemma 2B** via Ollama
- ✅ Clean output parsing with `StrOutputParser`
- ✅ Dynamic prompt templating using LangChain
- ✅ Simple web UI with Streamlit
- ✅ API key and project settings managed via `.env`
- ✅ LangChain Tracing V2 enabled for debugging and observability

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Vurhd0/QA-App-using-Gemma-Model-with-Streamlit
cd QA-App-using-Gemma-Model=with-Streamlit
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Set up .env
Create a .env file in the project root and add the following variables:
```
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_langchain_project_name
```
### 4. Start Ollama and Pull Gemma Model

Install Ollama and run:
```
ollama pull gemma:2b
```
Ensure the Ollama server is running locally.

## ▶️ Run the App
```
streamlit run app.py
```

## 🧠 How It Works
- The user inputs a natural language question into the Streamlit app.

- LangChain creates a structured prompt using ChatPromptTemplate.

- The prompt is sent to the gemma:2b model running via Ollama.

- The response is parsed and displayed back in the app UI.

## 📸 Screenshot
![image](https://github.com/user-attachments/assets/b2d5321e-ce28-4a64-a330-718ce3714c44)

