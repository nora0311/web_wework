from test_wework_selenium.page.contacts.contact import Contact
from test_wework_selenium.utils.data_name import DataName


class TestContact:

    def setup(self):
        self.contact = Contact(reuse=True)

    # 通讯录-添加成员-跳转到添加成员界面
    def test_add_member(self):
        name=DataName.data_name()
        acctid="99000"
        phone="13122990088"
        self.contact.goto_add_member().add_member_page(name,acctid,phone)


    def test_import_users(self):
       pass

