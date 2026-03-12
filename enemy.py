class enemy:
  #name = 'goblin'
  def __init__(self,health,name,damage):
    self.health = health
  def info(self):
    return f"Health {self.health}"

class goblin(enemy):
  def stab(self):
    stab=True



g1 = goblin(10,'goblin',1)
g1.info()

