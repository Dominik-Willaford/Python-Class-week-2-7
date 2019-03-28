
sentence = 'Perl and Python programming languages are both cross platform in nature and can be used on Windows, Linux/Unix and Mac OS systems. This broad-based capability makes the Perl/Python Scripting languages highly useful in the field of technology. Both languages are highly capable in stream editing of data, data manipulation and parsing, which are programming capabilities required in IT Forensics'

numberOfOccurences = 0
for word in sentence.split():
    if word == 'Python' or word == 'Perl/Python':
        numberOfOccurences += 1
print(numberOfOccurences)

