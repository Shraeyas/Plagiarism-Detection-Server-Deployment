import os
from gensim.models.doc2vec import Doc2Vec

def get_inference_vector (doc) :
    model = Doc2Vec.load (os.path.join ("models", "doc2vec_20news.bin"))
    return model.infer_vector (doc)