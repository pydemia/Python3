# ```Scikit-Learn```

A machine learning library in Python.

## ```API```

* ```fit()```
* ```transform()```
* ```fit_transform()```

Use ```fit()``` to train(learn) from a Dataset and then use ```transform()``` to test(estimate) 

### Example 1: Both the trainset and the testset are the same
```python
from sklearn import RandomizedPCA

tmp = RandomizedPCA(n_components=3)   # Generate a PCA object.

tmp.fit(trainData)                    # Fit the PCA object to a trainset.(Training)

tmp.transform(trainData)              # Transform the PCA object, which were fitted to the trainset, to the trainset again.
                                      # (Estimation)

# It can be executed at once.
tmp.fit_transform(trainData)
```

### Example 2: Train with A, 
