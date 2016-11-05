[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)


# Data Structure

* list
* tuple
* dictionary
* set

| TYPE | DESCRIPTION | EXAMPLE | UNIQUE VARIABLES | IMMUTABLE |
| :--: | :---------- | :------ | :--------------: | :-----: |
| list | Sequence | ['a', 1, 4,0, (tuple), [list]] | X | X |
| tuple | Sequence | ('a', 1, 4.0, (tuple), [list]] | X | O |
| dictionary | Hashmap(pair) | {key1:value1, key2:value2} | O(Key) | X |
| set | Hashmap | {key1, kye2} | O | X |

---
## List
A *MUTABLE* Sequence of Data: It can contains __different__ data types.

### Atom of list
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
| append | _list_.**append(var)** | mylist.append(yrlist) | ['a', 1, 'b', ['e', 'c', 'd']] |
| annex  | _list_.**extend(**_list_**)**  <br/> __list1__ **+=** __list2__ | mylist.extend(yrlist)  <br/> * mylist += yrlist | ['a', 1, 'b', 'e', 'c', 'd'] |
| insert | _list_.**insert(index, var)** | mylist.insert(1, 'z') | ['a', 'z', 1, 'b'] |
| remove | _list_.**remove(var)** | mylist.remove(1) | ['a', 'b'] |
| get var & remove | _list_.**pop( )** <br/> _list_.**pop(**0**)** <br/> _list_.**pop(**-1**)** | mylist.pop( ) <br/> mylist.pop(0) <br/> mylist.pop(-1) | console>'a' <br/> (list) [1, 'b'] <br/> console>'b' <br/> (list) ['a', 1] <br/> console>'b' <br/> (list) ['a', 1] |
| get index | _list_.**index(var)** | mylist.index('a') | 0 |
| count | _list_.**count(var)** | mylist.count('b') | 1 |
| sort | asc: _list_.**sort( )** <br/> desc: _list_.**sort(reverse=True)** | yrlist.sort() <br/> yrlist.sort(reverse=True) | ['c', 'd', 'e'] <br/> 'e', 'd', 'c'] |

### Built-in Function

| OPERATION | FUNCTION | EXAMPLE | RESULT |
| :-------- | :------- | :------ | :----- |
| sort & return a new list | **sorted(**_list_**)** | sorted(yrlist) | ['c', 'd', 'e'] |
| length | **len(**_list_**)** | len(mylist) | 3 |

### Statements

| OPERATION | STATEMENT | EXAMPLE | RESULT |
| :-------- | :-------- | :------ | :----- |
| delete | **del** _list_**[ ]** | del mylist[2] | ['a', 1] |

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

__** A copied list is not affected by the root list.**__

* **Copy(  )**  
* **list(  )**  
* **[ : ]**

---
## Tuple
A *IMMUTABLE* Sequence of Data: It can contains __different__ data types.

### Atom of tuple (key: value)

| KEY | VALUE |
| :-: | :---: |
| * boolean<br/>* integer<br/>* numeric<br/>* float<br/>* string<br/>*tuple  | * boolean<br/>* integer<br/>* numeric<br/>* float<br/>* string<br/>* list |



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



##Set
An **UNORDERED** Data Structure consists of **UNIQUE** values.




```python
s2 = set("Hello")
s2
{'e', 'l', 'o', 'H'}
```



---
## Dictionary
Not a sequence;(UNOREDERED) An dictionary cannot be indexed & cannot use offset.  
* Its _Key value_ **MUST BE UNIQUE** _(If overlapped, the Last input will be used.)_

Key에 리스트는 쓸 수 없다는 것이다. 하지만 튜플은 Key로 쓸 수 있다. 딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지 변하지 않는 값인지에 달려 있다. 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없는 것이다. 아래 예처럼 리스트를 Key로 설정하면 리스트를 키 값으로 사용할 수 없다는 형 오류(TypeError)가 발생한다.

```python
mydict = {'coffee': 7, 'milk': 11, 'water': 20, 'wine': 'outofstock'}
```


| OPERATION | METHOD          | EXAMPLE   | RESULT    |
| :-------- | :-------------- | :-------- | :-------: |
| Generate  | **{**a: b**}** <br/> **dict(**a, b**)**  | {'water': 20, 'wine': 'outofstock'} <br/> dict('water': 20, 'wine': 'outofstock')  | {'water': 20, 'wine': 'outofstock'}  |
| Transform to dict<br/>(ex) tuple to dict) | **dict((**pair or pairlist**))** | dict([('milk', 11), ('water': 20)]) | {'milk': 11, 'water': 20} |
| Offset | _dict_**[**key**]** | _mydict_**[**'milk'**]** | 11 |



---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)
