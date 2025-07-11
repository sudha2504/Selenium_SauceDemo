from lxml import etree

class PageWithListings:
    def __init__(self, page_source):
        self.tree = etree.HTML(page_source)

    def get_product_listings(self, based_on='item_name'):

        list_products = []

        if based_on == 'item_name':
            data = self.tree.xpath("//div[@class = 'inventory_item_name ']")
            for element in data:
                list_products.append(element.text)
        elif based_on == 'item_price':
            data = self.tree.xpath("//div[@class = 'inventory_item_price']")
            for element in data:
                list_products.append(float(element.text.replace("$", "")))

        print("Found {} products".format(list_products))
        return list_products

    def check_product_order(self, list_products, reverse=False):
        print(list_products)

        if list_products == sorted(list_products, reverse=reverse):
            return True
        else:
            return False

    def get_total_price_of_products_checkout(self):

        total_price = 0
        data = self.tree.xpath("//div[@class = 'inventory_item_price']")
        for element in data:
            total_price = float(element.text.replace("$", ""))+ total_price

        return total_price

    def get_price_details_checkout(self):

        price_details = {}
        for i in ['summary_subtotal_label','summary_tax_label','summary_total_label']:
            value = self.tree.xpath(f"//div[@class = '{i}']")
            price_details[i] = float(value[0].text.split("$")[1])

        return price_details
