from pypdf import PdfReader
import spacy
import re

def is_mobile(txt):
    pattern = r'(?:\(\+91-\)|\(\+91\))?\d{10}'
    # pattern = r'(?:\+91)?\d{10}'

    matches = re.findall(pattern,txt)
    return matches

def is_email(txt):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    matches = re.findall(pattern, txt)

    return matches

def extract_data(pdf):
    reader = PdfReader(pdf)
    page = reader.pages[0]  
    text = page.extract_text()
    print(text, '\n\n', type(text))
    return text

def extract_entities(text):
    nlp = spacy.load("en_core_web_trf")
    name = []
    mob = None
    email = []
    address = []

    doc = nlp(text)

    for ent in doc.ents:
        
        if ent.label_ == "PERSON" and not name:
            name.append(ent.text.strip())
        
        if ent.label_ == "GPE" and not address:
            address.append(ent.text.strip())
        
    mob = is_mobile(text)
    email = is_email(text)

    name_result = name[0] if name else None
    address_result = ''.join(address) if address else None
    mob_result = mob[0] if mob else None
    email_result = ''.join(email) if email else None
    
    return name_result, address_result, mob_result, email_result


