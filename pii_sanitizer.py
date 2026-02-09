import re

def sanitize(text):
    text = re.sub(r'\b\d{10}\b', '[PHONE]', text)
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    text = re.sub(r'Patient Name:\s.*', 'Patient Name: [REDACTED]', text)
    text = re.sub(r'ID:\s.*', 'ID: [REDACTED]', text)
    return text
