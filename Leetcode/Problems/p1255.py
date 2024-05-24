class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
    
        # Create a counter for the letters we have
        letter_count = Counter(letters)
        
        # Function to calculate the score of a word
        def get_word_score(word):
            word_score = 0
            for char in word:
                word_score += score[ord(char) - ord('a')]
            return word_score
        
        # Backtracking function to try all combinations of words
        def backtrack(index, current_score):
            nonlocal max_score
            if index == len(words):
                max_score = max(max_score, current_score)
                return
            
            # Try to use the word at the current index
            word = words[index]
            word_counter = Counter(word)
            can_use_word = True
            for char, cnt in word_counter.items():
                if letter_count[char] < cnt:
                    can_use_word = False
                    break
            
            if can_use_word:
                # Use the word
                for char, cnt in word_counter.items():
                    letter_count[char] -= cnt
                backtrack(index + 1, current_score + get_word_score(word))
                # Backtrack
                for char, cnt in word_counter.items():
                    letter_count[char] += cnt
            
            # Try not using the word
            backtrack(index + 1, current_score)
        
        max_score = 0
        backtrack(0, 0)
        return max_score
