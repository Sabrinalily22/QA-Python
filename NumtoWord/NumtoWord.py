import pdb
digit = {
  "0": "",
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  '8': 'Eight',
  '9': 'Nine',
  '10': 'Ten',
  '11': 'Eleven',
  '12': 'Twelve',
  '13': 'Thirteen',
  '14': 'Fourteen',
  '15': 'Fithteen',
  '16': 'Sixteen',
  '17': 'Seventeen',
  '18': 'Eightteen',
  '19': "Nineteen"
}
ten = {
    '1': 'Ten',
    '2': 'Twenty',
    '3': 'Thirty',
    '4': 'Fourty',
    '5': 'Fifty',
    '6': 'Sixty',
    '7': 'Seventy',
    '8': 'Eighty',
    '9': 'Ninety'
}
factor = {
    '1': 'Hundred',
    '2': 'Thousand',
    '3': 'Million',
    '4': 'Billion',
    '5': 'Trillion',
    '6': 'Quadrillion',
    '7': 'Quintillion'
}

def tens(x):
  x = str(x)
  if x[0] == '0':
    return digit[x[1]]
  if x[0] == '1':
    return digit[x]
  else:
    return ten[x[0]] + ' ' + digit[x[1]]

def integer(number, inc):
  number = str(number)
  e = str(inc + 1)  
  if len(number) == 3:
    if difference == 0:      
      return digit[number[0]] + ' Hundred ' + 'and ' + tens(number[1:3])
    else:
      return digit[number[0]] + ' Hundred ' + 'and ' + tens(number[1:3]) + ' ' + factor[e] + ','
  elif difference == 0:
    return tens(number)
  else:
    return tens(number) + ' ' + factor[e] + ', '

def loopy(x):
  numlist = ([str(x[::-1][i:i+3][::-1]) for i in range(0, len(x), 3)][::-1])
  length = len(numlist)
  global difference
  index = 0
  for i in numlist:
    index += 1
    difference = length - index
    print(f"{integer(i,difference)}", end=" ") 
  print('\n')

#NumtoWord = str(input("Enter any Number?  "))
#loopy(NumtoWord)


def test_tens():
  assert tens(18) == "Eighteen"


loopy("1")
loopy("10")
loopy("18")
loopy("20")
loopy("99")
loopy("101")
loopy("132")
loopy("1024")
loopy("12560")
loopy("120000555")
loopy("50342")
loopy("383578325783257032085")
