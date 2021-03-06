import re
from scipy import spatial
from preprocess import pre_process
from inference import get_inference_vector
import re
import string

def get_sentence_similarity (doc_0, doc_1) :
    sentences_0 = []
    sentences_0 = doc_0.split (".")
    sentences_0_processed = []
    sentences_0_processed.append (pre_process (sentences_0))
    vectors_0 = []
    for i, sentence in enumerate (sentences_0_processed[0]) :
        v = get_inference_vector (sentence)
        start = doc_0.find (sentences_0[i])
        end = start + len(sentences_0[i]) + 1
        vectors_0.append ([v, start, end])

    sentences_1 = []
    sentences_1 = doc_1.split (".")
    sentences_1_processed = []
    sentences_1_processed.append (pre_process (sentences_1))
    vectors_1 = []
    for i, sentence in enumerate (sentences_1_processed[0]) :
        v = get_inference_vector (sentence)
        start = doc_1.find (sentences_1[i])
        end = end = start + len(sentences_1[i]) + 1
        vectors_1.append ([v, start, end])

    values = []
    for i in range (len (vectors_0)) :
        for j in range (len (vectors_1)) :
            result = 1 - spatial.distance.cosine (vectors_0[i][0], vectors_1[j][0])
            values.append ([result, [vectors_0[i][1], vectors_0[i][2]], [vectors_1[j][1], vectors_1[j][2]]])

    return values
