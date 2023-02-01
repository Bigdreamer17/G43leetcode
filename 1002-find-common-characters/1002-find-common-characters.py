class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
            min_counter = collections.Counter(words[0])

            for word in words[1:]:
                word_counter = collections.Counter(word)
                min_counter = word_counter & min_counter

            return list(min_counter.elements())