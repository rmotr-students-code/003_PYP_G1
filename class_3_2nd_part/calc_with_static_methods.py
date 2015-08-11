class Calculator(object):

    @classmethod
    def _perform_sum(cls, *args):
        return sum(args)

    @staticmethod
    def add(*args):
        # cls = ScientificCalculator
        Calculator._perform_sum(*args)

    @staticmethod
    def subtract(x, y):
        return x - y


class ScientificCalculator(Calculator):

    @classmethod
    def _perform_sum(cls, *args):
        return sum_with_precision(args)


ScientificCalculator.add(2, 3, 5)