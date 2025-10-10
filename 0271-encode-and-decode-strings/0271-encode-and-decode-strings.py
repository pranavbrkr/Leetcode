class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        
        return enc
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        dec = []
        i = 0
        n = len(s)

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            dec.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return dec
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))