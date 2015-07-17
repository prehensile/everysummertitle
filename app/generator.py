import nltk
import os
import random

class PerpetualAstonishment( object ):

    def __init__( self ):
        self._adjectives = None
        self._nouns = None
        self._firstnames = None
        self._surnames = None
        self.load_corpora()


    def load_corpora( self ):

        print "Loading corpora..."

        pth = os.path.realpath( os.path.dirname(__file__) )
        nltk.data.path.append( os.path.join( pth, "nltk_data" ) )
        from nltk.corpus import wordnet as wn

        self._adjectives = list(wn.all_synsets('a'))
        self._nouns = list(wn.all_synsets('n'))

        with open( os.path.join( pth, "firstnames.txt") ) as fh:
            self._firstnames = fh.readlines()

        with open( os.path.join( pth, "surnames.txt") ) as fh:
            self._surnames = fh.readlines()


    def sanitise( self, str_in ):
            return str_in.replace( "_", " " ).title()


    def generate( self ):

        n_synset = random.choice( self._nouns )
        noun = n_synset.lemmas()[0].name()

        a_synset = random.choice( self._adjectives )
        adj = a_synset.lemmas()[0].name()

        fn = random.choice(self._firstnames).rstrip()
        sn = random.choice(self._surnames).rstrip()

        return "The %s %s of %s %s" % (
            self.sanitise(adj),
            self.sanitise(noun),
            fn, sn
        )

if __name__ == '__main__':
    pa = PerpetualAstonishment()
    print pa.generate()