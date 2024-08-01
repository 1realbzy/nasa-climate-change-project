import pandas as pd

dict = {
'country' : ['Brasil', 'Nigeria', 'China', 'Ghana'],
'population' : [200, 150, 1000, 50, ],
'area': [8.517, 5.356, 10.567, 3.98 ],
'capital': ['Brasília', 'Abuja', 'Beijing', 'Accra']
}

brics = pd.DataFrame(dict)
brics.index = ['BR', 'NG', 'CH', 'GH']

print(brics)
