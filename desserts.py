"""Dessert classes."""


class Cupcake():
    """A cupcake."""

    # To store all types of cupcake, by name
    cache = {}



    def __init__(self, name, flavor, price):
      """Cupcake object"""

      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0
      # Cupcake.cache[self.name] = Cupcake(name, flavor, price)


    def add_stock(self, amount):
      """Adjust inventory when baking a cupcake"""
 
      self.qty += amount


    def sell(self, amount):
      """Adjust inventory when selling a cupcake"""  

      if self.qty == 0:
        print("So sorry! There's no more of this cupcake available!")
      elif (self.qty - amount) < 0:
        self.qty = 0
        ## Should there be an added step, if ordering 10, but only 7 avail, to
        ## give partial orders?


    @staticmethod
    def scale_recipe(ingredients, amount):
      """Adjust ingredient list for different-sized batches"""

      scaled = [qty * amount for ingredient, qty in ingredients]

      return scaled


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
