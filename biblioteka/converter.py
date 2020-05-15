class Converter:
    def remove_space(self,fraze):
        words = list(fraze)
        for i in range (len(words)):
            if words[i] == ' ' or words[i] == ',' or words[i] == '_' or words[i] == '-' or words[i] == '.':
                words[i] = ''
        return ''.join(words)

    def change_characters(self, fraze):
        words = list(fraze)
        for i in range (len(words)):
            if words[i] == 'ł':
                words[i] = 'l'
            elif words[i] == 'ć':
                words[i] = 'c'
            elif words[i] == 'ś':
                words[i] = 's'
            elif words[i] == 'ź' or words[i] == 'ż':
                words[i] = 'z'
            elif words[i] == 'ó':
                words[i] = 'o'
            elif words[i] == 'ń':
                words[i] = 'n'
            elif words[i] == 'ą':
                words[i] = 'a'
            elif words[i] == 'ę':
                words[i] = 'e'
            elif words[i] == 'Ł':
                words[i] = 'L'
            elif words[i] == 'Ć':
                words[i] = 'C'
            elif words[i] == 'Ś':
                words[i] = 'S'
            elif words[i] == 'Ź' or words[i] == 'Ż':
                words[i] = 'Z'
            elif words[i] == 'Ó':
                words[i] = 'O'
            elif words[i] == 'Ń':
                words[i] = 'N'
            elif words[i] == 'Ą':
                words[i] = 'A'
            elif words[i] == 'Ę':
                words[i] = 'E'

        return ''.join(words)
