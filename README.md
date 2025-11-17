# Text-Summarization-Using-NLP-and-Deep-Learning

# Text Summarization Using NLP and Deep Learning (T5 Transformer)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Transformers-HuggingFace-yellow)
![Framework](https://img.shields.io/badge/Framework-PyTorch-red)
![Interface](https://img.shields.io/badge/Interface-Gradio-orange)

## 📌 Project Overview
This project implements an **Abstractive Text Summarization system** using the **T5 (Text-to-Text Transfer Transformer)** model. [cite_start]Unlike extractive methods that simply clip sentences, this system leverages deep learning to generate concise, coherent, and semantically rich summaries that capture the essence of the input text[cite: 60, 83].

[cite_start]The model is fine-tuned on the **CNN/DailyMail dataset** and deployed using a **Gradio** web interface for real-time user interaction[cite: 63, 65].

## 🚀 Key Features
* [cite_start]**Abstractive Summarization:** Generates new sentences to summarize content rather than just extracting existing phrases[cite: 83].
* [cite_start]**Fine-Tuned T5 Model:** Optimized on the CNN/DailyMail dataset for news and article summarization[cite: 109].
* [cite_start]**User-Friendly Interface:** Integrated web GUI using Gradio for easy input and output[cite: 118].
* [cite_start]**Customizable Constraints:** Logic to handle maximum and minimum summary lengths (Max: 200 tokens, Min: 74 tokens)[cite: 345].

## 🛠️ Tech Stack
* **Language:** Python
* **Deep Learning Framework:** PyTorch
* **NLP Library:** Hugging Face Transformers
* **Dataset Library:** Hugging Face Datasets
* **Web Interface:** Gradio
* **Evaluation Metric:** ROUGE Score
* **Other Tools:** NumPy, Pandas, Accelerate

## 📂 Dataset
The project utilizes the **CNN/DailyMail (Version 3.0.0)** dataset.
* [cite_start]**Source:** Hugging Face Datasets[cite: 366].
* **Content:** A collection of news articles and their associated human-written summaries (highlights).
* [cite_start]**Preprocessing:** Data was truncated, lowercased, and tokenized to fit the T5 model architecture [cite: 367-371].

## ⚙️ Model Architecture & Training
* [cite_start]**Base Model:** `t5-base`[cite: 381].
* **Hyperparameters:**
    * Batch Size: 16
    * Epochs: 5
    * [cite_start]Max Sequence Length: 512 tokens [cite: 384-386].
* [cite_start]**Training Environment:** GPU-enabled environment for accelerated computation[cite: 388].

## 📊 Performance Results
[cite_start]The model was evaluated using **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)** scores to measure the overlap between generated summaries and reference summaries[cite: 399].

| Metric | Score |
| :--- | :--- |
| **ROUGE-1** | 0.533 |
| **ROUGE-2** | 0.356 |
| **ROUGE-L** | 0.453 |
[cite_start][cite: 536-537]

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/text-summarization-t5.git](https://github.com/your-username/text-summarization-t5.git)
cd text-summarization-t5
