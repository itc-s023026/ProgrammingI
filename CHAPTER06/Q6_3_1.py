class Katsuo(Nigiri):
    top = "カツオ"
    topping = "生姜とネギ"
    price = 100

    def my_list(self):
        super().my_list()
        print("topping: {}".format(self.topping))


k1 = Katsuo()
k1.my_list
