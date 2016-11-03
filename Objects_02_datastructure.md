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
| append | __list__.**append(var)** | mylist.append(yrlist)** | ['a', 1, 'b', ['e', 'c', 'd']]
| annex  | * __list__.**extend(**__list__**)**  <br/> * __list1__ **+=** __list2__ | * mylist.extend(yrlist)  <br/> * mylist += yrlist | ['a', 1, 'b', 'e', 'c', 'd']
| insert | __list__.**insert(index, var)** | mylist.insert(1, 'z') | ['a', 'z', 1, 'b'] |
| remove | __list__.**remove(var)** | mylist.remove(1) | ['a', 'b'] |
| get var & remove | [1] __list__.**pop( )** <br/> [2] __list__.**pop(0)** <br/> [3] __list__.**pop(-1)** | [1] mylist.**pop( )** <br/> [2] mylist.**pop(0)** <br/> [3] mylist.**pop(-1)** | [1] 'a' \ [1, 'b'] <br/> [2] 'b' \ ['a', 1] <br/> [3] 'b' \ ['a', 1] |
| get index | __list__.**index(var)** | mylist.index('a') | 0 |
| count | __list__.**count(var)** | mylist.count('b') | 1 |
| sort | [1] asc: __list__.**sort( )** <br/> [2] desc: __list__.**sort(reverse=True)** | [1] yrlist.sort() <br/> [2] yrlist.sort(reverse=True) | [1] ['c', 'd', 'e'] <br/> [2] 'e', 'd', 'c'] |

#### Built-in Function

| OPERATION | FUNCTION | EXAMPLE | RESULT |
| sort & return a new list | **sorted(**__list__**)** | sorted(yrlist) | ['c', 'd', 'e'] |
| length | **len(**__list__**)** | len(mylist) | 3 |

#### Statements

| OPERATION | STATEMENT | EXAMPLE | RESULT |
| delete | **del** __list__**[ ]** | del mylist[2] | ['a', 1] |

---
#### Align

```python
mylist = [1, 2, 3]
xylist = mylist
xylist#[1, 2, 3]
```

* __**xylist only refers to mylist**__
```python
mylist[1] = 5
mylist#[1, 5, 3]
xylist#[1, 5, 3]
```

#### Copy

__** A copied list is not affected by the root list.**__

* **Copy( )**  
* **list( )**  
* **[:]**

---
### Tuple

