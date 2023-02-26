# Plagiarism-Detection-Server-Deployment

---
![](https://github.com/Shraeyas/Plagiarism-Detection-Server-Deployment/raw/main/images/Preview.png)

### This is the Production code of the Plagiarism detector that is deployed on Render at :

```
https://plagiarism.onrender.com/
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
        curl --location 'https://plagiarism.onrender.com/api/document_similarity' \
        --form 'doc_0="This is a test document. This can highlight the text and can also show the percentage of similarity between the inputs. You can also hover over the text to view the similarity values."' \
        --form 'doc_1="This document is for testing. You can check the highlighted text for plagiarism and also hover over it for more details. You can also hover over the text for more details."'
    ```

*  **Response:**  
```
{
    "doc_similarity": 0.6435717344284058,
    "sen_similarity": {
        "doc_0": [
            {
                "doc_0": {
                    "index": 0,
                    "sentence": "This is a test document."
                },
                "doc_1": {
                    "index": 0,
                    "sentence": "This document is for testing."
                },
                "similarity": 0.9703976511955261
            },
            {
                "doc_0": {
                    "index": 1,
                    "sentence": "This can highlight the text and can also show the percentage of similarity between the inputs."
                },
                "doc_1": {
                    "index": 1,
                    "sentence": "You can check the highlighted text for plagiarism and also hover over it for more details."
                },
                "similarity": 0.4555428624153137
            },
            {
                "doc_0": {
                    "index": 2,
                    "sentence": "You can also hover over the text to view the similarity values."
                },
                "doc_1": {
                    "index": 2,
                    "sentence": "You can also hover over the text for more details."
                },
                "similarity": 0.7167359590530396
            }
        ],
        "doc_1": [
            {
                "doc_0": {
                    "index": 0,
                    "sentence": "This is a test document."
                },
                "doc_1": {
                    "index": 0,
                    "sentence": "This document is for testing."
                },
                "similarity": 0.9703976511955261
            },
            {
                "doc_0": {
                    "index": 1,
                    "sentence": "This can highlight the text and can also show the percentage of similarity between the inputs."
                },
                "doc_1": {
                    "index": 1,
                    "sentence": "You can check the highlighted text for plagiarism and also hover over it for more details."
                },
                "similarity": 0.4555428624153137
            },
            {
                "doc_0": {
                    "index": 2,
                    "sentence": "You can also hover over the text to view the similarity values."
                },
                "doc_1": {
                    "index": 2,
                    "sentence": "You can also hover over the text for more details."
                },
                "similarity": 0.7167359590530396
            }
        ]
    }
}
```
      
