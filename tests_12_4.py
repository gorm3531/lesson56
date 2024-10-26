import logging
import RunnerTest as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            logging.info(f'"test_walk" выполнен успешно')
            runner1 = rt.Run.Runner('Alice', speed=-1)
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
        except ValueError as vl:
            logging.warning("Неверная скорость для Runner")


    def test_run(self):
        try:
            logging.info(f'"test_run" выполнен успешно')
            runner2 = rt.Run.Runner(5.2341)
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
        except TypeError as type_:
            logging.warning("Неверный тип данных для объекта Runner")







logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s !|! %(levelname)s !|! %(message)s')

