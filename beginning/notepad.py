# commands
new_note = ''
view_note = ''
cmd = ''

# data
note1 = 'EMPTY - note something'
note2 = 'EMPTY - note something'
note3 = 'EMPTY - note something'
# Getting Input
get = ''
# help

print('''
new note - To make a new note
view note - to view previous note
''')
# main
while True:
    cmd = input('>>> ').lower()
    if cmd == 'new note':
        name = input('Give a name - note1/note2/note3 ').lower()
        get = input('Note something: ')
        if name == 'note2':
            note2 = get
        elif name == 'note3':
            note3 = get
        else:
            note1 = get
        print('Successfully Noted')
        # new note end
        # multiple new note cmd start
    elif cmd == 'new note/note1':
        get = input('Note something: ')
        note1 = get
        print('Noted Successfully')
    elif cmd == 'new note/note2':
        get = input('Note something: ')
        note2 = get
        print('Noted Successfully')
    elif cmd == 'new note/note3':
        get = input('Note something: ')
        note3 = get
        print('Noted Successfully')
    # multiple new note cmd end
    # clear note single start
    elif cmd == 'clear':
        clear_which = input('Which One? ').lower()
        if clear_which == 'note1' and note1 == 'EMPTY - note something':
            print('It is already empty')
        elif clear_which == 'note1':
            note1 = 'EMPTY - note something'
            print('Clear Successfully')
        elif clear_which == 'note2' and note2 == 'EMPTY - note something':
            print('It is already empty')
        elif clear_which == 'note2':
            note2 = 'EMPTY - note something'
            print('Clear Successfully')
        elif clear_which == 'note3' and note3 == 'EMPTY - note something':
            print('It is already empty')
        elif clear_which == 'note3':
            note3 = 'EMPTY - note something'
            print('Clear Successfully')
        elif clear_which == 'all':
            note1 = 'EMPTY - note something'
            note2 = 'EMPTY - note something'
            note3 = 'EMPTY - note something'
            print('Cleared All Successfully')
        else:
            print('no note found!')
    # view note single start
    elif cmd == 'view note':
        view_note_cmd = input('Which One? note1/note2/note3  ').lower()
        if view_note_cmd == 'note1' and note1 == 'EMPTY - note something':
            print('note something first!')
        elif view_note_cmd == 'note1':
            print(f'your note:  {note1}')
        elif view_note_cmd == 'note2' and note2 == 'EMPTY - note something':
            print('note something first!')
        elif view_note_cmd == 'note2':
            print(f'your note:  {note2}')
        elif view_note_cmd == 'note3' and note3 == 'EMPTY - note something':
            print('note something first!')
        elif view_note_cmd == 'note3':
            print(f'your note:  {note3}')
        else:
            print('no note found')
    # single cmd end
    # multiple view note cmd start
    # note1
    elif cmd == 'view note/note1':
        print(f'your note:  {note1}')
        # note2
    elif cmd == 'view note/note2':
        print(f'your note:  {note2}')
        # note3
    elif cmd == 'view note/note3':
        print(f'your note:  {note3}')
        # view note end
        # exit
    elif cmd == 'exit':
        break
        # error
    elif cmd == 'help':
        print('''
new note - To make a new note
view note - to view previous note
''')
    else:
        print('ERROR')
