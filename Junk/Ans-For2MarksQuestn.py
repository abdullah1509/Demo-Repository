Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data = pd.read_csv("Olympic_Athlete.csv")
>>> print(f"Solution 1 : Average :- {data['Age'].mean()}")
Solution 1 : Average :- 26.405433646812956
>>> print(f"Solution 2 : Country with highest Athlete :- {data['Country'].value_counts().idxmax()}.")
Solution 2 : Country with highest Athlete :- United States.
>>> print(f"Solution 3 : Different sports count :- {len(data['Sport'].unique())}")
Solution 3 : Different sports count :- 49
>>> medals = data.groupby('Sport').agg({'Gold Medals': 'sum','Silver Medals': 'sum','Bronze Medals': 'sum'})
>>> totalMedals = medals['Gold Medals'].sum() + medals['Silver Medals'].sum() + medals['Bronze Medals'].sum()
>>> print(f"Solution 4 : Total medals won :- {totalMedals}")
Solution 4 : Total medals won :- 9529
>>> max_gold_winner = data.groupby('Sport')['Gold Medals'].sum()
>>> print(f"Solution 5 : Sport of highest gold medals :- {max_gold_winner.idxmax()}")
Solution 5 : Sport of highest gold medals :- Swimming
>>> medals_by_country = data.groupby('Country')['Total Medals'].sum()
>>> print(f"Solution 6 : Country wise medals:-\n{medals_by_country}")
Solution 6 : Country wise medals:-
Country
Afghanistan      2
Algeria          8
Argentina      141
Armenia         10
Australia      609
              ... 
Uruguay          1
Uzbekistan      19
Venezuela        4
Vietnam          2
Zimbabwe         7
Name: Total Medals, Length: 110, dtype: int64
>>> print(f"Solution 7 : Medals by Sports :-\n{medals}")

>>> print(f"Solution 8 : Correlation :- {data['Age'].corr(data['Total Medals'])}")
Solution 8 : Correlation :- -0.07235683052681496
