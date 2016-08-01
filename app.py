from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

sentence = "Hello world!!!"
results = analyser.polarity_scores(sentence)
for k in sorted(results):
    print('{0}: {1}, '.format(k, results[k]), end='')
    print()
