# warnings

```py
import warnings
```

## Classes

| Class | Descriptions |
| :---- | :----------- |
| Warning	| This is the base class of all warning category classes. It is a subclass of Exception. |
| UserWarning	| The default category for warn(). |
| DeprecationWarning	| Base category for warnings about deprecated features. |
| SyntaxWarning	| Base category for warnings about dubious syntactic features. |
| RuntimeWarning	| Base category for warnings about dubious runtime features. |
| FutureWarning	| Base category for warnings about constructs that will change semantically in the future. |
| PendingDeprecationWarning	| Base category for warnings about features that will be deprecated in the future (ignored by default). |
| ImportWarning	| Base category for warnings triggered during the process of importing a module (ignored by default). |
| UnicodeWarning	| Base category for warnings related to Unicode. |
| BytesWarning	| Base category for warnings related to bytes and buffer. |

## Filter

```py
warnings.simplefilter('default', ImportWarning)
```

| Value | Descriptions |
| :---- | :----------- |
| "error" | turn matching warnings into exceptions |
| "ignore" | never print matching warnings |
| "always" | always print matching warnings |
| "default" | print the first occurrence of matching warnings for each location where the warning is issued |
| "module" | print the first occurrence of matching warnings for each module where the warning is issued |
| "once" | print only the first occurrence of matching warnings, regardless of location |

## Warning

`warnings.warn(message, category=None, stacklevel=1)`
```py
warnings.warn(message, DeprecationWarning, stacklevel=1)
warnings.warn(message, stacklevel=1)
```
