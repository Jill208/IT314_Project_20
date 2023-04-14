from django_unicorn.components import UnicornView


class CreatecrosswordmanualView(UnicornView):
    title = ""
    description = ""
    rows: int = 0
    columns: int = 0
    grid = []
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', '_']
    activeChar = '_'
    activeStep = 1
    roadMapStatusLabel1 = ""
    roadMapStatusLabel2 = "Empty"
    roadMapStatusLabel3 = "Empty"
    roadMapStatusLabel4 = "Empty"
    roadMapStatusLabel5 = "Empty"

    def incrementStep(self):
        self.activeStep += 1
        if self.activeStep == 2:
            self.roadMapStatusLabel2 = ""
        if self.activeStep == 3:
            self.roadMapStatusLabel3 = ""
        if self.activeStep == 4:
            self.roadMapStatusLabel4 = ""
        if self.activeStep == 5:
            self.roadMapStatusLabel5 = ""

    def create_crossword(self):
        print(self.title)
        print(self.description)
        print(self.rows)
        print(self.columns)

    def set(self, height, width):
        self.rows = height
        self.columns = width

    def createGrid(self):
        gridRow = []
        self.grid = []
        print(type(self.rows))
        print(type(self.columns))

        if type(self.rows) != int:
            self.rows = int(self.rows)

        if type(self.columns) != int:
            self.columns = int(self.columns)

        print(type(self.rows))
        print(type(self.columns))

        for i in range(0, self.rows):
            for j in range(0, self.columns):
                gridRow.append('_')
            self.grid.append(gridRow)
            gridRow = []
        print(self.grid)

    def cellClicked(self, cell):
        rowIndex, colIndex = cell[0], cell[1]
        print("Cell clicked at: ", rowIndex, colIndex)
        self.grid[rowIndex][colIndex] = self.activeChar

    def setActiveChar(self, clickChar):
        print("Active char: ", clickChar)
        self.activeChar = clickChar
        print("Active char: ", self.activeChar)
