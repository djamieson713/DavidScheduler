class Patient:
    # the problems are in the form of a list
    def __init__(self, name ,age , problems):
        self.name = name
        self.age = age
        self.problems = problems

    def __str__(self):
        msg = self.name + " is " + str(self.age) + "  yrs. old with the following problems: "
        for problem in self.problems:
            msg = msg + " " + problem + ","
        return msg[0: len(msg)-1]





