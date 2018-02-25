# from PyDictionary import PyDictionary
# from get_from_dictionaries import from_wordreference
import csv
from .Word import Word
from . import dictionary_com as dc
from . import merriam_webster as mw
from . import wordreference as wr

from .html_utils import remove_from

heb_ab = [
	'א',
	'ב',
	'ג',
	'ד',
	'ה',
	'ו',
	'ז',
	'ח',
	'ט',
	'י',
	'כ',
	'ל',
	'מ',
	'נ',
	'ס',
	'פ',
	'ע',
	'צ',
	'ק',
	'ר',
	'ש',
	'ת',
	'ם', 'ף', 'ץ', 'ך'
]
bad_stuff = ['http', '👍🏼', '😍', '@', '😇', '🤔', '👏']

has_heb = lambda s: s in heb_ab
has_emojis_links = lambda collection: any(b in collection for b in bad_stuff)


def is_good(collection: str):
	if any(has_heb(s) for s in collection):
		return False
	if has_emojis_links(collection):
		return False
	for s in collection:
		if s * 3 in collection:
			return False
	return True


# is_good = lambda collection:
is_one_word_not_empty_or_qmark = lambda x: x != '' and x != '?' and x.count(' ') == 0


def find_name(line, names):
	for name in names:
		if name in line:
			name_idx = line.find(name)
			return remove_from(line, '\n', '*', '?', '!')[name_idx:]


def get_clean_line(line):
	colon_idx_1 = line.find(':') + 1
	colon_idx_2 = line.find(':', colon_idx_1) + 2
	return remove_from(line, '\n', '*', '?', '!')[colon_idx_2:]


def get_line_with_name(line):
	name_idx = line.find('- ') + 2
	return remove_from(line, '\n', '*', '?', '!', '"')[name_idx:]


def get_name(line):
	if 'Elad' in line:
		return 'Elad'
	elif 'Gilad' in line:
		return 'Gilad'
	elif 'null' in line:
		return 'null'
	elif 'גיא' in line:
		return 'Guy'
	else:
		return None


# words_def = {}


def append_or_set(d, key, value):
	try:  # if exists
		d[key].append(value)
	except KeyError:  # create value
		d[key] = [value]


def get_definitions_and_examples(query, dic=True, wordref=False, merriam=False):
	word = Word()
	if dic:
		word = dc.get_word(word, query)
	if wordref:
		word = wr.get_word(word, query)
	if merriam:
		word = mw.get_word(word, query)

	return word


def set_words_from_imported_conv():
	with open('text.txt', 'r', encoding='utf8') as f:
		conv = f.readlines()
	for i, line in enumerate(conv[1:], 1):
		clean_line = get_clean_line(line)
		if is_one_word_not_empty_or_qmark(clean_line):
			if is_good(clean_line):
				print(f'set_words_from_imported_conv|good|{clean_line}')
				word = get_definitions_and_examples(clean_line)
				words.append(word)


def get_words_raw_from_txt():
	with open('word_list.txt', 'r') as f:
		ret = []
		ret.extend(f.readlines())
	return ret


def write_words_to_csv():
	if len(words) == 0:
		for word in words_raw:
			words.append(get_definitions_and_examples(word))
	with open('eggs.csv', 'w', newline='', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
		                    quoting=csv.QUOTE_MINIMAL)
		for word in words:

			writer.writerow([word.query])
			for website, values in word.dictionaries.items():
				if values.definitions:
					writer.writerow([website])
					writer.writerow(['', 'Definitions'])
					for definition in values.definitions:
						writer.writerow(['', '', definition])
					if values.examples:
						writer.writerow(['', 'Examples'])
						for example in values.examples:
							writer.writerow(['', '', example])


def write_words_to_text_file():
	with open('word_list.txt', 'w') as f:
		for word in words:
			print(f'write_words_to_text|{word.query}')
			f.write(word.query + '\n')


# [print(w) for w in words_raw]
# write_words_to_file()

sender_words = {}
words = []
# words_raw = get_words_raw_from_txt()
# for word in words_raw:
# 	words.append(get_definitions_and_examples(word, dic=False, merriam=True))
# write_words_to_csv()


word = get_definitions_and_examples('Avarice', dic=True, wordref=True, merriam=True)
print()
