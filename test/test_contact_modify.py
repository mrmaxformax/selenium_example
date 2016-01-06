__author__ = 'Max Terekhov'
from model.model_contact import Contact
from random import randrange
from datetime import datetime


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.change_field(Contact(first_name="Vasilius", middle_name="G", last_name="Pupkinus", title="King of hell", company="New company", address="Address address", home_phone="212-8506", mobile_phone="212-8507", work_phone="212-8508", fax_phone="212-8509", email_first="first@gmai.com", email_second="second@gmai.com", email_third="third@gmai.com", home_page="www.google.com", byear="1999", ayear="2012", address2="Lizukova str.", bld_number="22", notes="Test notes"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    new_name = old_contacts[index].last_name + (" NEW %s" % datetime.now())
    contact = Contact(last_name=new_name)
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

