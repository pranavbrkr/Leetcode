class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        def deVowel(s):
            return ''.join('*' if c in 'aeiou' else c for c in s)

        for w in wordlist:
            lower = w.lower()
            devowel = deVowel(lower)
            if lower not in case_map:
                case_map[lower] = w
            if devowel not in vowel_map:
                vowel_map[devowel] = w
        
        answer = []

        for q in queries:
            if q in exact:
                answer.append(q)
            else:
                lower = q.lower()
                devowel = deVowel(lower)
                if lower in case_map:
                    answer.append(case_map[lower])
                elif devowel in vowel_map:
                    answer.append(vowel_map[devowel])
                else:
                    answer.append("")
        
        return answer