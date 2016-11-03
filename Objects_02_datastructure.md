#Objects

##Data Structure
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
### List
A *MUTABLE* Sequence of Data: It can contains different types

#### Generate
* **[a, b]**
* **list(a, b)**

#### Transform to list
* **list(('a', 'b', 'c')**

#### Offset
* **ls_name[-2]**

#### Slice
* **ls_name[0:7:-2]**

---
#### Methods
```python
mylist = ['a', 1, 'b']
yrlist = ['e', 'c', 'd']
```

| OPERATION | METHOD | EXAMPLE | RESULT |
| :-------- | :----- | :------ | :----- |
| append | _list_.**append(var)** | mylist.append(yrlist)** | ['a', 1, 'b', ['e', 'c', 'd']] |
| annex  | _list_.**extend(**_list_**)**  <br/> __list1__ **+=** __list2__ | mylist.extend(yrlist)  <br/> * mylist += yrlist | ['a', 1, 'b', 'e', 'c', 'd'] |
| insert | _list_.**insert(index, var)** | mylist.insert(1, 'z') | ['a', 'z', 1, 'b'] |
| remove | _list_.**remove(var)** | mylist.remove(1) | ['a', 'b'] |
| get var & remove | _list_.**pop( )** <br/> _list_.**pop(0)** <br/> _list_.**pop(-1)** | mylist.**pop( )** <br/> mylist.**pop(0)** <br/> mylist.**pop(-1)** | console>'a' <br/> (list) [1, 'b'] <br/> console>'b' <br/> (list) ['a', 1] <br/> console>'b' <br/> (list) ['a', 1] |
| get index | _list_.**index(var)** | mylist.index('a') | 0 |
| count | _list_.**count(var)** | mylist.count('b') | 1 |
| sort | asc: _list_.**sort( )** <br/> desc: _list_.**sort(reverse=True)** | yrlist.sort() <br/> yrlist.sort(reverse=True) | ['c', 'd', 'e'] <br/> 'e', 'd', 'c'] |

#### Built-in Function

| OPERATION | FUNCTION | EXAMPLE | RESULT |
| :-------- | :------- | :------ | :----- |
| sort & return a new list | **sorted(**_list_**)** | sorted(yrlist) | ['c', 'd', 'e'] |
| length | **len(**_list_**)** | len(mylist) | 3 |

#### Statements

| OPERATION | STATEMENT | EXAMPLE | RESULT |
| :-------- | :-------- | :------ | :----- |
| delete | **del** _list_**[ ]** | del mylist[2] | ['a', 1] |

---
#### Align

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

#### Copy

__** A copied list is not affected by the root list.**__

* **Copy(  )**  
* **list(  )**  
* **[ : ]**

---
### Tuple
