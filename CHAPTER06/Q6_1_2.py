class Person:
    def __int__(self, name="", nationality="", birth="", address=""):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいるところ:", self.address)


hero = Person("宮里", "日本", "2005", "沖縄県宜野湾市")
hero.show_attributes()
