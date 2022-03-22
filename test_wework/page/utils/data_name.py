from faker import Faker


class DataName:

    @classmethod
    def data_name(cls):
        fake = Faker(locale='zh_CN')
        name = fake.word()
        return name
    # 随机手机号
