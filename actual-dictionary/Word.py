class Word:
	def __init__(self, query=''):
		self.query = query
		self.sender = ''
		self.dictionaries = {}

	def _add_definition(self, website, definition):
		if website in self.dictionaries:
			self.dictionaries[website].definitions.append(definition)
		else:
			self.dictionaries[website].definitions = [definition]

	def _add_example(self, website, example):
		if website in self.dictionaries:
			self.dictionaries[website].examples.append(example)
		else:
			self.dictionaries[website].examples = [example]

	def add_definitions(self, website, definitions):
		for definition in definitions:
			self._add_definition(website, definition)

	def add_examples(self, website, examples):
		for example in examples:
			self._add_example(website, example)


class Definition:
	def __init__(self):
		self.definitions = []
		self.examples = []
