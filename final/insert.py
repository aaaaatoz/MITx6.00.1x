def insert(atMe, newFrob):
    if atMe.myName() >= newFrob.myName():
        while atMe.getBefore():
            atMe = atMe.getBefore()
            if atMe.myName() >= newFrob.myName(): continue
            newFrob.setBefore(atMe)
            newFrob.setAfter(atMe.getAfter())
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
            return
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)
    else:
        while atMe.getAfter():
            atMe = atMe.getAfter()
            if atMe.myName() <= newFrob.myName(): continue
            newFrob.setAfter(atMe)
            newFrob.setBefore(atMe.getBefore())
            atMe.getBefore().setAfter(newFrob)
            atMe.setBefore(newFrob)
            return
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)
