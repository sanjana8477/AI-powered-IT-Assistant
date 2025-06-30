# AI-powered Incident Resolution Assistant   
*Built by Team SheCodes for Code for Bharat - Season 2 (2025)*  
**Theme:** Generative AI & LLMs

---

## Overview

This project was developed during **Code for Bharat Season 2**, under the theme **Generative AI & LLMs**, by **Team SheCodes** (a team of four passionate women technologists). It is an AI-powered assistant designed to help IT support teams resolve incident tickets faster and more accurately. 

The assistant uses **Large Language Models (LLMs)**, **semantic search**, and **historical ticket embeddings** to:
- Recommend relevant resolutions
- Retrieve similar past incidents
- Answer troubleshooting questions via a natural-language interface

It features a modular, cloud-ready design and can be easily deployed on **Microsoft Azure**.

---

## Built For

🛠 **Code for Bharat - Season 2 Hackathon**  
🎯 **Theme:** Generative AI & LLMs  
👩‍💻 **Team Name:** SheCodes  
👥 **Team Members:**  
- Sanjana Kumari
- Suruchi Kumari
- Shruti Kumari
- Muskan Sohani

---

## Screenshots:
![Screenshot 2025-06-28 162641](https://github.com/user-attachments/assets/062754eb-d678-461a-821b-fd61691df08e)
![Screenshot 2025-06-28 160208](https://github.com/user-attachments/assets/118b3d33-556b-4125-a5a9-c6bf9390cd38)
![Screenshot 2025-06-28 160126](https://github.com/user-attachments/assets/e1d997ce-7018-4471-b3b4-ab30d267d0f2)



## Features

- **Semantic Search:** Find similar past incidents using vector embeddings and state-of-the-art language models.
- **Resolution Recommendation:** Get concise, step-by-step solutions for new incidents based on historical data.
- **Conversational Assistant:** Ask troubleshooting questions and receive AI-powered answers.
- **Interactive UI:** Streamlit-based chatbot interface for seamless agent interaction.
- **Cloud-Ready:** Easily containerized and deployable on Azure App Service, Azure Container Instances, or similar platforms.

---

## Architecture

Solution Architechture Diagram: 
![solution-architecture](https://github.com/user-attachments/assets/956949b1-26dd-446e-bc97-982ab678db82)


**Architecture Highlights:**
- **Ingestion:** Historical ITSM data (CSV) processed with Python and Pandas.
- **Vectorization:** Sentence Transformers convert ticket data into embeddings.
- **Vector Database:** ChromaDB stores embeddings for semantic search.
- **LLM Integration:** Ollama (open-source LLM) powers natural language understanding and solution generation(model used phi3).
- **Backend:** FastAPI exposes RESTful APIs for recommendations, search, and Q&A.
- **Frontend:** Streamlit provides an easy-to-use chatbot UI for agents.
- **Azure-ready:** Components are containerized and compatible with Azure services.

---

## Technologies Used

- **Python:** Core language for backend, data processing, and ML integration
- **FastAPI:** High-performance web framework for backend APIs
- **Ollama:** Open-source large language model for conversational AI
- **Sentence Transformers:** For generating semantic embeddings of ticket data
- **ChromaDB:** Vector database for efficient similarity search
- **Streamlit:** Rapid UI development for the chatbot interface
- **Pandas:** Data cleaning and preparation

---

## Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) server running (for LLM)
- Docker (optional, for containerized deployment)
- (Recommended) Azure account for cloud deployment

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SuruchiCode/AI-powered-Incident-Resolution-Assistant.git
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up historical ticket data**
   - Place your ITSM CSV file in the `data/` directory.

4. **Start ChromaDB and embedding model**
   - No separate ChromaDB server required; the app handles this.
   - Make sure you have enough memory to load the Sentence Transformer model.

5. **Run Ollama server**
   ```bash
   ollama serve
   ollama pull phi3
   ollama run phi3
   ```

6. **Start the FastAPI backend**
   ```bash
   uvicorn main:app --reload
   ```

7. **Run the Streamlit frontend**
   ```bash
   streamlit run chatbot.py
   ```

8. **Access the UI**
   - Open the Streamlit URL in your browser (usually `http://localhost:8501`).

---

## Example Usage

1. **Enter a new incident description:**  
   The assistant suggests probable resolutions.
2. **Search for similar incidents:**  
   Retrieve historical tickets related to the current issue.
3. **Ask troubleshooting questions:**  
   Get concise, AI-generated answers.

---

## License

[MIT License](LICENSE)

---

## Authors

- Suruchicodes(Suruchi Kumari)

---

## Acknowledgments

- Open-source community for Ollama, FastAPI, ChromaDB, and Sentence Transformers.

