### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
    # This condition should be written as == 
      return True
    else
    # The else keyword needs a following :
      return False
   

  dif highest_card(self, card1 card2):
	  # There is a typo here: dif should be def. There should also be a comma between card1 & card2
  if card1.value > card2.value:
    # The entire if statement should be indented
    return card
		# card has not been defined
  else:
    return card2
  

# This definition should be indented
def cards_total(self, cards):
  total
	# total has not been defined
  for card in cards:
    total += card.value
    return "You have a total of" + total
		# This will give an error - we cannot concatenate a string and int.
    # The return statement should not be indented in the for loop
  
```
