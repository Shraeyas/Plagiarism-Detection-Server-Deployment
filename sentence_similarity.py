from scipy import spatial
from preprocess import pre_process
from inference import get_inference_vector
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def get_sentence_similarity (doc_0, doc_1) :
    sentences_0 = []
    sentences_0 = split_into_sentences(doc_0 + ".")
    sentences_0_processed = []
    sentences_0_processed.append (pre_process (sentences_0))
    vectors_0 = []
    for i, sentence in enumerate (sentences_0_processed[0]) :
        v = get_inference_vector (sentence)
        vectors_0.append (v)

    sentences_1 = []
    sentences_1 = split_into_sentences(doc_1 + ".")
    sentences_1_processed = []
    sentences_1_processed.append (pre_process (sentences_1))
    vectors_1 = []
    for i, sentence in enumerate (sentences_1_processed[0]) :
        v = get_inference_vector (sentence)
        vectors_1.append (v)

    values = { "doc_0": [], "doc_1": [] }

    similarities = []
    for i in range (len(vectors_0)):
        for j in range (len(vectors_1)):
            similarity = 1 - spatial.distance.cosine (vectors_0[i], vectors_1[j])
            similarities.append({ "similarity": similarity, "doc_0_idx": i, "doc_1_idx": j })
    similarities = sorted(similarities, key=lambda d: d['similarity'], reverse = True) 

    sentences_0_map = {}
    sentences_1_map = {}
    
    for similarity in similarities:
        if similarity["doc_0_idx"] not in sentences_0_map and similarity["doc_1_idx"] not in sentences_1_map:
            sentences_0_map[similarity["doc_0_idx"]] = similarity
            sentences_1_map[similarity["doc_1_idx"]] = similarity

    for i in range (len (vectors_0)):
        if i in sentences_0_map:
            value =  {
                "doc_0": {
                    "index": i,
                    "sentence": sentences_0[i]
                },
                "doc_1": {
                    "index": sentences_0_map[i]["doc_1_idx"],
                    "sentence": sentences_1[sentences_0_map[i]["doc_1_idx"]]
                },
                "similarity": sentences_0_map[i]["similarity"]
            }
        
        else:
            value =  {
                "doc_0": {
                    "index": i,
                    "sentence": sentences_0[i]
                },
                "doc_1": {
                    "index": -1,
                    "sentence": -1
                },
                "similarity": -1
            }
        values["doc_0"].append(value)

    for i in range(len(vectors_1)):
        index = i
        sentence = sentences_1[i]
        chk = False
        for value in values["doc_0"]:
            if value["doc_1"]["index"] == index and value["doc_1"]["sentence"] == sentence:
                chk = True
                values["doc_1"].append({
                    "doc_0": {
                        "index": value["doc_0"]["index"],
                        "sentence": value["doc_0"]["sentence"]
                    },
                    "doc_1": {
                        "index": index,
                        "sentence": sentence
                    },
                    "similarity": value["similarity"]
                })
                break
            
        if chk is False:
            values["doc_1"].append({
                "doc_0": {
                    "index": -1,
                    "sentence": ""
                },
                "doc_1": {
                    "index": index,
                    "sentence": sentence
                },
                "similarity": -1
            })

    # for i in range (len (vectors_1)):
    #     similarities = {}
    #     maxSimilarity = -1
    #     for j in range (len (vectors_0)):
    #         result = 1 - spatial.distance.cosine (vectors_1[i], vectors_0[j])
    #         if result > maxSimilarity:
    #             maxSimilarity = result
    #             similarities = {
    #                 "index": j,
    #                 "sentence": sentences_0[j],
    #                 "similarity": result
    #             }

    #     value =  {
    #         "doc_1": {
    #             "index": i,
    #             "sentence": sentences_1[i]
    #         },
    #         "doc_0": {
    #             "index": similarities["index"],
    #             "sentence": similarities["sentence"]
    #         },
    #         "similarity": similarities["similarity"]
    #     }
    #     values["doc_1"].append(value)


    return values
