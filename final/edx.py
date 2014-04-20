class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x"):
        #   fill in code to set the grade
        for internalCourse in self.myCourses:
            if course == internalCourse.courseName:
                internalCourse.setGrade(grade)

    def getGrade(self, course="6.02x"):
        #   fill in code to get the grade
        for internalCourse in self.myCourses:
            if course == internalCourse.courseName:
                return internalCourse.getGrade()
        return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        for internalCourse in self.myCourses:
            if course == internalCourse.courseName:
                internalCourse.setPset(pset,score)

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        for internalCourse in self.myCourses:
            if course == internalCourse.courseName:
                return internalCourse.getPset(pset)
        return -1
