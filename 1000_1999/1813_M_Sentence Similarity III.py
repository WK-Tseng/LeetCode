class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        split1, split2 = sentence1.split(' '), sentence2.split(' ')
        
        if len(split1) > len(split2):
            split1, split2 = split2, split1

        while len(split1) > 0 and len(split2) > 0 and split1[0] == split2[0]:
            split1.pop(0)
            split2.pop(0)

        while len(split1) > 0 and len(split2) > 0 and  split1[-1] == split2[-1]:
            split1.pop(-1)
            split2.pop(-1)
        
        # print(split1, split2)
        return len(split1) == 0
