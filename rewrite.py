from transformers import pipeline

# Load the paraphrasing model
paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

# Headlines to rewrite
headlines = [
    "Nigeria inflation rises to 20%",
    "Lagos launches new transport system"
]

# Rewrite each headline
for headline in headlines:
    new_headline = paraphraser(headline, max_length=50, num_return_sequences=1)[0]['generated_text']
    print("Original:", headline)
    print("Rewritten:", new_headline)
    print("-" * 40)

