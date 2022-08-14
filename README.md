# Plagiarism-Detection-Server-Deployment

---

### This is the Production code of the Plagiarism detector that is deployed on Heroku at :

```
https://plism.herokuapp.com/api/document_similarity
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
        curl --location --request POST 'https://plism.herokuapp.com/api/document_similarity' \
        --form 'doc_0="hi! how are you?"' \
        --form 'doc_1="hello! how do you do?"'
    ```

*  **Response:**  

      ```  
      {
          "doc_similarity": The cosine similarity between the two documents,
          "sen_similarity": [
              [
                  The cosine similarity between first pair of sentences,
                  [
                      start index of the sentence in the first document,
                      end index of the sentence in the first document
                  ],
                  [
                      start index of the sentence in the second document,
                      end index of the sentence in the second document
                  ]
              ],
              [
                  The cosine similarity between second pair of sentences,
                  [
                      start index of the sentence in the first document,
                      end index of the sentence in the first document
                  ],
                  [
                      start index of the sentence in the second document,
                      end index of the sentence in the second document
                  ]
              ]
          ]
      }
      ```
