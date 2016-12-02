'''
name = input('What is your name? > ' )
stuff = 'josoishluhsf'
welcome = "Hello {1}!".format(stuff, name)

print(welcome)
'''
#####
'''
### easy one
noun = input('Choose a NOUN, please... > ')
adj_noun = input('Choose an adjective noun, please... > ')
madlib_finish = "The {} jumped over the {}! ".format(noun, adj_noun)

print(madlib_finish)
'''

### advanced one
print("Let's create a madlib limerick!")
noun_one = input('Choose a one syllable NOUN, please... > ')
name = input ("OH WHAT'S IN A NAME??? ... Give me a three syllable name... > ")
noun_two = input('Choose a different NOUN, make it rhyme with the name - dammit... > ')
noun_three = input(' Yet another NOUN, different than the others... duh... > ')
noun_four = input("You guessed it... a different NOUN... rhymes with you last noun...don't judge me... > ")
noun_five = input(" Can I trouble you for another single syllable noun? ... > ")
past_tense_verb = input("Enter a past tense verb..it's ok it you need to look it up...really... >  ")
past_tense_verb_two = input(" Gimme another past tense verb...rhymes with the name... >  ")
verb = input(" Finally, give me a verb ... > ")

madlib_finish_two = """There once was a {noun_one} named {name}.
Who {past_tense_verb} in a vat of {noun_two}.
With a flick of their {noun_three}, and a {verb} of their {noun_four}
A jumble of {noun_five} was {past_tense_verb_two}.""".format(noun_one=noun_one,
name=name, past_tense_verb=past_tense_verb,noun_two=noun_two, noun_three=noun_three,
verb=verb,noun_four=noun_four, noun_five=noun_five, past_tense_verb_two=past_tense_verb_two )

print(madlib_finish_two)

"""

Madlib

The NOUN jumped over the ADJ NOUN.
Prompt user to input the three placeholder words, save them in variables, interpolate them in

Advanced

Look up a more complicated madlib and fill that out.
There once was a NOUN named NAME.
Who PAST TENSE VERB in a vat of NOUN.
With a flick of their NOUN, and a VERB of their NOUN
A jumble of NOUN was PAST TENSE.


Super Advanced

Make a flexible madlib parser for any length madlib.

Read a madlib from a text file that has the special text {noun} for each placeholder.
Ask the user for a real word for each placeholder.
Then fill in those words and print ou the final madlib.
"""
