
import re

def extract_results(text):
    matches = re.findall(r'\d+\.\d+', text)
    return [float(x) for x in matches[-30:]]

def predict_result(text):
    data = extract_results(text)
    if len(data) < 10:
        return "Datos insuficientes"
    avg = sum(data[-10:]) / 10
    if avg > 1.5:
        return "Alta probabilidad de >1.5x"
    else:
        return "Baja probabilidad"
