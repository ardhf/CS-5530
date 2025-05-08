
# 🤖 Transformer-Based Chatbot (General Attempt)

This repository contains an experimental Transformer-based chatbot built using PyTorch. The initial goal was to train a general-purpose chatbot using open-domain dialog data, with plans to fine-tune it for a healthcare setting. This version focuses on the first attempt, which encountered several limitations.

---

## 📂 Project Structure

```bash
├── Ron_Chatbot_Transformer.ipynb    # Main notebook (model training and inference)
├── README.md                        # This file
├── data/
│   ├── checkpoints/                 # Saved model checkpoints
│   ├── config/                      # Model and tokenizer configurations
│   ├── dataset/                     # Loaded training data (e.g., .parquet files)
│   └── model_output/                # Trained model weights and vocab files
