from lib import merriam_webster as mw


def basic_merriam(query, definitions, examples):
	word = mw.get_word(query=query)
	assert word.query == query
	assert word.dictionaries['merriam-webster.com'].definitions == definitions
	assert word.dictionaries['merriam-webster.com'].examples == examples


def test_reprimand():
	basic_merriam('reprimand',
	              definitions=['a severe or formal reproof',
	                           'a severe or formal criticism',
	                           'to criticize (a person) severely or formally'],
	              examples=[
		              'while reviewing the troops, the officer delivered a curt reprimand to one of the soldiers',
		              'The soldiers were severely reprimanded.',
		              'reprimanded the summer intern for her constant tardiness'])


def test_iniquity():
	basic_merriam('iniquity',
	              definitions=['gross injustice', 'a wicked act or thing',
	                           'an evil or unfair act'],
	              examples=[
		              'the use of illegal narcotics is not only a destroyer of personal health but also an iniquity that undermines our society',
		              'a nation still struggling with the aftereffects of the iniquity of slavery'])


def test_rapierlike():
	basic_merriam('rapierlike', definitions=[], examples=[])


def test_rapier():
	basic_merriam('rapier',
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
	basic_merriam('turnstile',
	              definitions=[
		              'a post with arms pivoted on the top set in a passageway so that persons can pass through only on foot one by one'],
	              examples=[
		              'The subway turnstile — low enough to vault, ubiquitous enough to figure in the lives of millions of New Yorkers each day — has long served as a kind of dragnet for the Police Department.',
		              'In celebration, some Eagles fans across Philadelphia overturned cars, jumped SEPTA turnstiles, looted a gas station, smashed windows and broke the awning of the Ritz Carlton Hotel.',
		              'The Lynx is something of an honor system in that there is no turnstile to walk through.',
		              'Shoppers walking into the store scan their phone on a subway-station-like turnstile, connecting their presence in the store (as well as their family members or other fellow shoppers) with their Amazon profile.',
		              'Shoppers enter by scanning the Amazon Go smartphone app at a turnstile, opening plastic doors.',
		              'To enter the Amazon Go store, customers download a smartphone app and scan a QR code to open a glass turnstile.',
		              'New stairs and turnstiles will be added at a number of stations.',
		              'As tens of thousands of people poured through the turnstiles on their commutes that morning, the B, D, F and M lines, as well as portions of the E and R lines, all were stricken by delays in both directions.'])


def test_sputum():
	basic_merriam('sputum',
	              definitions=[
		              'matter expectorated from the respiratory system and especially the lungs that is composed of mucus but may contain pus, blood, fibrin, or microorganisms (such as bacteria) in diseased states'],
	              examples=[
		              'Refugees who have positive blood tests and chest x-rays are taken to a county health office for sputum tests, according to Robert Moser, head of Catholic Charities in San Diego.'])
