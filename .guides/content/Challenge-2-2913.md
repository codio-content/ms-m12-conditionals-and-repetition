You are going to write the same program you just did with the `For` loop but as a `while` loop.  So you will still be printing out the sale price every week but your loop structure will be a `while` loop.  

Do not forget you need to give your loop variable a number to start with and increment it inside the loop. 



{Run}(python3 .guides/content/Test4.py)

*Since this does not grade itself please advise your teacher when completed and they can review your final program.* 

|||guidance
To view your students work see [Viewing Student Code](https://codio.com/docs/teacher/assess/studentcode/)
#Solution (many other ways of doing it)

```python
i = 1
while i < 5:
    print("Price week ",i,"  $", price - (price * (i*.20)))
    i = i + 1
```
|||