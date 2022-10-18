import matplotlib.pyplot as plt
import numpy as np
def text():

    path = "./asas.txt"
    with open(path, encoding="utf8") as tf:
        text = tf.read()
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    text1 = ""
    for char in text:
        if char in chars:
            text1 += char
    return text1

def number_of_words(text_ascii):
    number=0
    number = len(text_ascii)
    Len=len(text_ascii)
    return number

def link_words_and_numbers(text_ascii):
        L=[]
        for i in range(len(text_ascii)):
            Sum=len(text_ascii[i])
            L.append(Sum)

def evaluate(text_ascii):
    L=[]
    for i in range(len(text_ascii)):
        Sum=len(text_ascii[i])
        L.append(Sum)
    del_list=[]
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i]+L[j]==20:
                if i in del_list or j in del_list:
                    pass
                else:
                    del_list.append(i)
                    del_list.append(j)
    del_list.sort(reverse=True)
    for i in del_list:
        try:del L[i]
        except:pass
    max1=max(L)
    a=[]
    b=[]
    for i in range(max1+1):
        if i>0:
            number = L.count(i)
            print(number,"words with",i,"letters")
            a.append(number)
            b.append(i)

def main():

    final_text = text()
    text_ascii = final_text.split(sep=" ")
    number_words = number_of_words(text_ascii)
    words_and_numbers=link_words_and_numbers(text_ascii)
    evaluation=evaluate(text_ascii)
    print("There are",number_words,"words")


main()
