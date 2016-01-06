__author__ = 'Max Terekhov'
from model.model_group import Group
from random import randrange


def test_del_group(app):
    if app.group.count == 0:
        app.group.change_field(Group(name=app.group.name_generator(), header="Header", footer="footer"))

    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    app.group.delete_by_index(index)
    assert len(old_group) - 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group[index:index+1] = []
    assert old_group == new_group