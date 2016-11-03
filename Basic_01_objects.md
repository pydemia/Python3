#Objects

Variable:Object(Data) = 참조(이름):실제 객체(memory에 존재)
mutable:immutable = memory에 있는 실제 Data value를 변경할 수 있는지 없는 지

---
variable naming  

| list                                               | example            |
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
##Data type
* integer: 정수;5,0,~~05~~  
* numeric: 실수  
* float: 실수(소수점, 지수 등)  
* string:  텍스트 문자열 Sequence;indexing/slicing 가능)
* boolean

##Data Structure
* list
* tuple
* dictionary
* set

---
###integer, numeric, float


#### Change Data Type Method(trunc)
* **int()**
* **float()**


#### Operation

| Operator | description         | example | result | function                 |
| :------: | :------------------ | :------ | -----: | :----------------------- |
| +        | addition            | 3 + 8   | 24     | add(a, b)                |
| -        | subtraction         | 20 - 7  | 13     | sub(a, b)                |
| *        | multiplication      | 5 * 3   | 15     | mul(a, b)                |
| /        | division(float)     | 20 / 8  | 2.5    | div(a, b), trediv(a, b)  |
| //       | division(integer)   | 20 // 8 | 2      | floordiv(a, b)           |
| %        | division(remainder) | 20 % 8  | 4      | mod(a, b), devmod(a, b)  |
| **       | exponentiation      | 3 ** 5  | 243    | pow(a, b)                |
[종류 및 용법]

#### Assignment: **=**
```python
foo = 10
foo = foo -3
```

| Operator | description  |
| :------: | :----------: |
| a += b   | a = a + b    |
| a -= b   | a = a - b    |
| a *= b   | a = a * b    |
| a /= b   | a = a / b    |
| a //= b  | a = a // b   |
| a %= b   | a = a % b    |
| a **= b  | a = a ** b   |
[종류 및 용법]

#### Base: decimal(default), binary, octal, hex(0~9,a~f)
| Base   | description  | example | result |
| :----: | :----------: | :------ | :----- |
| binary | 0b, 0B       | 0b10    | 2      |
| octal  | 0o, 0O       | 0o10    | 8      |
| hex    | 0x, 0X       | 0x10    | 16     |
[종류 및 용법]

#### Approximation
| Appox    | method       |
| :------: | :----------- |
| round    | round()      |
| ceiling  | math.ceil()  |
| floor    | math.floor() |
| truncate | amth.trunc() |
[종류 및 용법]

---
### String

* Single Line Quatation: **' '**, **" "**
* Multiple Line Quatation: **''' '''**, **""" """**
* Escape: \n, \t, \\

#### Change Data Type Method
* **str()**

#### Operation

| Operator | description       | example     | result   | function                 |
| :------: | :---------------- | :---------- | -------: | :----------------------- |
| +        | concatenate       | 'aa' + 'bb' | 'aabb    | concat(a, b)             |
| *        | copy              | 'aa' * 3    | 'aaaaaa' |                          |
[종류 및 용법]

#### Indexing
* **[]**(_like a list_)
```python
mystr = 'abcdefg'
mystr[0]#a
mystr[2]#c
mystr[-2]#f

####Slicing, Substring
* **[start:end:step]**(_like a list_)
