import requests
from lib.Word import Word, Definition
from lib.html_utils import remove_tags_from, remove_from
from lib.dictionary_utils import get_from_next_ex, get_from_next_def


def get_word(word: Word = Word(), query=''):
	print(f'from_wordreference|{query}')
	html = requests.get(f'http://www.wordreference.com/definition/{query}')
	word.query = query

	definitions = []
	try:
		definition = get_from_next_def(html.text, "rh_def\'>")
		while True:
			if definition.index('</span>') < definition.index('<span'):
				temp, _, remain = definition.partition('</span>')
			else:
				temp, _, remain = definition.partition('<span')
			definitions.append(temp)
			definition = get_from_next_def(remain, "rh_def\'>")
	except ValueError:
		pass

	# EXAMPLES
	examples = []
	try:
		example = get_from_next_ex(html.text, "<span class='rh_ex'>")
		while True:
			temp, _, remain = example.partition('</span>')
			examples.append(temp.strip())
			example = get_from_next_ex(remain, "<span class='rh_ex'>")
	except ValueError:
		pass

	word.dictionaries['wordreference.com'] = Definition()
	word.add_definitions('wordreference.com', definitions)
	word.add_examples('wordreference.com', examples)

	return word
