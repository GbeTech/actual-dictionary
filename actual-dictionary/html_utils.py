def remove_from(collection, *args):
	for arg in args:
		collection = collection.replace(arg, '')
	return collection


def get_next_tag(collection):
	first_tag_open_idx = collection.index('<')
	first_tag_close_idx = collection.index('>')
	tag_content = collection[first_tag_open_idx:first_tag_close_idx + 1]
	return tag_content


def remove_tags_from(collection: str):
	try:
		tag_content = get_next_tag(collection)
		collection = collection.replace(tag_content, '')
	except ValueError:
		return collection
	return remove_tags_from(collection)


def remove_tags_from_iter(collection: str):
	try:
		while True:
			tag_content = get_next_tag(collection)
			collection = collection.replace(tag_content, '')
	except ValueError:
		pass
	return collection


def get_text_idx(website):
	count = 0
	text = []
	for i, s in enumerate(website):
		if s == '<' or s == '>':
			count = 0
			text = []
		else:
			count += 1
			text.append(s)
