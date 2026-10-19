from transformers import AutoTokenizer, AutoModelForSequenceClassification


MODEL_NAME = "khanfs/ChemSolubilityBERTa"


print("Завантаження моделі...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME
)

print("Модель завантажена!")


def predict_solubility(smiles):
    inputs = tokenizer(
        smiles,
        return_tensors="pt"
    )

    outputs = model(**inputs)

    solubility = outputs.logits.item()

    return solubility