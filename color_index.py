'''
colors = ('white', 'red', 'blue', 'yellow')
mixed_colors = ['white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow']
first_color = input('Enter one of: ' + str(colors))
second_color = input('Enter one of: ' + str(colors))
first_index = colors.index(first_color)
second_index = colors.index(second_color)
if first_index == 0:
  mix_index = second_index*second_index
elif second_index == 0:
  mix_index = first_index*first_index
else:
  mix_index = first_index*second_index
mix_color = mixed_colors[mix_index]
print(first_color, '+', second_color, '=', mix_color)
'''
# using Def:
def mix(index1, index2):
  colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
  if index1 == 0:
      mix_index = index2*index2
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]
  return mix_color
def main():
  colors = ('white', 'red', 'blue', 'yellow')
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()