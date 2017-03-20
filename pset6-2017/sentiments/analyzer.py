import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set()
        self.negatives = set()
        
        with open(positives, "r") as positive:
            for line in positive:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue
                self.positives.add(line)
            #self.positives = set([line for line in positive if line.strip() and not line.startswith(';')]) - convoluted way
                
        with open(negatives, "r") as negative:
            for line in negative:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue
                self.negatives.add(line)

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0
        for token in tokens:
            if token.lower() in self.positives:
                score += 1
            elif token.lower() in self.negatives:
                score += -1
        return score
        
