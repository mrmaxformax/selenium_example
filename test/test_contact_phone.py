__author__ = 'Max Terekhov'
import re
from random import randrange


# Test of all contact phones
def test_phones_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_phones_like_on_hp(contact_from_edit_page) == contact_from_home_page.all_phones_from_home_page


def test_phones_on_contact_view_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_edit_page.home_phone == contact_from_view_page.home_phone
    assert contact_from_edit_page.mobile_phone == contact_from_view_page.mobile_phone
    assert contact_from_edit_page.work_phone == contact_from_view_page.work_phone


# Test of names
def test_name_and_address_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    name_from_home_page = app.contact.get_contact_list()[index]
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert name_from_home_page.last_name == name_from_edit_page.last_name
    assert name_from_home_page.first_name == name_from_edit_page.first_name
    assert name_from_home_page.address == name_from_edit_page.address


def test_name_and_address_on_view_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    name_from_view_page = app.contact.get_contact_from_view_page(index)
    assert merge_names(name_from_edit_page) == clear(name_from_view_page.first_name)


# Test of e-mails
def test_mails_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    mails_from_home_page = app.contact.get_contact_list()[index]
    mails_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_mails(mails_from_edit_page) == mails_from_home_page.all_mails_from_home_page

# Help function
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.bld_number]))))

def merge_names(contact):
    return "".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.first_name, contact.middle_name, contact.last_name]))))

def merge_mails(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email_first, contact.email_second, contact.email_third]))))