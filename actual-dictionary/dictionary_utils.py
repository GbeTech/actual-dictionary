def get_from_next_def(text, tag, def_relative_idx=None):
	if def_relative_idx is None:
		def_relative_idx = len(tag)
	temp = text[text.index(tag):]
	return temp[def_relative_idx:].strip()


def get_from_next_ex(text, tag):
	temp = text[text.index(tag):]
	return temp[len(tag):].strip()
