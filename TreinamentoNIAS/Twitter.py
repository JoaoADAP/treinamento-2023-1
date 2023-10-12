tweets = ["Wow, what a great day today!! #sunshine",
"I feel sad about the things going on around us. #covid19",
"I'm really excited to learn Python with @JovianML #zerotopandas",
"This is a really nice song. #linkinpark",
"The python programming language is useful for data science",
"Why do bad things happen to me?",
"Apple announces the release of the new iPhone 12. Fans are excited.",
"Spent my day with family!! #happy",
"Check out my blog post on common string operations in Python. #zerotopandas",
"Freecodecamp has great coding tutorials. #skillup"]

#Pegando a quantidade de tweets da lista
a = len(tweets)
print( "Existem {} tweets nessa lista\n". format(a))

happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

b = tweets[0].split()
i = 0
happy = False #Inicialmente, todas as frases são tristes

#Para cada palavra do primeiro tweet
for i in range(len(b)):
    if b[i] in happy_words:
        happy = True

if happy:
    print("O tweet é feliz\n")
else:
    print("O tweet é triste\n")

#--------------------------------------------------------------------------------------------------------------#

#Quantidade de tweets triste e feliz

i = 0
a = 0
c = 0
happy = False
Sad = False
for i in range(len(tweets)):                          #Numero de tweets na lista
    ii = 0
    for ii in range(len(tweets[i].split())):          #Numero de palavras em cada tweet da lista
        if tweets[i].split()[ii] in happy_words:      #Analisando cada palavra de cada tweet da lista
            happy = True
            a = a + 1                                 #Caso seja feliz, acrescenta mais um
            
        elif tweets[i].split()[ii] in sad_words:
            Sad = True
            c += 1                                    #Caso seja triste, acrescenta mais um
            
print("existem {} tweets felizes". format(a))
print("existem {} tweets triste". format(c))
d = len(tweets) - (a + c)
print("existe {} tweets neutros". format(d))

#O código pode ser melhorado usando "re.split(r'\W+', frase)", Tiramos todos os "!", ",", "#" dos tweets da lsta