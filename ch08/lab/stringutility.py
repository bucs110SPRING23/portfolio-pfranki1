class StringUtility:
    def _init_(self,string):
        self.string=string
    def _str_(self):
        return self.string
    def vowels(self):
        count=sum(1 for c in self.string if c.lower() in "aeiou")
        if count>5:
            return "many"
        else:
            return str(count)
    def bothEnds(self):
        if len(self.string)<=2:
            return""
        else:
            return self.string[-2:]+self.string[:2]
    def fixStart(self):
        if len(self.string)<=1:
            return self.string
        else:
            return self.string[0]+self.string[1:].replace(self.string[0], "*")
    def asciiSum(self):
        return sum(ord(c) for c in self.string)
    def cipher(self):
        result=""
        for c in self.string:
            if c.isalpha():
                shift=len(self.string)
                if c.isupper():
                    base=ord("A")
                else:
                    base=ord("a")
                result+=chr((ord(c)-base+shift)%26+base)
            else:
                result+=c
        return result    
