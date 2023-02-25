# Plagiarism-Detection-Server-Deployment

---

### This is the Production code of the Plagiarism detector that is deployed on Render at :

```
https://plagiarism.onrender.com/api/document_similarity
```

### The Original Plagiarism Detection Notebook is present at :

**[Shraeyas/Plagiarism-Detection](https://github.com/Shraeyas/Plagiarism-Detection)**

## About

```
The server has been deployed using Flask which fetches requests using POST method and return the following data :
1. The cosine similarity between the two documents.
2. The cosine similarity between all pairs of sentences and the start and end indices of those sentences in the original document.
```

## Deploy to your Machine

* **Requirements**
```
1. Python
2. Pip
```

* **Install the prerequisites using pip**
```
pip install -r requirements.txt
```
* **Run the server**
```
python deploy.py
```

## API

*  **Curl:**  
    ```
        curl --location 'http://127.0.0.1:5000/api/document_similarity' \
        --form 'doc_0="Object oriented programming is a  style of programming that supports encapsulation, inheritance, and polymorphism. Inheritance means derived  a new class from the base class.  "' \
        --form 'doc_1="The idea of inheritance in OOP refers to the formation of new classes with the already existing classes. The concept of inheritance was basically formulated for Simula in 1967.
        "'
    ```

*  **Response:**  
```
{
    "doc_similarity": 0.6415585875511169,
    "sen_similarity": {
        "doc_0": [
            {
                "doc_0": {
                    "index": 0,
                    "sentence": "Object oriented programming is a  style of programming that supports encapsulation, inheritance, and polymorphism."
                },
                "doc_1": {
                    "index": 1,
                    "sentence": "The concept of inheritance was basically formulated for Simula in 1967."
                },
                "similarity": 0.5923653244972229
            },
            {
                "doc_0": {
                    "index": 1,
                    "sentence": "Inheritance means derived  a new class from the base class."
                },
                "doc_1": {
                    "index": 0,
                    "sentence": "The idea of inheritance in OOP refers to the formation of new classes with the already existing classes."
                },
                "similarity": 0.628696858882904
            }
        ],
        "doc_1": [
            {
                "doc_0": {
                    "index": 1,
                    "sentence": "Inheritance means derived  a new class from the base class."
                },
                "doc_1": {
                    "index": 0,
                    "sentence": "The idea of inheritance in OOP refers to the formation of new classes with the already existing classes."
                },
                "similarity": 0.628696858882904
            },
            {
                "doc_0": {
                    "index": 0,
                    "sentence": "Object oriented programming is a  style of programming that supports encapsulation, inheritance, and polymorphism."
                },
                "doc_1": {
                    "index": 1,
                    "sentence": "The concept of inheritance was basically formulated for Simula in 1967."
                },
                "similarity": 0.5923653244972229
            }
        ]
    }
}
```
      
