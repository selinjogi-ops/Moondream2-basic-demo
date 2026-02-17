# Moondream2 Image Question Answering (Local VLM Demo)

A simple Image Question-Answering system built using Moondream-2, a lightweight Vision Language Model (VLM).

This project demonstrates how to:
*Load Moondream2 locally

*Encode an image

*Ask questions about the image

*Generate natural language answers

Runs on CPU or GPU.

# Features
*Local Vision-Language inference

*Interactive question loop

*GPU support (if available)

*Lightweight 1.8B parameter model

*No API required (fully local)

# Model Used
*Model: vikhyatk/moondream2

*Revision: 2024-08-26

*Parameters: ~1.8B

*Type: Vision-Language Model (VLM)

Moondream-2 can:
*Describe images

*Answer questions about images

*Read text from images (OCR-like capability)

# Project Structure
moondream2-image-qa/
│
├── basic_moondream.py
├── requirements.txt
└── README.md

# Installation
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/moondream2-image-qa.git
cd moondream2-image-qa

2️⃣ Install Dependencies
pip install -r requirements.txt
Or manually:
pip install torch transformers pillow

▶️ How to Run
Edit the image path inside main.py:

image_path = r"your_image_path_here.jpg"

Then run:
python basic_moondream.py

You will see:
You can now ask questions about the image.
Type 'exit' to quit.
Ask anything like:
1.What is in the image?

2.Describe the scene.

3.What color is the object?

4.Is there text in the image?

# How It Works
1.Load tokenizer and Moondream2 model

2.Move model to GPU (if available)

3.Load image using PIL

4.Encode image using encode_image()

5.Ask questions using answer_question()

Core functions used:
model.encode_image(image)
model.answer_question(image_embeds, question, tokenizer)

# Hardware Requirements
Recommended:
*8GB RAM

*NVIDIA GPU (for faster inference)

# Example Use Cases
*Image description

*Visual Q&A systems

*AI assistants

*Accessibility tools

*Real-time webcam integration (extendable)

# Future Improvements
*Add webcam support

*Add speech output

*Add multilingual responses

*Optimize for Jetson / Edge deployment

*Add GUI interface

# Author
Selin Jogi Chittilappilly

AI/ML | Computer Vision | Vision Language Models
