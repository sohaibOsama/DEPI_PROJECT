from transformers import AutoModelForSequenceClassification,AutoTokenizer
import torch


################
model_path = r'D:\django chatbot\fine-tuned-model'
mymodel = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# make a pipline
def classify(text:str):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    # Disable gradient calculation since we are doing inference
    with torch.no_grad():
        outputs = mymodel(**inputs)

    # Get the logits (model raw outputs)
    logits = outputs.logits

    # Convert logits to binary classification (0 or 1) using argmax
    predictions = torch.argmax(logits, dim=-1)

    # Convert to list format for easier reading
    binary_output = predictions.cpu().numpy().tolist()  # Here, Output will be a list like [1, 0, 1]

    # Map the binary predictions to 'Positive' or 'Negative'
    mapped_labels = ["Positive" if pred == 1 else "Negative" for pred in binary_output]

    print("Predictions:")
    return  mapped_labels

# print(classify("I am happy today"))

