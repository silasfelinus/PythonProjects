"""Rewritten dictionary to use OrderedDict"""
from collections import OrderedDict

glossary = OrderedDict()

glossary['if'] = "conditional returning true or false"
glossary['elif'] = "The best thing since sliced bread."
glossary['dictionary'] = "What this is, even though we are also calling it a 'glossary'"
glossary['print'] = "Believe it or not,this prints"
glossary['python'] = "Either a snake or a comedy troupe or a language, still not sure"


for word, definition in glossary.items():
	print("\n" +
	word +
	": " +
	definition
	)