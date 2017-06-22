[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)


---

# Data Structure

* [Lists](#lists)
* [Tuples](#tuples)
* [Dictionaries](#dictionaries)
* [Sets](#sets)

| TYPE | DESCRIPTION | EXAMPLE | UNIQUE VARIABLES | IMMUTABLE |
| :--- | :---------- | :------ | :--------------: | :-----: |
| list | Sequence | **[**'a', 1, 4,0, (tuple), [list]**]** | X | X |
| tuple | Sequence | **(**'a', 1, 4.0, (tuple), [list]**)** | X | O |
| dictionary | Hashmap(pair) | **{**key1**:**value1, key2**:**value2**}** | O(Key) | X |
| set | Hashmap | **{**key1, key2**}** | O | X |





---
## Lists
A *MUTABLE* Sequence of Data: It can contains __different__ data types.

### Atom of a list
* boolean  
* integer  
* numeric  
* float  
* string  
* another list  
* tuple  
* dictionary  
* set  

### Operation
 
```python
mylist = ['q', 'u', 'e', 's', 't', 'i', 'o', 'n']
```

| OPERATION | METHOD          | EXAMPLE   | RESULT    |
| :-------- | :-------------- | :-------- | :-------: |
| Generate  | **[**a, b**]** <br/> **list(**a, b**)**  | ['t', 1] <br/> list('t', 1)  | ['t', 1]  |
| Transform to list<br/>(ex) tuple to list) | **list((**seq**))** | list('question') | ['q', 'u', 'e', 's', 't', 'i', 'o', 'n'] |
| Offset | _list_**[**int**]** | _mylist_**[**-2**]** | 'o' |
| Slice  | _list_**[**start\:end\:step**]** | _mylist_**[**7:2:-2**]** | ['n', 'i', 's'] |

### Methods
```python
mylist = ['a', 1, 'b']
yrlist = ['e', 'c', 'd']
```

| OPERATION | METHOD | EXAMPLE | RESULT |
| :-------- | :----- | :------ | :----- |
| Append | _list_.**append(var)** | mylist.append(yrlist) | ['a', 1, 'b', ['e', 'c', 'd']] |
| Annex  | _list_.**extend(**_list_**)**  <br/> __list1__ **+=** __list2__ | mylist.extend(yrlist)  <br/> * mylist += yrlist | ['a', 1, 'b', 'e', 'c', 'd'] |
| Insert | _list_.**insert(index, var)** | mylist.insert(1, 'z') | ['a', 'z', 1, 'b'] |
| Remove | _list_.**remove(var)** | mylist.remove(1) | ['a', 'b'] |
| Get var & remove | _list_.**pop( )** <br/> _list_.**pop(**0**)** <br/> _list_.**pop(**-1**)** | mylist.pop( ) <br/> mylist.pop(0) <br/> mylist.pop(-1) | console>'a' <br/> (list) [1, 'b'] <br/> console>'b' <br/> (list) ['a', 1] <br/> console>'b' <br/> (list) ['a', 1] |
| Get index | _list_.**index(var)** | mylist.index('a') | 0 |
| Count | _list_.**count(var)** | mylist.count('b') | 1 |
| Sort | asc: _list_.**sort( )** <br/> desc: _list_.**sort(reverse=True)** | yrlist.sort() <br/> yrlist.sort(reverse=True) | ['c', 'd', 'e'] <br/> 'e', 'd', 'c'] |
list + list
### Built-in Function

| OPERATION | FUNCTION | EXAMPLE | RESULT |
| :-------- | :------- | :------ | :----- |
| Sort & return a new list | **sorted(**_list_**)** | sorted(yrlist) | ['c', 'd', 'e'] |
| Length | **len(**_list_**)** | len(mylist) | 3 |

### Statements

| OPERATION | STATEMENT | EXAMPLE | RESULT |
| :-------- | :-------- | :------ | :----- |
| Delete | **del** _list_**[ ]** | del mylist[2] | ['a', 1] |

### Align
```python
mylist = [1, 2, 3]
xylist = mylist
xylist#[1, 2, 3]
```

* __**xylist refers to mylist**__  
It means the list [1, 2, 3] is assigned to mylist & xylist.
(In other words, that list can be called with both of names)  
If a mylist's variable changes, xylist  
```python
mylist[1] = 5
mylist#[1, 5, 3]
xylist#[1, 5, 3]
```

### Copy

* _list_.**Copy(  )**  
* **list(  )**  
* **[ : ]**


* #-- **_"Copy()" Method is used to copy & edit a list!)_** --#
1. Case 1(not using **_copy()_**)
```python
mylist = [0, 1, 2, 3, 4]
otlist = mylist
otlist[1] = 10
otlist#[0, 10, 2, 3, 4]
mylist#[0, 10, 2, 3, 4]
otlist == mydict#True

#If one is changed, both of dicts will be changed.
```


2. Case 2(using **_copy()_**)
```python

mylist = [0, 1, 2, 3, 4]
otlist = mylist.copy()
otlist[1] = 10
otlist#[0, 10, 2, 3, 4]
mylist#[0, 1, 2, 3, 4]
otdict == mydict#False
#Even if one is changed, the other will NOT be changed.
```


[↑ Up to the Top](#data-structure)





---
## Tuples
A *IMMUTABLE* Sequence of Data: It can contains __different__ data types.

### Type of a tuple (key: value)

| KEY | VALUE |
| :-: | :---: |
| boolean<br/>integer<br/>numeric<br/>float<br/>string<br/>**tuple**  | boolean<br/>integer<br/>numer### Operationic<br/>float<br/>string<br/>**list** |



### Operation
```python
mytuple = 'q', 'u', 'e', 's', 't', 'i', 'o', 'n'
```
| OPERATION | METHOD          | EXAMPLE   | RESULT    |
| :-------- | :-------------- | :-------- | :-------: |
| Generate  | **(**var1, var2**)** <br/> **tuple(**var1, var2**)** <br/> var1**,** var2 | ('t', 1) <br/> tuple('t', 1) <br/> 't', 1 | ('t', 1)  |
| Generate(single var)  | **(**var1**,)** <br/> **tuple(**var1**,)** <br/> var1**,**  | ('t',) <br/> tuple('t',) <br/> 't', | ('t',)  |
| **UNPACKING** | name1, ..., nameN = _tuple_ (len=N) | foo, bar = tuple('t', 1) | foo # 't', bar # 1 |

### Advantages of TUPLE
* A Tuple uses less space than a list  
* Items of a tuple are IMMUTABLE; It cannot be damaged  


[↑ Up to the Top](#data-structure)





---
## Dictionaries
Not a sequence;(UNOREDERED) An dictionary cannot be indexed & cannot use offset.  
* Its _Key value_ **MUST BE UNIQUE** ~~_(If overlapped, the Last input will be used.)_~~

> Key에 list는 사용 불가, tuple은 사용 가능.(Immutable)  
> list를 Key로 설정하면 TypeError 발생.  

### Operation
```python
mydict = {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
yrdict = {'milk' : 8, 'juice' = 7 }
```

| OPERATION | METHOD          | EXAMPLE   | RESULT    |
| :-------- | :-------------- | :-------- | :-------- |
| Generate  | **{**a: b**}** <br/> **dict(**a, b**)**  | {'water': 20, 'wine': 'outofstock'} <br/> dict('water': 20, 'wine': 'outofstock')  | {'water': 20, 'wine': 'outofstock'}  |
| Transform to dict<br/>(ex) tuple to dict) | **dict((**pair or pairlist**))** | dict([('milk', 11), ('water': 20)]) | {'milk': 11, 'water': 20} |
| Select | _dict_**[**key**]** | mydict['milk'] | 11 |
| Select All keys | _dict_.**keys( )** | mydict.keys() | dict_keys(['coffee', 'milk', 'water', 'wine']) |
| Select All values | _dict_.**values( )** | mydict.values() | dict_values([7, 11, 20, 'outofstock']) |
| Select All elements by tuple | _dict_.**items( )** | mydict.items() | dict_items([('coffee', 7), ('milk', 11), ('water', 20), ('wine', 'outofstock')]) |
| Replace | _dict_**[**key**]=newval**<br/>_dict_**[**newkey**]**=newval | mydict['milk']=10<br/>mydict['tea']=10 | {'coffee': 7, 'milk': 10, 'water': 20, 'wine': 'outofstock'}<br/>{'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock', 'tea' = 10} |
| Update or Join | _dict1_.**update(**dict2**)** | mydict.update(yrdict) | {'coffee': 7, 'milk': 8, 'water': 20, 'wine': 'outofstock', 'juice' = 7 } |
| **_Copy_** | _dict_.**copy( ) ** | otdict = mydict.copy() | {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'} |
| Delete | **del** _dict_**[**key**]** | del mydict['wine'] | {'coffee': 7, 'milk': 11, 'water': 20} |
| Delete All | _dict_.**clear( )**<br/>_dict_ **= { }** | mydict.clear()<br/>mydict = {} | {} |
| Check a key | **'**key**' in **_dict_ | 'beer' in mydict<br/>'coffee' in mydict | False<br/>True |

* #-- **_"Copy()" Method is used to copy & edit a dict!)_** --#
1. Case 1(not using **_copy()_**)
```python
mydict = {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
otdict = mydict
otdict['coffee'] = 10
otdict#{'coffee': 10, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
mydict#{'coffee': 10, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
otdict == mydict#True

#If one is changed, both of dicts will be changed.
```

2. Case 2(using **_copy()_**)
```python
mydict = {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
otdict = mydict.copy()
otdict['coffee'] = 10
otdict#{'coffee': 10, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
mydict#{'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
otdict == mydict#False
#Even if one is changed, the other will NOT be changed.
```


[↑ Up to the Top](#data-structure)

## Sets
An **UNORDERED** Data Structure consists of **UNIQUE** items.(As a dict, only the KEY part)
* If there are overlapped values, ONLY ONE can remains.
* Set is used to calculate "Sets" on Mathmatics;Unions,Differences & Intersections


### Operation
```python
myset = {'e', 'l', 'e', 'm', 'e', 'n', 't', 's'}
myset#{'e', 'l', 'm', 'n', 't', 's'}
yrset = {'e', 'l', 'e', 'f', 'a', 'n', 't', 's'}
yrset#{'e', 'l', 'f', 'a', 'n', 't', 's'}

myset = { }#It generates A DICTIONARY, NOT A SET!
mydict = {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
```

| OPERATION | METHOD          | EXAMPLE   | RESULT    |
| :-------- | :-------------- | :-------- | :-------- |
| Generate  | **set( )**<br/>**set(**list & string & tuple & dict**)**<br/>**{**values**}** | myset = set()<br/>set(mydict)<br/>myset = {'e', 'l', 'e', 'm', 'e', 'n', 't', 's'} | { }(a set)<br/>{'coffee', 'milk', 'water', 'wine'}#_(only the keys)_<br/>{'e', 'l', 'm', 'n', 't', 's'} |
| Union(|) | _set1_.**union(**_set2_**)** | myset.union(yrset) | {'e', 'l', 'm', 'n', 't', 's', 'f', 'a'} |
| Intersection(&) | _set1_.**intersection(**_set2_**)** | myset.intersection(yrset) | {'e', 'l', 'n', 't', 's'} |
| Difference(_set1_ **-** _set2_) | _set1_.**difference(**_set2_**)** | myset.difference(yrset) | {'m'} | 
| Difference(_set2_ **-** _set1_) | _set2_.**difference(**_set1_**)** | yrset.difference(myset) | {'f', 'a'} | 
| Symmetric<br/>Difference(^)<br/>(_Union_ **-** _Intersection_) | _set1_.**symmetric_difference(**_set2_**)** | myset.union(yrset) | {'m', 'f', 'a'} |
| Subset(<=) |  _set1_.**issubset(**_set2_**)** | myset.issubset(yrset) | False | 
| Superset(>=) |  _set1_.**issuperset(**_set2_**)** | myset.issuperset(yrset) | False |


[↑ Up to the Top](#data-structure)





---
## Ndarray(numpy.ndarray)
[Go to Numpy]()
### Operation
```python
import numpy as np
myarray = np.array([0, 1, 2.5, 4, 4.5])
```

[↑ Up to the Top](#data-structure)





---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)
