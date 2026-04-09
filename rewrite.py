from transformers import pipeline

paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

headline = "Nigeria inflation rises to 20%"
new_headline = paraphraser(headline, max_length=50, num_return_sequences=1)[0]['generated_text']

print("Original:", headline)
print("Rewritten:", new_headline)
