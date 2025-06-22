### Challenges I faced for day 35(creating list maker):

#### INDEXING THE LIST


**Challenge**: List[] doesn't accept variables in it. I used a for loop but I ended up having 'i' variable being used once as an input and once as a variable created by for loop. Obviously, when I started the for loop it didn't recognise 'i' as input but rather as variable in range (len(List)).

**Result**: Whenever I tried to edit the list, it always ended up editing the first item in the list. 

**Solution**: I created a subroutine with 'i' as a parameter. And that 'i' was a defined integer by the user as per their wishes.

