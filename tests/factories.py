import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from .models import Product, Category  # Adjust the import path according to your project structure

class ProductFactory(factory.Factory):
    """Creates fake products for testing."""
    class Meta:
        """Maps factory to the Product data model."""
        model = Product

    # Sequential ID for each product instance
    id = factory.Sequence(lambda n: n)

    # Random product name from a predefined list of choices
    name = FuzzyChoice(
        choices=[
            "Hat",
            "Pants",
            "Shirt",
            "Apple",
            "Banana",
            "Pots",
            "Towels",
            "Ford",
            "Chevy",
            "Hammer",
            "Wrench"
        ]
    )

    # Fake text for product description
    description = factory.Faker("text")

    # Random price within the specified range, with two decimal places
    price = FuzzyDecimal(0.5, 2000.0, 2)

    # Randomly available or not
    available = FuzzyChoice(choices=[True, False])

    # Random category from a predefined list of choices
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )
