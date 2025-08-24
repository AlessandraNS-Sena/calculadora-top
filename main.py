# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
import unittest

# Teste manual (apenas imprime o resultado da função)
print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Classe de testes
class TestMeanVarStd(unittest.TestCase):

    def test_calculate_correct(self):
        result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0],
                     [1.0, 4.0, 7.0],
                     4.0],
            'variance': [[6.0, 6.0, 6.0],
                         [0.6666666666666666,
                          0.6666666666666666,
                          0.6666666666666666],
                         6.666666666666667],
            'standard deviation': [[2.449489742783178,
                                    2.449489742783178,
                                    2.449489742783178],
                                   [0.816496580927726,
                                    0.816496580927726,
                                    0.816496580927726],
                                   2.581988897471611],
            'max': [[6, 7, 8],
                    [2, 5, 8],
                    8],
            'min': [[0, 1, 2],
                    [0, 3, 6],
                    0],
            'sum': [[9, 12, 15],
                    [3, 12, 21],
                    36]
        }
        self.assertEqual(result, expected)

    def test_calculate_invalid_list(self):
        with self.assertRaises(ValueError) as context:
            mean_var_std.calculate([1, 2, 3])  # lista inválida
        self.assertEqual(str(context.exception), "List must contain nine numbers.")


# Run unit tests automatically
if _name_ == "_main_":
    unittest.main()
