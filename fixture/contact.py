__author__ = 'Max Terekhov'
import re
from model.model_contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and wd.find_element_by_id("maintable")):
            wd.find_element_by_link_text("home").click()

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field("firstname", contact.first_name)
        self.change_field("middlename", contact.middle_name)
        self.change_field("lastname", contact.last_name)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home_phone)
        self.change_field("mobile", contact.mobile_phone)
        self.change_field("work", contact.work_phone)
        self.change_field("fax", contact.fax_phone)
        self.change_field("email", contact.email_first)
        self.change_field("email2", contact.email_second)
        self.change_field("email3", contact.email_third)
        self.change_field("homepage", contact.home_page)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.bld_number)
        self.change_field("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    contact_cache =None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_mails_from_home_page=all_mails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()
        return wd

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name('selected[]')[index].click()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        middle_name = wd.find_element_by_name('middlename').get_attribute('value')
        address = wd.find_element_by_name('address').text
        id = wd.find_element_by_name('id').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        bld_number = wd.find_element_by_name('phone2').get_attribute('value')

        email_first = wd.find_element_by_name('email').get_attribute('value')
        email_second = wd.find_element_by_name('email2').get_attribute('value')
        email_third = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(first_name=first_name, middle_name = middle_name, last_name=last_name, address=address, id=id,
                       home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, bld_number=bld_number,
                       email_first=email_first, email_second=email_second, email_third=email_third)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        first_name = re.search('(.*)', text).group(1)
        first_name = re.search('(.*)', text).group(1)
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(first_name=first_name, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)