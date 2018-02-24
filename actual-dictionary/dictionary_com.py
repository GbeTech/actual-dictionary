import requests
from lib.Word import Word, Definition
from lib.html_utils import remove_from, remove_tags_from
from lib.dictionary_utils import get_from_next_ex, get_from_next_def


def get_word(word: Word = Word(), query=''):
	print(f'from_dictionary_com_alt|{query}')
	html = requests.get(f'http://www.dictionary.com/browse/{query}')
	word.query = query

	# DEFINITIONS
	definitions = []
	try:
		definition = get_from_next_def(html.text, 'def-content">')
		while True:
			temp, _, remain = definition.partition('</div>')
			definitions.append(remove_tags_from(temp.strip()))
			definition = get_from_next_def(remain, 'def-content">')
	except ValueError:
		pass

	examples = []
	try:
		example = get_from_next_ex(html.text, 'partner-example-text">')

		while True:
			temp, _, remain = example.partition('</p>')

			examples.append(remove_from(temp.strip(), '<em>', '</em>'))
			example = get_from_next_ex(remain, 'partner-example-text">')
	except ValueError:
		pass

	word.dictionaries['dictionary.com'] = Definition()
	word.add_definitions('dictionary.com', definitions)
	word.add_examples('dictionary.com', examples)
	# for definition in definitions:
	# 	# for definition in soup.find_all('div', attrs={'class': 'def-content'}):
	# 	# 	definition_text = bs.get_text(definition).strip()
	# 	word._add_definition('dictionary.com', definition)
	# for example in examples:
	# 	word._add_example('dictionary.com', example)
	# examples = set()
	# for i, l in enumerate(html_lines):
	# 	if 'partner-example-text' in l:
	# 		cleaned = html_lines[i + 1]
	# 		cleaned = remove_from(cleaned, '<em>', '</em>', '<p>', '</p>')
	# 		cleaned = cleaned.strip()
	# 		word._add_example('dictionary.com', cleaned)
	# examples.add(cleaned)
	# examples_idxs = set(html_lines.index(l) + 1 for l in html_lines if 'partner-example-text' in l)
	# examples = [html_lines[line].replace('</div>', '').strip() for line in examples_idxs]
	# print(examples)
	# 	examples = soup.find_all('p', attrs={'class': 'partner-example-text'})
	# 	for ex in examples:
	# 		word._add_example('dictionary.com', bs.get_text(ex).strip())
	return word
