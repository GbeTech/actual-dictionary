from lib import wordreference as wr


def basic_wordreference(query, definitions, examples):
	word = wr.get_word(query=query)
	assert word.query == query
	assert word.dictionaries['wordreference.com'].definitions == definitions
	assert word.dictionaries['wordreference.com'].examples == examples


def test_iniquity():
	basic_wordreference('iniquity',
	                    definitions=['great and harmful injustice or wickedness.', 'a wicked act; sin.'],
	                    examples=[])


def test_reprimand():
	basic_wordreference('reprimand',
	                    definitions=[
		                    'a severe scolding or act of placing blame for wrongdoing, esp. a formal or official one.',
		                    'to scold or blame (someone) severely.',
		                    'a severe reproof or rebuke, esp. a formal one by a person in authority.',
		                    'to reprove or rebuke severely, esp. in a formal way.'],
	                    examples=['reprimanded by the judge and warned of a possible charge of contempt of court.',
	                              'The minister upbraided the parishioners for their poor church attendance.',
	                              'gently admonished the children to make less noise; admonished the players about promptness at practice sessions.',
	                              'censured in the media for her off-the-cuff remarks; voted to censure their fellow senator.'])


def test_rapierlike():
	basic_wordreference('rapierlike', definitions=[], examples=[])


def test_rapier():
	basic_wordreference('rapier',
	                    definitions=['a straight 2-edged sword with a narrow pointed blade',
	                                 'a straight sword with a narrow blade having two sharp edges'],
	                    examples=[
		                    'There is also a small sword, which is a martial weapon that came before single sword, and rapier, which is the type of weapon used by the Three Musketeers or the Count of Monte Cristo.',
		                    'The excavations, sponsored by the Croatoan Archaeological Society, have so far uncovered several artifacts that may have been made during Elizabethan times, including the handle of a rapier and bits of metal from clothing.',
		                    'The outdoor festival setting is ideal for this cheerful, rapier-twirling spectacle.',
		                    'Apparently, this exactly the kind of of rapier wit that the president is looking for in his spokespeople.',
		                    'To sharpen your rapier wit on your would-be guests.',
		                    'The excavations, sponsored by the Croatoan Archaeological Society, have so far uncovered several artifacts that may have been made during Elizabethan times, including the handle of a rapier and bits of metal from clothing.'])


def test_turnstile():
	basic_wordreference('turnstile', definitions=[
		'a structure to stop passage until a charge is paid, or to record the number of people passing through:',
		'a structure of four horizontally revolving arms pivoted atop a post and set in a gateway or opening in a fence to allow the controlled passage of people.',
		'a similar device set up in an entrance to bar passage until a charge is paid, to record the number of persons passing through, etc.'],
	                    examples=['He put his token in the turnstile.'])
