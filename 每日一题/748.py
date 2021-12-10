from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        counter_plate = Counter(licensePlate.lower())
        words = sorted(words, key=len)
        for word in words:
            counter_word = Counter(word)
            if True not in list(map(str.isalpha, list((counter_plate-counter_word).keys()))):
                return word

s = Solution()
s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"])