fc = [
    {"front": "Wofür ist fine-tuning geeignet?",
     "back": "Beschreibt das 'Nachtrainieren' eines Basis Modells. Bei LLMs ist es geeignet, um den Sprachstil des Modells anzupassen"
    },
    {"front": "Wofür ist RAG (Retrieval Augmented Generation) geeignet?",
     "back": "RAG ist gut geeignet, wenn das LLM Zugang zu aktuellen oder sich ständig verändernden Daten benötigt"
    },
    {"front": "Wofür ist Sentiment Analysis gut geeignet?",
     "back" : "Es ist gut geeignet, wenn man herausfinden möchte, ob Texte positive oder negative Stimmungen ausdrücken, z.B. bei Kundenbewertungen."
     },
    {"front": "Was ist die Aufgabe eines (Language) Embedding Modells?",
     "back" : "Es wandelt Text in Vektoren um, sodass dieser von z.B. Chat-basierten LLMs verarbeitet werden kann"
     } 
    ]

_flashcards = {
    'fc_id': ['fc'],
    'fc' : fc
   
    # Add more flashcardlists to this dictionary as you create them
}

def load_flashcards(fc_id=str):
    """
    Access questions defined in this module.
    
    Parameters:
    -----------
    question_identifier : str or None
        The identifier of the question (e.g., 'q1', 'q2')
        If None, returns all questions as a dictionary
    
    Returns:
    --------
    A question dictionary or dictionary of all questions
    """
    if fc_id is None:
        return _flashcards
    
    if fc_id in _flashcards:
        return _flashcards[fc_id]
    else:
        raise ValueError(f"Flashcards '{fc_id}' not found")