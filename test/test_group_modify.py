__author__ = 'Max Terekhov'
from model.model_group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group.count == 0:
        app.group.change_field(Group(name=app.group.name_generator(), header="Header", footer="footer"))

    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    group = Group(name="New funny group")
    group.id = old_group[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)