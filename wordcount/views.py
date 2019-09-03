from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

#def elis(request):
    #return HttpResponse('<h1> Elis hair braing is great</h1>')
def count(request):
    fulltext= request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

            sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedword': sortedword})

def About(request):
    return render(request, 'About.html')
