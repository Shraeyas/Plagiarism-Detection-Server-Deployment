from scipy import spatial
from preprocess import pre_process
from inference import get_inference_vector
import re
import nltk.data
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def get_document_similarity (doc_0, doc_1) :
    sentences_0 = tokenizer.tokenize(doc_0)
    document_0_processed = pre_process (sentences_0)
    flat_document_0 = [item for sublist in document_0_processed for item in sublist]
    vector_0 = get_inference_vector (flat_document_0)

    sentences_1 = tokenizer.tokenize(doc_1)
    document_1_processed = pre_process (sentences_1)
    flat_document_1 = [item for sublist in document_1_processed for item in sublist]
    vector_1 = get_inference_vector (flat_document_1)

    return (1 - spatial.distance.cosine (vector_0, vector_1))
