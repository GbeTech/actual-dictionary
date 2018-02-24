from lib import dictionary_com as dc


def basic_dc(query, definitions, examples):
	word = dc.get_word(query=query)
	assert word.query == query
	assert word.dictionaries['dictionary.com'].definitions == definitions
	assert word.dictionaries['dictionary.com'].examples == examples


def test_reprimand():
	basic_dc('reprimand',
	         definitions=['a severe reproof or rebuke, especially a formal one by a person in authority.',
	                      'to reprove or rebuke severely, especially in a formal way.',
	                      'a reproof or formal admonition; rebuke',
	                      '(transitive) to admonish or rebuke, esp formally; reprove'],
	         examples=[
		         'Two years later, the reprimand was overturned, but Mia was unsuccessful in her bid to annul the adoptions.',
		         'He failed to reprimand the MKs in question, implicitly suggesting that in the Likud, support for two states is optional at best.',
		         'He Made a Positive Test Result ‘Go Away’ Did Armstrong pay to have a reprimand by the International Cycling Union disappear?',
		         'He and one other officer received only a letter of reprimand.',
		         'He said he was not allowed to keep a copy of the classified letter of reprimand.',
		         'He frequently spoke in verse when he wished to reprimand an artiste.',
		         'I hope Collins will be consoled, and light his segar with the reprimand.',
		         'Now the memory of the reprimand was a strong spur to endeavour.',
		         'He said nothing, except to reprimand me for assaulting Martin.',
		         'At any rate, he thought, the reprimand would be only a matter of form.'])


def test_iniquity():
	basic_dc('iniquity',
	         definitions=['gross injustice or wickedness.', 'a violation of right or duty; wicked act; sin.',
	                      'lack of justice or righteousness; wickedness; injustice', 'a wicked act; sin'],
	         examples=[
		         'He stormed legendary spots like Palladium and Tunnel, and turned them into strobe-lit dens of iniquity.',
		         'He read Borges and admired him, but the title of The Universal History of iniquity gave him an immediate jolt.',
		         'Residents of South Carolina divorce at a rate twice as high as for that den of iniquity, Washington, D.C.',
		         'The guerrillas also attacked the hotel, he says, because it was a den of iniquity in the eyes of the puritanical insurgency.',
		         'A cynic might question the use of religion as a landing pad when one is tumbling from a place of power into the abyss of iniquity.',
		         'The young Arab spoke to the boards as though they were partners in his iniquity.',
		         'The cup of their iniquity was full; or they had not fallen so signally, thus.',
		         'I felt now that I might as well follow the iniquity to the end.',
		         'For my part, I call that downright countenancing of iniquity.',
		         'He now stood obstinately resolved to persevere in his iniquity.'])


def test_rapierlike():
	basic_dc('rapierlike', definitions=[], examples=[])


def test_turnstile():
	basic_dc('Turnstile',
	         definitions=[
		         'a structure of four horizontally revolving arms pivoted atop a post and set in a gateway or opening in a fence to allow the controlled passage of people.',
		         'a similar device set up in an entrance to bar passage until a charge is paid, to record the number of persons passing through, etc.',
		         'a mechanical gate or barrier with metal arms that are turned to admit one person at a time, usually in one direction only',
		         'any similar device that admits foot passengers but no large animals or vehicles',
		         '(logic) Also called gatepost. a symbol of the form ̃⊢, ⊨, or ⊩, used to represent logical consequence when inserted between expressions to form a sequent, or when prefixed to a single expression to indicate its status as a theorem'],
	         examples=['Unfortunately Lauren is watching this entire scene wedged in the turnstile by the Maclaren.',
	                   'He jumps out, goes through the turnstile, and enters the next train as it pulls into the station.',
	                   'One must pass through a turnstile before these wonders are accessible.',
	                   'A balanced barrier to a passage in a fort, of the nature of a turnstile.',
	                   'They paid their two halfpennies at the turnstile and crossed the bridge.',
	                   'A railing should be built in front of the turnstile to block the passage on that side.',
	                   'If you want to know what that means, go somewhere and watch a turnstile.',
	                   'The rest was lost in the clicking of the turnstile that let him through.',
	                   'A clicking, turnstile gate allowed only one to pass out at a time.',
	                   'Something clicked behind me like the turnstile at the gate of a show.'])


def test_sputum():
	basic_dc('sputum',
	         definitions=[
		         'matter, as saliva mixed with mucus or pus, expectorated from the lungs and respiratory passages.',
		         'a mass of salivary matter ejected from the mouth',
		         'saliva ejected from the mouth mixed with mucus or pus exuded from the respiratory passages, as in bronchitis or bronchiectasis'],
	         examples=[
		         'Third, the virus could not be found in sputum, further supporting the clear observation that airborne spread does not occur.',
		         'The germ is found in the sputum and in the nasal secretions.',
		         'Do not dress if the temperature is above 99 degrees, or if there is blood in the sputum.',
		         'It is the sputum after its discharge from the body on which our attention must be fixed.',
		         'The sputum should always be examined, both unstained and stained.',
		         "The sputum should be fresh—not more than three or four hours' old.",
		         'In pneumonic cases the bacillus may be found in the sputum of the patient.',
		         'The amount of sputum should be noticed as well as its appearance.',
		         'We are caring for the sputum, but many other avenues for the diffusion of the disease are open.',
		         'No examination of the sputum was made except in cases of suspects.'])
