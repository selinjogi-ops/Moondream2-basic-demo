import torch
from PIL import Image
from transformers import AutoTokenizer, AutoModelForCausalLM
# -------------------------
# 1️⃣ Load Model + Tokenizer
# -------------------------
model_id = "vikhyatk/moondream2"
print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(model_id, revision="2024-08-26")
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    revision="2024-08-26",
    trust_remote_code=True
)
model.eval()
# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print("Model loaded successfully!\n")
# -------------------------
# 2️⃣ Load Image
# -------------------------
image_path = "sample.jpg"
try:
    image = Image.open(image_path).convert("RGB")
except Exception as e:
    print("Error loading image:", e)
    exit()
print("Encoding image...")
image_embeds = model.encode_image(image)
print("Image encoded successfully!\n")
# -------------------------
# 3️⃣ Ask Questions Loop
# -------------------------
print("You can now ask questions about the image.")
print("Type 'exit' to quit.\n")
while True:
    question = input("Your Question: ")
    if question.lower() == "exit":
        print("Exiting...")
        break
    with torch.no_grad():
        answer = model.answer_question(
            image_embeds,
            question,
            tokenizer
        )
    print("Model Answer:", answer)

    print("-" * 50)
