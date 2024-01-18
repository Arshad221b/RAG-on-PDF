import re

class TextFilter:
    def __init__(self, file_path):
        self.file_path = file_path


    def filter_lines(self, texttoclean):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        filtered_lines = [line.strip() for line in lines if not line.startswith(texttoclean)]

        with open(self.file_path, 'w') as file:
            file.write('\n'.join(filtered_lines))


    def remove_lines_with_keyword(self, texttoclean):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        filtered_lines = []
        skip_next_line = False

        for line in lines:
            if line.startswith(texttoclean):
                skip_next_line = True
            elif skip_next_line:
                skip_next_line = False
            else:
                filtered_lines.append(line.strip())

        with open(self.file_path, 'w') as file:
            file.write('\n'.join(filtered_lines))

    def remove_square_brackets(self):
        with open(self.file_path, 'r') as file:
            lines = file.read()

        pattern = r'\[.*?\]'
        result = re.sub(pattern, '', lines, flags=re.DOTALL)

        with open(self.file_path, 'w') as file:
            file.write(result)


    def clean_text_prep(self):
        with open(self.file_path, 'r') as file:
            lines = file.read()

        pattern_roman = r'\b(?:I{1,3}|IV|V|IX|X{1,3}|XL|L|XC|C{1,3}|CD|D|CM|M)\.\b'
        pattern_digit = r'\d+'
        pattern_multispace = r'\s+'
        pattern_smallwords = r'\b(?!an|a)\w{1}\b'

        lines = re.sub(pattern_roman, '', lines)
        lines = re.sub(pattern_digit, '', lines)
        lines = re.sub(pattern_multispace, ' ', lines)
        lines = re.sub(pattern_smallwords, '', lines)

        with open(self.file_path, 'w') as file:
            file.write(lines)


    def clean_text(self):
        self.filter_lines('Marcus Aurelius')
        self.filter_lines('Page')
        self.remove_lines_with_keyword('MEDITATIONS OF MARCUS AURELIUS')
        self.remove_square_brackets()
        self.clean_text_prep()


if __name__ == "__main__":
    filter_instance = TextFilter('/Users/arshad_221b/Documents/Documents - Arshad’s MacBook Pro - 1/Projects/Lanchain Pinecone/meditations copy 2.text')
    filter_instance.clean_text()

