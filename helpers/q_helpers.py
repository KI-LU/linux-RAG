q1 = {}

q1['question'] = 'Was könnten wir also tun, damit der Onkel eine gute Antwort gibt? Nicht nur zu diesen, sondern auch zu weiteren Themen.'
q1['type'] = 'multiple_choice'
q1['answers'] = [
    {
        'answer' : 'Wir könnten den Onkel dauerhaft in die Schule schicken, sodass er immer mit dem neuesten Wissen lernt.',
        'correct' : False,
        'feedback' : 'Das wäre sehr aufwendig und ineffektiv.'
        },
    {
        'answer' : 'Wir könnten dem Onkel beibringen die Bibliothek zu benutzen und immer nur zu Antworten, wenn er dort Information zu unserer Frage findet.',
        'correct' : True
    }
    ]


q2 = {}

q2['question'] = 'Der erste Test hat ergeben, dass die Performance von Phi3 nicht gut genug ist. Mit welcher Technik solltest du versuchen die Performance zu verbessern?'
q2['type'] = 'multiple_choice'
q2['answers'] = [
        {
        'answer' : 'Das LLM sollte auf alten Wartungsdaten und Handbüchern gefinetuned werden',
        'correct' : False,
        'feedback' : 'Das würde nur für einen Kurzen Zeitraum funktionieren. Sobald sich etwas in der Produktionslinie ändert müsste wieder neu trainiert werden. Das wäre teuer und aufwändig.'
            },
    {
        'answer' : 'Das LLM sollte über RAG Zugriff auf Wartungsdaten und Handbücher bekommen.',
        'correct' : True
    }
    ]

q3 = {}

q3['question'] = 'Welches Statement ist richtig?'
q3['type'] = 'multiple_choice'
q3['answers'] = [
        {
        'answer' : 'Neuronale Netze können mit numerischen Daten und Strings (Textdaten) arbeiten',
        'correct' : False,
        'feedback' : 'Strings können nicht direkt von Neuronalen netzen verwendet werden. Sie müssen erst in numerische Daten umgewandelt werden.'
            },
    {
        'answer' : 'Neuronale Netze können nur numerischen Daten verarbeiten.',
        'correct' : True
    }
    ]

q4 = {}

q4['question'] = 'Beim Befüllen der Wissensdatenbank muss man darauf achten, dass...'
q4['type'] = 'many_choice'
q4['answers'] = [
        {
        'answer' : '...auf allen Dokumenten das Firmenlogo zu sehen ist.',
        'correct' : False,
        'feedback' : 'Wie die Dokumente Aussehen ist nicht so relevant. Kunden bekommen diese Dokumente garnihct zu sehen.'
            },
    {
        'answer' : '...in allen dokumenten der Text durchsuchbar ist.',
        'correct' : True
    },
    {
        'answer' : '...alle Dokumente möglichst aktuell sind.',
        'correct' : True
    },
    {
        'answer' : '...alle Dokumente im richtigen Ordner gespreichert sind.',
        'correct' : True
    },
    {
        'answer' : '...alle Dokumente in der richtigen Sprache sind.',
        'correct' : True
    },
    {
        'answer' : '...alle wichtigen Informationen enthalten sind.',
        'correct' : True
    }
    ]

q5 = {}

q5['question'] = 'In welchen Dateiformaten können Computer generell den enthaltenen Text durchsuchen?'
q5['type'] = 'multiple_choice'
q5['answers'] = [
        {
        'answer' : 'Bilddateien wie .png oder .jpg',
        'correct' : False,
        'feedback' : 'Menschen können natürlich auch Text lesen der auf .png oder .jpg Dateien abgebildet ist. Computer benötigen dafür allerdings extra Programme.'
            },
    {
        'answer' : 'Textdateien wie .txt oder .docx',
        'correct' : True
    },
    {
        'answer' : 'Dokumente mit der Endung .pdf',
        'correct' :  False,
        'feedback' : 'Vorsicht, nicht alle PDFs sind durchsuchbar! Oft gibt es allerdings die Möglichkeit diese durch Converter durchsuchbar zu machen.'
    },
]

#dictionary for all questions
_questions = {
    'q_id': ['q1', 'q2', 'q3', 'q4', 'q5'],
    'q1' : q1,
    'q2' : q2,
    'q3' : q3,
    'q4' : q4,
    'q5' : q5
    # Add more questions to this dictionary as you create them
    }



def load_question(q_id=str):
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
    if q_id is None:
        return _questions
    
    if q_id in _questions:
        return _questions[q_id]
    else:
        raise ValueError(f"Question '{q_id}' not found")