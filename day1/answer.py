
class Solver(object):
    """
    This is hec44 solution for the problem described on: https://adventofcode.com/2022/day/1
    Copy and paste the input on the file input.inp
    """

    @staticmethod
    def solve(input_file_name: str) -> int:
        """
        main function of the solver. Use it to calculate the highest total calories that an elf is carrying
        :param input_file_name: name of the input file that contains the input of the problem
        :return: the number of the highest total calories per elf
        """
        elf_calories = Solver.parse_input(input_file_name)
        highest_total_calories = 0
        current_total_calories = 0
        for carry in elf_calories:
            if carry == "":
                if current_total_calories > highest_total_calories:
                    highest_total_calories = current_total_calories
                current_total_calories = 0
            else:
                current_total_calories += int(carry)
        return highest_total_calories

    @staticmethod
    def parse_input(input_file_name: str) -> list[str]:
        """
        Simple help function that reads the input file and parses it to a list of strings
        :param input_file_name: file that we will read
        :return: list of strings, where each element of the array is a line in the input document
        """
        with open(input_file_name, "r") as file_buffer:
            input_lines = file_buffer.readlines()

        elf_calories = [line.strip() for line in input_lines]
        return elf_calories


if __name__ == '__main__':
    heavies_lift = Solver.solve("input.inp")
    print('jingle jingle')
    print(f'the heavies elf is carrying {str(heavies_lift)} apples.')
    print('jingle jingle')


