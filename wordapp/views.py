from django.shortcuts import render


def wordhome(request):
    return render(request,'wordhome.html')

def worddetail(request):
    return render(request,'worddetail.html')

def wordresult(request):
    text = request.GET['fulltext'] #전체 텍스트 받아오고 싶어요
    words = text.split() 
    # 총 단어수 갯수 받아온거야.
    word_dic = {}
    #안녕 : 1
    for word in words:
        if word in word_dic:
            #카운트를 하나 더해줘
            word_dic[word]+=1
        else:
            word_dic[word]=1
    return render(request,'wordresult.html', {'full': text, 'total': len(words), 'dictionary': word_dic.items}) 
