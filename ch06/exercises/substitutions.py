import json

def main():
    news= "news.txt"
    json="subs.json"
    fptr= open(news, "r")
    fptr2=open(json, "r")

    accumulator=0
    for ch in fptr.read():
        if ch.isalnum():
            accumulator+=1
    fptr.close()

    fptr=open("news.text", "w")
    data=str(accumulator)+"characters"
    fptr.write()


# data= {
#     "num":0,
#     "msg":"Hello World",
# }

# json_string=json.dumps(data)
# print(json_string), type(json_string)

fptr= open("news.txt", "r")
json_data=json.load(fptr)
fptr2= open("subs.json", "r")
better=fptr.read()

for k, v in json_data.items():
    better=better.replace(k,v)
fptr= open("betternews.txt", "w")
fptr.write(better)

fptr.close()


