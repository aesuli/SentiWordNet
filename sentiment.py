import re
from nltk.corpus import stopwords

#remove stopwords
stop_words=set(stopwords.words('english'))
stop_words.remove('not')

def split_line(line):
    cols = line.split("\t")
    return cols

def get_words(cols):
    words_ids = cols[4].split(" ")
    words = [w.split("#")[0] for w in words_ids]
    return words

def get_positive(cols):
    return cols[2]

def get_negative(cols):
    return cols[3]

def get_objective(cols):
    return 1 - (float(cols[2]) + float(cols[3]))

def get_gloss(cols):
    return cols[5]

def get_scores(filepath, sentiword):

    f = open(filepath)
    totalobject =0.0
    count =0.0
    totalpositive =0.0
    totalnegative =0.0
    for line in f:
        if not line.startswith("#"):
            cols = split_line(line)
            words = get_words(cols)
           # print(words)
            
            for word in sentiword:

                if word in words:
                    if word == "not":
                        totalobject = totalobject + 0
                        totalpositive = totalpositive + 0
                        totalnegative = totalnegative + 16
                        count =count + 1
                    else:

                        #print("For given word {0} - {1}".format(word, get_gloss(cols)))
                        #print("P Score: {0}".format(get_positive(cols)))
                        #print("N Score: {0}".format(get_negative(cols)))
                        #print("O Score: {0}\n".format(get_objective(cols)))
                        totalobject = totalobject + get_objective(cols)
                        totalpositive = totalpositive + float(get_positive(cols))
                        totalnegative = totalnegative + float(get_negative(cols))
                        count =count + 1
    if count >0:
        if totalpositive > totalnegative :
            print("Positive word : 1")
            print("Positive value : ",totalpositive)
            print("Negative value : ",totalnegative)
        else :
            print("Negative : -1")
            print("Positive value : ",totalpositive)
            print("Negative value : ",totalnegative)

        print("average object Score : ",totalobject/count)

            

if __name__ == "__main__":
    comment = input("Enter Your feeling : ")
    sentiword = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", comment).split())
    stop_words = set(stopwords.words('english'))
    
    sentiword = sentiword.lower().split(" ")
    filtered_sentence = [w for w in sentiword  if not w in stop_words ]
    #print(filtered_sentence)
    get_scores("SentiWordNet_3.0.0.txt",filtered_sentence)