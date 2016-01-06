# -*- coding: utf-8 -*-
from model.model_contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Vasilius", middle_name="G", last_name="Pupkinus", title="King of hell", company="New company", address="Address address", home_phone="212-8506", mobile_phone="212-8507", work_phone="212-8508", fax_phone="212-8509", email_first="first@gmai.com", email_second="second@gmai.com", email_third="third@gmai.com", home_page="www.google.com",  address2="Lizukova str.", bld_number="22", notes="Test notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
