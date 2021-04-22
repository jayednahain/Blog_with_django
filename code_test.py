from textblob import TextBlob as tx


speach = '''Our faces are lined with sad wrinkles now, cry  and weak  my hearing is half gone. She's stooped now, hunched and pinched, yet every time she smiles we go back unhappy  to being young, with those jewels in her eyes, and I fall in love all over again. We don't go out to the kids anymore. They come to us, and a young man helps her make the cookies when her hands shake, and a young woman helps me with the weeds when my knees give. I hear on the news every day about the new generation being lazy, and I shake my head every time. These kids are just growing the way all things grow. Messily.

'''
speach_2 = " i am unhappy. i am crying . i feel lonely . i want to be happy . smile like a happy person  "
bad_words = ["sex","fuck"]

blob_object = tx(speach)

'''for word in blob_object.words:
   if word in bad_words:
      print(word)
      
'''



speach_ob = tx(speach_2)


for sentence in speach_ob.sentences:
   if sentence.polarity < -0.6:
      print("sad: ",sentence)
      print(sentence.sentiment.polarity)
   elif sentence.polarity > 0.6:
      print(sentence.sentiment.polarity)
      print("happy: ",sentence)



