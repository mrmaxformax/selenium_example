from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, title=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, email_first=None,
                 email_second=None, email_third=None, home_page=None, address2=None, bld_number=None, notes=None,
                 id=None, all_phones_from_home_page=None, all_mails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email_first = email_first
        self.email_second = email_second
        self.email_third = email_third
        self.home_page = home_page
        self.address2 = address2
        self.bld_number = bld_number
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.first_name is None or other.first_name is None or self.first_name == other.first_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
