## https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

##############################################################################

# def solution(s):
    
#     s = s.replace("zero", '0')
#     s = s.replace("one", '1')
#     s = s.replace("two", '2')
#     s = s.replace("three", '3')
#     s = s.replace("four", '4')
#     s = s.replace("five", '5')
#     s = s.replace("six", '6')
#     s = s.replace("seven", '7')
#     s = s.replace("eight", '8')
#     s = s.replace("nine", '9')

#     answer = int(s)

#     return answer


##############################################################################

def solution(s):
    word_dic = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',   
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }

    answer = ""
    temp = ""

    for c in s:
        if(c.isnumeric()):
            answer += c
            continue
        
        temp += c
        if temp in word_dic.keys():
            answer += word_dic[temp]
            temp = ""
    
    return int(answer)


word_dic = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',   
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

print(type(word_dic.keys()))
