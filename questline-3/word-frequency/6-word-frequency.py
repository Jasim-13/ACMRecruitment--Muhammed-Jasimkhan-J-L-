def word(text):
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
if  __name__ =="__main__":
    para="python is a language and python is simple"

    freq= word(para)

    for word,count in freq.items():
        print(word,"=>",count)
    
