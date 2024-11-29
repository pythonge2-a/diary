 4532  cd panda-demo
 4533  python3 -mvenv venv
 4534  ls -al
 4535  source venv/bin/activate
 4536  which python
 4537  pip install pandas
 4538  history
 4539  pip install ipython numpy matplotlib
 4540  pip freeze
 4541  ipython


import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df
hist
