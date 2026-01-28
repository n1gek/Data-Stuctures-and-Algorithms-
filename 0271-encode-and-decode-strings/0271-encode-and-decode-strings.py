class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        word = ""
        for char in strs:
            length = len(char)
            new = str(length) + "#" + char
            word += new

        return word
        #   5#Hello5#World

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        x = 0
        print(f'{s} this is the input')

        length = len(s)
        # "1#0"
        while x < length:

            count = ""
            while x < length and s[x].isdigit():
                count += s[x]
                print(f'{count}, count in while')
                x += 1
                
            x += 1
            stop = int(count) + x
            new_word = s[x: stop]
            res.append(new_word)
            x += int(count)

        return res        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))