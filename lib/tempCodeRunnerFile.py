# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
        print(word)
        
    def match(self,anagrams):
        anagram_list = []
        for anagram in anagrams:
            if sorted(anagram.lower())==sorted(self.word.lower()) and anagram.lower() != self.word.lower():
               anagram_list.append(anagram)
               print(anagram)
        print(anagram_list)
        return anagram_list

power = Anagram('power')
power.match(['rower','sjjshsgfs','werop','perow','abgsd','WerOp'])    
