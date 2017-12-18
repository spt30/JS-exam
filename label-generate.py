for i, var in enumerate(range(22)):
    # print('<input id="' +'tnum' + str(i) + '" type="radio" name="tasks-number">')
    # print('<label for="' + 'tnum' + str(i) + '">' + str(i) + '</label>')
    print('input[id=\'tnum' + str(i) + '\']:checked ~ ol .task' + str(i) + '\n{\n\tbackground-color: var(--bckgr);\n}')

