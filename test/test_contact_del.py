# -*- coding: utf-8 -*-
from model.model_contact import Contact
from random import randrange

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.change_field(Contact(first_name="Vasilius", middle_name="G", last_name="Pupkinus", title="King of hell", company="New company", address="Address address", home_phone="212-8506", mobile_phone="212-8507", work_phone="212-8508", fax_phone="212-8509", email_first="first@gmai.com", email_second="second@gmai.com", email_third="third@gmai.com", home_page="www.google.com", byear="1999", ayear="2012", address2="Lizukova str.", bld_number="22", notes="Test notes"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts