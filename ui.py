class UI:
  def __init__(self):
    pass
  def divider(self):
    print('▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂')
  def divideret(self):
    return '▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂'
  def midt(self,text):
    print(f'[{text}]')
  def midtr(self,text):
    return f'[{text}]'

uitest = UI()

print(uitest.divider())