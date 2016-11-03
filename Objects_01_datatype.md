(Objects)

Variable:Object(Data) = 참조(이름):실제 객체(memory에 존재)  
mutable:immutable = memory에 있는 실제 Data value를 변경할 수 있는지 없는 지

---
## Variable Naming  

| ATTRIBUTE                                          | EXAMPLE            |
| :------------------------------------------------- | :----------------- |
| **lower alphabet**                                 | foo, bAr, baZ      | 
| **upper alphabet**                                 | FOO, Bar, BaZ      |  
| **number**(_A name cannot be started with number_) | ~~1foo~~, b2ar     |  
| **underscore**                                     | _foo, _b_a_r, _baz_ |  
 __\# a name started with underscore is dealt with in some special way.__  
---

* **Reserved words**
> False None   True  
> and   or     not is  in  
> class def    lambda  global   nonlocal  
> for   if     else    elif     try      except
> while pass   break   continue   with   yield  return  
> del   assert finally raise  
> from  import as  


---
#Data type
* integer: 정수;5,0,~~05~~  
	concatenate	'aa' + 'bb'	'aabb'	concat(a, b)
* numeric: 실수  
* float: 실수(소수점, 지수 등)  
* string:  텍스트 문자열 Sequence;indexing/slicing 가능)
* boolean

---
##integer, numeric, float

### Change Data Type Built-in Function(trunc)
* **int()**
* **float()**


### Operation

| OPERATOR | DESCRIPTION         | EXAMPLE | RESULT | FUNCTION                 |
| :------: | :------------------ | :-----: | :----: | :----------------------- |
| +        | addition            | 3 + 8   | 24     | add(a, b)                |
| -        | subtraction         | 20 - 7  | 13     | sub(a, b)                |
| *        | multiplication      | 5 * 3   | 15     | mul(a, b)                |
| /        | division(float)     | 20 / 8  | 2.5    | div(a, b), trediv(a, b)  |
| //       | division(integer)   | 20 // 8 | 2      | floordiv(a, b)           |
| %        | division(remainder) | 20 % 8  | 4      | mod(a, b), devmod(a, b)  |
| **       | exponentiation      | 3 ** 5  | 243    | pow(a, b)                |

### Assignment: **=**
```python
foo = 10
foo = foo -3
```

| OPERATOR | DESCRIPTION  |
| :------: | :----------: |
| a += b   | a = a + b    |
| a -= b   | a = a - b    |
| a *= b   | a = a * b    |
| a /= b   | a = a / b    |
| a //= b  | a = a // b   |
| a %= b   | a = a % b    |
| a **= b  | a = a ** b   |

### Base: decimal(default), binary, octal, hex(0~9,a~f)
| BASE   | DESCRIPTION  | EXAMPLE | RESULT |
| :----: | :----------: | :-----: | :----- |
| binary | 0b, 0B       | 0b10    | 2      |
| octal  | 0o, 0O       | 0o10    | 8      |
| hex    | 0x, 0X       | 0x10    | 16     |

### Approximation
| APPROX   | BUILT-IN FUNCTION/METHOD       |
| :------: | :----------- |
| round    | round()      |
| ceiling  | math.ceil()  |
| floor    | math.floor() |
| truncate | amth.trunc() |

---
## String

* Single Line Quatation: **' '**, **" "**
* Multiple Line Quatation: **''' '''**, **""" """**
* Escape: \n, \t, \\

### Operation

| OPERATOR | DESCRIPTION       | EXAMPLE     | RESULT   | FUNCTION                 |
| :------: | :---------------- | :---------- | :------: | :----------------------- |
| +        | concatenate       | 'aa' + 'bb' | 'aabb'   | concat(a, b)             |
| *        | copy              | 'aa' * 3    | 'aaaaaa' |                          |

### Indexing
* **[ ]**(_like a list_)
```python
mystr = 'abcdefg'
mystr[0]#a
mystr[2]#c
mystr[-2]#f
```
###Slicing, Substring
* **[start \: end \: step]**(_like a list_)
* offset
start:0  
end: last-1
```python
mystr = 'abcdefg'
mystr[:]#'abcdefg'
mystr[3:]#'defg'
mystr[3:8]#'defg'
mystr[:4]#'abcd'
mystr[1:5]#'bcde'
mystr[1:5:2]#'bd'
```

### Methods
#### Built-in Functions

| OPERATION          | FUNCTION | EXAMPLE | RESULT | RESULT TYPE |
| :----------------- | :----- | :------ | :----: | :---------: |
| length of string   | **len()** | len('11') | 2 | int         |
| change to string   | **str()** | str('11') | '11'| str    |

#### String Methods
* split a string to smaller strings: _string_.**split()**
```python
myword = 'to be, or not to be'
myword.split(',')
# ['to be', 'or not to be']
# list
```
* join a list of strings together: _string_.**join()**
```python
mywords = ['to be', 'or not to be', 'that is my question']
sentence = '! '.join(mywords)
# 'to be! or not to be! that is my question!'
# str
```

* Other Methods

| METHOD | RESULT TYPE | DESCRIPTION |
| :----- | :---------: | :---------- |
| _string_.**startswith(str)** | boolean | check if string starts with str |  
| _string_.**endswith(str)** | boolean | check if string ends with str | 
| _string_.**find(str)** | int | get the first index of a str you find from string  
| _string_.**rfind(str)** | int | get the last index of a str you find from string    
| _string_.**count(str)** | int | how many str exists in string |
| _string_.**isalnum(str)** | boolean | check if string only contains numbers |  
| _string_.**strip(str)** | str | new string eliminated str at the startpoint & endpoint |
| _string_.**capitalize()** | str | Capitalize the first alphabet of string |
| _string_.**title()** | str | Capitalize The First Alphabet Of Each Words |
| _string_.**upper()** | str | CAPITALIZE ALL ALPHABETS |
| _string_.**lower()** | str | un-capitalize all alphabets |
| _string_.**swapcase()** | str | CAPITALIZE LOWER ALPHABETS & un-capitalize upper alphabets |
| _string_.**center(50)** | str | align string on center within 50 spaces |
| _string_.**ljust(50)** | str | align string on left within 50 spaces |
| _string_.**rjust(50)** | str | align string on right within 50 spaces |
| _string_.**replace('a', 'b', 7)** | str | replace 'a' to 'b', in string, by 7 times |

