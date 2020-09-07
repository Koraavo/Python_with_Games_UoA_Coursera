'''
for i in range(1, 6):
    print("#" * i)
for i in range(6, 0, -1):
    print("#" * i)
'''

'''
<st trying to match if 'COOKIES'.isupper: newline indent 'milk' newline dedent
  <cs trying to match if 'COOKIES'.isupper: newline indent 'milk' newline dedent
    <if trying to match if 'COOKIES'.isupper: newline indent 'milk' newline dedent
      <ex trying to match 'COOKIES'.isupper
        <ar trying to match 'COOKIES'
          <ex trying to match 'COOKIES'
          ex>@li matches 'COOKIES
        ar>@id matches 'COOKIES'.isupper
      ex>@ar matches 'COOKIES'.isupper
      <su trying to match newline indent 'milk' newline dedent
        <st trying to match 'milk' newline
          <ss trying to match 'milk'
            <es trying to match 'milk'
              <ex trying to match 'milk'
              ex>@li matches 'milk'
            es>@ex matches 'milk'
          ss>@es matches 'milk'
        st>@nl matches 'milk' newline
      su>@de matches newline indent 'milk' newline dedent
    if>@su matches newline indent 'milk' newline dedent
  cs>@if matches if 'COOKIES'.isupper: newline indent 'milk' newline dedent
st>@cs matches if 'COOKIES'.isupper: newline indent 'milk' newline dedent  
'''

'''
<if starting if age >= 18: school = 'university of alberta'.title()
  <be starting age >= 18
    <id> evaluated age to get int 20
    <li> evaluated 18 to get int 18
  be> evaluated age >= 18 to get bool true
  <su starting school = 'university of alberta'.title()
    <as starting school = 'university of alberta'.title()
      <fc starting 'university of alberta'.title()
        <ar starting 'university of alberta'.title
          <li> evaluated 'university of alberta' to get str university of alberta
        ar> evaluated 'university of alberta'.title to get function title
      fc> evaluated 'university of alberta'.title() to get str University Of Alberta
    as> evaluated school = 'university of alberta'.title()
  su> evaluated school = 'university of alberta'.title()
'''
'''
if done:
    42
    hello
else:
    'bye'


<st trying to match if done: newline indent 42 newline hello newline dedent else: newline indent 'bye' newline dedent
  <cs trying to match if done: newline indent 42 newline hello newline dedent else: newline indent 'bye' newline dedent
    <if trying to match if done: newline indent 42 newline hello newline dedent else: newline indent 'bye' newline dedent
      <ex trying to match done
      ex>@id matches done
      <su trying to match newline indent 42 newline hello newline dedent
        <st trying to match 42 newline
          <ss trying to match 42
            <es trying to match 42
              <ex trying to match 42
              ex>@li matches 42
            es>@ex matches 42
          ss>@es matches 42
        st>@nl matches 42 newline
        <st trying to match hello newline
          <ss trying to match hello
            <es trying to match hello
              <ex trying to match hello
              ex>@id matches hello
            es>@ex matches hello
          ss>@es matches hello
        st>@nl matches hello newline
      su>@de matches newline indent 42 newline hello newline dedent
      <su trying to match newline indent 'bye' newline dedent
        <st trying to match 'bye' newline
          <ss trying to match 'bye'
            <es trying to match 'bye'
              <ex trying to match 'bye'
              ex>@li matches 'bye'
            es>@ex matches 'bye'
         ss>@es matches 'bye'
        st>@nl matches 'bye' newline
      su>@de matches newline indent 'bye' newline dedent
    if>@su matches if done: newline indent 42 newline hello newline dedent else: newline indent 'bye' newline dedent
  cs>@if matches if done: newline indent 42 newline hello newline dedent else: newline indent 'bye' newline dedent
st>@cs matches if done: newline indent 42 newline hello newline dedent else: newline indent 'bye' newline dedent
'''

'''
<if starting if 1 == 'one': print('Hello!') elif 5 <= cartoon: print("That's all folks!")
  <be starting 1 == 'one'
    <li> evaluated 1 to get int 1
    <li> matched 'one' to get str one
  be> evaluated 1 == 'one' to get bool false
  <be starting 5 <= cartoon
    <li> evaluated 5 to get int 5
    <id> evaluated cartoon to get int 6
  be> matched 5 <= cartoon to get bool true
  <su starting print("That's all folks!")
    <fc starting print("That's all folks!")
      <id> evaluated print to get function print
      <al starting "That's all folks!"
        <li> evaluated "That's all folks!" to get str That's all folks!
      al> evaluated "That's all folks!" to get argument object list
    fc> evaluated print("That's all folks!") to display str That's all folks!
  su> evaluated print("That's all folks!")
'''
'''
for sock in hamper:
	wash_sock()

<st trying to match for sock in hamper: newline indent wash_sock() newline dedent
  <cs trying to match for sock in hamper: newline indent wash_sock() newline dedent
    <fs trying to match for sock in hamper: newline indent wash_sock() newline dedent
      <ex trying to match hamper
      ex>@id matches hamper
      <su trying to match newline indent wash_sock() newline dedent
        <st trying to match wash_sock() newline
          <ss trying to match wash_sock()
            <es trying to match wash_sock()
              <ex trying to match wash_sock()
                <fc trying to match wash_sock()
                  <ex trying to match wash_sock
                  ex>@id matches wash_sock
                fc>@rp matches wash_sock()
              ex>@fc matches wash_sock()
            es>ex matches wash_sock()
          ss>@es matches wash_sock()
        st>@nl matches wash_sock() newline
      su>@de matches newline indent wash_sock() newline dedent
    fs>@su matches for sock in hamper: newline indent wash_sock() newline dedent
  cs>@fs matches for sock in hamper: newline indent wash_sock() newline dedent
st>@cs matches for sock in hamper: newline indent wash_sock() newline dedent

for x in paint:
    print(x)
<fs starting for x in paint: print(x)
  <id> evaluated paint to get list ['red', 'white']
  <su starting print(x) with x bound to str red
    <fc starting print(x)
      <id> evaluated print to get function print
      <al starting x
        <id> evaluated x to get str red
      al> evaluated x to get argument object list
    fc> evaluated print(x) to display str red
  su> evaluated print(x)
  <su starting print(x) with x bound to str white
    <fc starting print(x)
      <id> evaluated print to get function print
      <al starting x
        <id> evaluated x to get str white
      al> evaluated x to get argument object list
    fc> evaluated print(x) to display str white
  su> evaluated print(x)
fs> evaluated for x in paint: print(x)

<st trying to match while True: newline indent y = False newline dedent
  <cs trying to match while True: newline indent y = False newline dedent
    <ws trying to match while True: newline indent y = False newline dedent
      <ex trying to match True
      ex>@li matches True
      <su trying to match newline indent y = False newline dedent
        <st trying to match y = False newline
          <ss trying to match y = False
            <as trying to match y = False
              <ta trying to match y
              ta>@id matches y
              <ex trying to match False
              ex>@li matches False
            as>@ex matches y = False
          ss>@as matches y = False
        st>@nl matches y = False newline
      su>@de matches newline indent y = False newline dedent
    ws>@su matches while True: newline indent y = False newline dedent
  cs>@ws matches while True: newline indent y = False newline dedent
st>@cs matches while True: newline indent y = False newline dedent


<ws starting while x < 2: x = -x
  <be starting x < 2
    <id> evaluated x to get int -4
    <li> evaluated 2 to get int 2
  be> evaluated x < 2 to get bool true
  <su starting x = -x
    <ai starting x = -x
      <ue starting -x
        <id> evaluated x to get int -4
      ue> evaluated -x to get int 4
    ai> evaluated x = -x
  su> evaluated x = -x
  <be starting x < 2
    <id> evaluated x to get int 4
    <li> evaluated 2 to get int 2
  be> evaluated x < 2 to get bool false
'''
'''
def hello():
    'Hello!'
hello()


<st trying to match def hello(): newline indent 'Hello!' newline dedent
  <cs trying to match def hello(): newline indent 'Hello!' newline dedent
    <fd trying to match def hello(): newline indent 'Hello!' newline dedent
      <su trying to match newline indent 'Hello!' newline dedent
        <st trying to match 'Hello!' newline
          <ss trying to match 'Hello!'
            <es trying to match 'Hello!'
              <ex trying to match 'Hello!'
              ex>@li matches 'Hello!'
            es>@ex matches 'Hello!'
          ss>@es matches 'Hello!'
        st>@nl matches 'Hello!' newline
      su>@de matches newline indent 'Hello!' newline dedent
    fd>@su matches def hello(): newline indent 'Hello!' newline dedent
  cs>@fd matches def hello(): newline indent 'Hello!' newline dedent
st>@cs matches def hello(): newline indent 'Hello!' newline dedent
<st trying to match hello() newline
  <ss trying to match hello()
    <es trying to match hello()
      <ex trying to match hello()
        <fc trying to match hello()
          <ex trying to match hello
          ex>@id matches hello
        fc>@rp matches hello()
      ex>@fc matches hello()
    es>@ex matches hello()
  ss>@es matches hello()
st>@nl matches hello() newline

'''
'''
def fox():
	print('in socks')

fox()

<fd> evaluated def fox(): print('in socks')
<fc starting fox()
  <id> evaluated fox to get function fox
  <su starting print('in socks')
    <fc starting print('in socks')
      <id> evaluated print to get function print
      <al starting 'in socks'
        <li> evaluated 'in socks' to get str in socks
      al> evaluated 'in socks' to get argument object list
    fc> evaluated print('in socks') to display str in socks
  su> evaluated print('in socks')
'''

'''
def two_things(thing_one, thing_two):
    shake_hands()

<st trying to match def two_things(thing_one, thing_two): newline indent shake_hands() newline dedent
  <cs trying to match def two_things(thing_one, thing_two): newline indent shake_hands() newline dedent
    <fd trying to match def two_things(thing_one, thing_two): newline indent shake_hands() newline dedent
      <pl trying to match thing_one, thing_two
      pl>@id matches thing_one, thing_two
      <su trying to match newline indent shake_hands() newline dedent
        <st trying to match shake_hands() newline
          <ss trying to match shake_hands()
            <es trying to match shake_hands()
              <ex trying to match shake_hands()
                <fc trying to match shake_hands()
                  <ex trying to match shake_hands
                  ex>@id matches shake_hands
                fc>@rp matches shake_hands()
              ex>@fc matches shake_hands()
            es>@ex matches shake_hands()
          ss>@es matches shake_hands()
        st>@nl matches shake_hands() newline
      su>@de mathes newline indent shake_hands() newline dedent
    fd>@su matches def two_things(thing_one, thing_two): newline indent shake_hands() newline dedent
  cs>@fd matches def two_things(thing_one, thing_two): newline indent shake_hands() newline dedent

'''
'''

def multiply(x,y):
	print(x * y)

multiply(2,3)

<fd> evaluated def multiply(x,y): print(x * y)
<fc starting multiply(2,3)
  <id> evaluated multiply to get function multiply
  <al starting 2, 3
    <li> evaluated 2 to get int 2
    <li> evaluated 3 to get int 3
  al> evaluated 2, 3 to get argument object list
  <su starting print(x * y)
    <fc starting print(x * y)
      <id> evaluated print to get function print
      <al starting x * y 
        <be starting x * y
          <id> evaluated x to to get int 2 
          <id> evaluated y to to get int 3
        be> evaluated x * y to get int 6
      al> evaluated x * y to get argument object list
    fc> evaluated print(x * y) to display int 6
  su> evaluated print(x * y)

'''

'''
def horton_hears():
	return 'a who'

x = horton_hears()


<ai starting x = horton_hears()
  <fc starting horton_hears()
    <id> evaluated horton_hears to get function horton_hears
    <su starting return 'a who'
      <rs starting return 'a who'
        <li> evaluated 'a who' to get str a who
      rs> evaluated return 'a who' to get str a who
    su> evaluated return 'a who'
  fc> evaluated horton_hears()

'''

'''
def watch_movie(film):
  return actors

<st trying to match def watch_movie(film): newline indent return actors newline dedent
  <cs trying to match def watch_movie(film): newline indent return actors newline dedent
    <fd trying to match def watch_movie(film): newline indent return actors newline dedent
      <pl trying to match film
      pl>@id matches film
      <su trying to match newline indent return actors newline dedent
        <st trying to match return actors newline
          <ss trying to match return actors
            <rs trying to match return actors
              <ex trying to match actors
              ex>@id matches actors
            rs>@ex matches return actors
          ss>@rs matches return actors
        st>@nl matches return actors newline
      su>@de matches newline indent return actors newline dedent
    fd>@su matches def watch_movie(film): newline indent return actors newline dedent
  cs>@fd matches def watch_movie(film): newline indent return actors newline dedent
st>@cs matches def watch_movie(film): newline indent return actors newline dedent
'''

def horton_hears():
	return 'a who'

x = horton_hears()
