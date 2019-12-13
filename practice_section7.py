import unicodedata

#1
mystery = '\U0001f4a9'
#print('mystery :',mystery,'unicode :',unicodedata.name(mystery))

#2
pop_bytes=mystery.encode('utf-8')
#print(pop_bytes)

#3
pop_string = pop_bytes.decode('utf-8')
#print(pop_string)

#4
my_string = '''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.'''%('roast beef','ham','head','clam')

#print(my_string)

#5
letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. please note that it sould never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.

Thank you for your support.

Sincerely,
{spokeman}
{job_title}'''
#print(letter)

#6
response = {'salutation':'Hello','name':'jiwon','product':'airpod pro',
            'verbed':'go','room':'First','animals':'dogs','amount':'two',
            'percent':'30%','spokeman':'onwer','job_title':'adventure of life'}
#print(letter.format(**response))

#7
mammoth = """We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.
Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.
We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon."""

#8
import re
#print(re.findall(r'\bc\w*',mammoth))

#9
t=re.findall(r'\bc\w{3}\b',mammoth)
#print(t)

#10
#print(re.findall(r'\b\w*r\b',mammoth))

#11
vowel = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b',mammoth)
print(vowel)