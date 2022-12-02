
class Solver(object):
    """
    This is hec44 solution for the problem described on: https://adventofcode.com/2022/day/2
    Copy and paste the input on the file input.inp
    """

    def __init__(self):
        """
        I saved all the possible outcomes of the match in a dictionary as keys and the match score as a result.
        """
        self.match_score = {}
        self.match_score['AY'] = 8
        self.match_score['AX'] = 4
        self.match_score['AZ'] = 3
        self.match_score['BY'] = 5
        self.match_score['BX'] = 1
        self.match_score['BZ'] = 9
        self.match_score['CY'] = 2
        self.match_score['CX'] = 7
        self.match_score['CZ'] = 6

    def solve(self, input_file_name: str) -> int:
        """
        main function of the solver. Use it to calculate the highest total calories that an elf is carrying
        :param input_file_name: name of the input file that contains the input of the problem
        :return: the total score of the rock paper scissor tournament
        """
        match_predictions = Solver.parse_input(input_file_name)
        total_score = 0
        for match_prediction in match_predictions:
            total_score += self.match_score[match_prediction]
        return total_score

    @staticmethod
    def parse_input(input_file_name: str) -> list[str]:
        """
        Simple help function that reads the input file and parses it to a list of strings
        :param input_file_name: file that we will read
        :return: list of strings, where each element of the array is a line in the input document,
                  plus we remove empty spaces
        """
        with open(input_file_name, "r") as file_buffer:
            input_lines = file_buffer.readlines()

        elf_calories = [line.strip().replace(" ", "") for line in input_lines]
        return elf_calories


if __name__ == '__main__':
    solver = Solver()
    total_score = solver.solve("input.inp")
    print('jingle jingle')
    print(f'the total score of your tournament activity is: {str(total_score)}')
    print('jingle jingle')