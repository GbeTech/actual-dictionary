import requests
from .Word import Word, Definition
from .html_utils import remove_from, get_next_tag, remove_tags_from_iter
from .dictionary_utils import get_from_next_ex, get_from_next_def


def get_word(word: Word = Word(), query=''):
	print(f'from_merriam_webster|{query}')
	html = requests.get(f'https://www.merriam-webster.com/dictionary/{query}')
	word.query = query
	# DEFINITIONS
	definitions = []

	try:
		definition = get_from_next_def(html.text, '<strong class="mw_t_bc">: </strong>')
		while True:
			temp, _, remain = definition.partition('<strong class="mw_t_bc">: </strong>')
			try:
				temp = temp[:temp.index('</span>')]
			except ValueError:
				pass
			temp = remove_tags_from_iter(temp).strip()
			definitions.append(temp)
			definition = get_from_next_def(remain, '<strong class="mw_t_bc">: </strong>')
	except ValueError:
		pass

	# EXAMPLES
	examples = []
	# Regular examples first
	try:
		example = get_from_next_ex(html.text, 'definition-inner-item">')
		while True:
			next_tag = get_next_tag(example)
			if next_tag == '<span>':  # hack
				raise ValueError
			temp, _, remain = example.partition('</p>')
			examples.append(remove_from(temp.strip(), '<em class="mw_t_it">', '</em>'))
			example = get_from_next_ex(remain, 'definition-inner-item">')
	except ValueError:
		pass

	if not examples:  # If regular examples were not found
		try:
			example = get_from_next_ex(html.text,
			                           'cite-example">')
			while True:
				example = remove_from(example, '<em>', '</em>')
				temp, _, remain = example.partition('</div>')
				examples.append(temp.strip())
				example = get_from_next_ex(example,
				                           'cite-example">')

				print()
		except ValueError:
			pass
	word.dictionaries['merriam-webster.com'] = Definition()
	word.add_definitions('merriam-webster.com', definitions)
	word.add_examples('merriam-webster.com', examples)

	return word
