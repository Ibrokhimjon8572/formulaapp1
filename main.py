from chempionship import Chempionship
from driver import Driver
from timeform import TimeForm
from gp import GP

chempionship = Chempionship()

gp = GP('mers form')
driver = Driver('ali')
end_time = TimeForm(12, 45, 34, 123)
print(chempionship.set_time(gp, driver, end_time))

# print(chempionship.define_gp('ford form'))
# print(chempionship.get_gp('ford form'))
# print(chempionship.create_driver('ali'))
# print(chempionship.create_driver('vali'))
# print(chempionship.get_drivers())
# print(chempionship.get_driver('ali'))
