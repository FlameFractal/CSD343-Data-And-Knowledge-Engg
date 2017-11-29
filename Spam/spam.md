# Spam Content - Report

**Group 26:**

- Samarjoy Pandit
- Saksham 
- Vishal
- Akanksha Jojwan
- Saurabh

### Source Code:

1. Count articles (a, an, the)

  ```python
  text = open('sample.txt').read()
  a_count = text.count('a') + text.count('A')
  an_count = text.count('an') + text.count('An')
  the_count = text.count('the') + text.count('The')
  print('Number of a:', a_count)
  print('Number of an:', an_count)
  print('Number of the:', the_count);
  ```

 **Screenshot:**

![](C:\Users\vishg\Desktop\aanthe.png)


2.  Average length of words

    ```python
    s = open('sample.txt').read()
    numlist = list(map(len, s.split()))
    sum = 0 
    for x in numlist: 
    	sum = sum + x 
    print('Average length of words in the file:',sum/len(numlist))
    ```


**Screenshot:**

![](C:\Users\vishg\Desktop\q2.png)



3. tri-grams

  ```python
  import nltk
  def get_words(string):
  	tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
  	return tokenizer.tokenize(string) 
  string = open('sample.txt').read() 
  words = get_words(string) 
  finder = nltk.collocations.TrigramCollocationFinder.from_words(words) 
  scored = finder.score_ngrams(nltk.collocations.TrigramAssocMeasures().raw_freq) 
  trigrams = finder.ngram_fd.items() 
  for x in trigrams: 
  	print(x+"\n") 
  ```


**Screenshots:**

![](C:\Users\vishg\Desktop\ngram.png)

![](C:\Users\vishg\Desktop\ngram2.png)
