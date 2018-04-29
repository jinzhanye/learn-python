# coding=utf-8
class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_local_element(self, key):
        pair = key.split('=')
        by = pair[0]
        by_value = pair[1]
        if by == 'id':
            return self.driver.find_element_by_id(by_value)
        elif by == 'name':
            return self.driver.find_element_by_name(by_value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(by_value)
        elif by == 'link':
            return self.driver.find_element_by_link_text(by_value)
        else:
            return self.driver.find_element_by_xpath(by_value)
