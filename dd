import numpy as np
import pandas as pd
from datetime import datetime as dt

from unipy.sample.datasets import dataManager
from scipy.stats import spearmanr
from multiprocessing import Process as mpc
from multiprocessing import Queue as que

ls = pvtbl.coluns.get_level_values(2).unique()
groupA = pvtbl.xs(ls[0], axis=1, level=2, drop_level=False)
groupB = pvtbl.xs(ls[1], axis=1, level=2, drop_level=False)

def corrLoop(dataA, dataB):
  
  arr = np.empty(dataB.shape[1], 0)
  for i in range(dataA.shape[1]):
    corr, _ = spearmanr(dataA.iloc[:,i], groupB, axis=0)
    arr = np.insert(arr, i, corr[0][1:])
  res = pd.DataFrame(res,
                     columns=dataA.columns,
                     index=dataB.columns)
  return res

ini_tm = dt.now()
if __name__ = '__main__':
  
  # Assign output queues
  result1 = que()
  result2 = que()
  result3 = que()
  result4 = que()
  
  # Assign each processes
  divLen = int(groupA.shape[1]/4)
  
  process1 = mpc(target=corrLoop, args=(groupA.iloc[:,:divLen], groupB, result1))
  process2 = mpc(target=corrLoop, args=(groupA.iloc[:,divLen:divLen*2], groupB, result2))
  process3 = mpc(target=corrLoop, args=(groupA.iloc[:,divLen*2:divLen*3], groupB, result3))
  process4 = mpc(target=corrLoop, args=(groupA.iloc[:,divLen*3:], groupB, result4))
  
  procs = [process1, process2, process3, process4]
  
  # Start processes
  for p in procs:
    p.start()
  
  # Save results as variables
  res1 = result1.get()
  res2 = result2.get()
  res3 = result3.get()
  res4 = result4.get()
  
  # Close output queues
  result1.close()
  result2.close()
  result3.close()
  result4.close()
  
  # Close processes
  for p in procs:
    p.join()
  
  res = res1.join([res2, res3, res4])

fin_tm = dt.now()
elapsed = fin_tm - ini_tm

print(str(elapsed))
