#Objects

Variable:Object(Data) = 참조(이름):실제 객체(memory에 존재)
mutable:immutable = memory에 있는 실제 Data value를 변경할 수 있는지 없는 지

variable naming  
> *lower alphabet*;foo, bAr, baZ   
> *upper alphabet*: FOO, Bar, BaZ  
> *number*(_A name cannot be started with number_); ~~1foo~~, b2ar  
> *underscore*; _foo, _b_a_r, _baz_  
> _\# a name started with underscore is dealt with in some special way._ 

* **Reserved words*
> False None True  
> and or not is in  
> class def lambda global nonlocal  
> for if else elif while pass break continue  
> try except with yield return  
> del assert finally raise  
> from import as  


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

* Operator
| Operator | explanation         | example | result |
| :------- | :-----------------: | :-----: | -----: |
| +        | addition            | 3 + 8   | 24     |
| -        | subtraction         | 20 - 7  | 13     |
| *        | multiplication      | 5 * 3   | 15     |
| /        | division(float)     | 20 / 8  | 2.5    |
| //       | division(integer)   | 20 // 8 | 2      |
| %        | division(remainder) | 20 // 8 | 4      |
| **       | power               | 3 ** 5  | 243    |
[종류 및 용법]
