import textract

def extract_text_from_file(file_path):
    text = textract.process(file_path).decode("utf-8")
    return text
