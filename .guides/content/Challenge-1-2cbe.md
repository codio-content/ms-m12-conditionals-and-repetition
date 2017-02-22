Write a program that starts with a 20 dollar item. Each of the next 4 weeks the price goes down by 20 more percent off the original price.

Example: 

- week 1 it is 20% off
- week 2 it is 40% off
- week 3 it is 60% off
- week 4 it is 80% off

Write a `for` loop that will handle printing out the sale price each week. 


{Run}(python3 .guides/content/Test3.py)

*Since this does not grade itself please advise your teacher when completed and they can review your final program.*

|||guidance
To view your students work see [Viewing Student Code](https://codio.com/docs/teacher/assess/studentcode/)

#Solution (many other ways of doing it)

```python
price = 20.00

for i in range(1,5):
		print("Price week ",i,"  $", price - (price * (i*.20)))
```
|||