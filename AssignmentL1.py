#Question 1 :-


url = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', 'www.website.org', 'www.bis.org.in', 'www.rbi.org.in']

def topLevelDomain(domain: str):
    return domain.rsplit('.', 1)[-1]

print(sorted(url, key=topLevelDomain))

###########################################

# Question 2 :-


def match_words(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr= ctr+1
  return ctr

print(match_words(['x', 'cd', 'cnc', 'kk']))
print(match_words(['axa', 'xyz', 'gg', 'x', 'yyy']))
print(match_words(['bab', 'ce', 'cba', 'syanora']))

###########################################

# Question 3:-

a=['bbb', 'ccc', 'axx', 'xzz', 'xaa']
a1=['mix', 'xyz','apple', 'xanadu', 'aardvark','xz']
xlist=[]
def sort(s):
    for z in s[:]:
        if z.startswith('x'):
           xlist.append(z)
           s.remove(z)
    print(sorted(xlist)+sorted(s))
    del xlist[:]

sort(a)
sort(a1)

###########################################

# Question 4:-

A1= [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
output = sorted(A1, key=lambda x:x[-1])
print(output)

###########################################

# Question 5:-

a = [1, 2, 2, 3]
b = [2, 2, 3, 3, 3]
a = list(set(a))
b = list(set(b))
print(a)
print(b)


#########################################

# Question 6:-

def formated(bookstore) :
    print ( "Values inside the function: ")
    print(bookstore['New Arrivals']['WEB'])
    print(bookstore['New Arrivals']['COOKING'])
    
bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
formated(bookstore)
print ("\n\n"" Values outside the function: " "\n",bookstore)

#########################################

# Question 7:-

import itertools
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    final_dic = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
    fin_keys = list((final_dic.keys()))[-5:]
    for fin_key in fin_keys:
        print(fin_key, final_dic[fin_key])
    return final_dic

print( word_count("Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."))

#########################################

# Question 8:-

str1="Python is a widely used high-level programming langauage for general-purpose prograaming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to concpets in fewer lines of code than possible languages such as C++ or Java. The language provides constructs inteneded to enable writing clear programs on both a small scale and a large scale. Python featues a dynamic type system and sutomatic memory management and supports multiple programming paradgms,including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython , the reference implementation of Python, is opne source software and has a community-based development model, as do nearly all of its variant implementations. CPython os managed by the non-profit Python Software Foundation."

str2="Python is Python are Python was Python not Python yes Python no Python awesome Python abcd"


def getDic(strn):
	dic={}
	wordList=strn.split()
	length=len(wordList)
	for index,word in enumerate(wordList):
		if dic.has_key(word):
			continue
		tmpList=[]
		for i in range(index,length):
			if index==length-1:
				break
			if word==wordList[i]:
				nextWord=wordList[i+1]
				tmpList.append(nextWord)
		#print word,tmpList

		dic[word]=tmpList
	return dic

def guess(strn,word):
	wordDictionary=getDic(strn)
	print (word ,wordDictionary[word])
    
guess(str1,"Python")

#########################################

# Question 9:-

import re
 
 
str1="""Interface		IP-Address	OK? 	Method Status	Protocol
 
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down"""

print ("\n")
for line in str1.splitlines():
 
    matchObj = re.match( r'(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+\w+', line, re.M|re.I)
 
    if matchObj:
         print  (matchObj.group(1),",",matchObj.group(2),"\n")
    print ("\n")

#########################################

# Question 10:-