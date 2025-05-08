
# 🤖 Transformer-Based Chatbot (General Attempt)

This repository contains an experimental Transformer-based chatbot built using PyTorch. The initial goal was to train a general-purpose chatbot using open-domain dialog data, with plans to fine-tune it for a healthcare setting. This version focuses on the first attempt, which encountered several limitations.

---


## 📂 Project Structure

> ⚠️ **Note:** The `data/` folder is too large to upload to GitHub. You can access the full dataset, model checkpoints, and configuration files here:  
> [Google Drive - Chatbot Data Folder](https://drive.google.com/drive/folders/1olztEcsPyQgerN_ql81RrHytXKI5kKbA?usp=sharing)

```bash
├── Ron_Chatbot_Transformer.ipynb    # Main notebook (model training and inference)
├── README.md                        # This file
├── data/                            # Directory for data (not uploaded due to size)
│   ├── checkpoints/                 # Saved model checkpoints
│   ├── config/                      # Model and tokenizer configurations
│   ├── dataset/                     # Loaded training data (e.g., .parquet files)
│   └── model_output/                # Trained model weights and vocab files
