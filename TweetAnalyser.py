from textblob import TextBlob
import tweepy

while True:
    text = str(input("Enter your opinion:\n"))
    analysis = TextBlob(text)
    polarity = (((analysis.sentiment.polarity)/2)+0.5)*100
    polarity = round(polarity,2)
    if polarity > 50:
        print("This is "+ str(polarity)+ " % positive, youre optimistic")

    elif polarity < 50:
        print("This is "+ str(polarity)+ " % positive, youre pessimistic")
    
    elif polarity == 50:
        print("This is a neutral opinion")
    
    print("\n")
