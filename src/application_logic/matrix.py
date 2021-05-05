import random

def generate_matrix(size):
    """Metodi, joka luo uuden matriisin, jossa on määritelty, mitä numeroita
       on missäkin neliössä

    Attributes:
        size: Kertoo kuinka monta riviä ja saraketta matriisissa on

    Returns:
        Juuri luotu matriisi, joka toteuttaa halutut ehdot
    """
    while True:
        amounts = {}
        amounts[0] = 0
        amounts[1] = 0
        amounts[2] = 0
        amounts[3] = 0
        matrix = [[]]*size
        for y_variable in range(size):
            row = []
            x_variable = 0
            while x_variable < size:
                number = random.randint(0, 3)
                amounts[number] += 1
                row.append(number)
                x_variable += 1
            matrix[y_variable] = row
        if amounts[0] <= 7 and amounts[3]+amounts[2] <= 6 and amounts[0] >= 5 \
			and amounts[3] >= 1 and amounts[3] <= 3:
            return matrix
