def is_validate_dom(dom_text : str) -> bool:
    checking_stack = []
    counter = 0
    data = list(dom_text.strip())
    while counter < len(data):
        checking_text = data[counter]

        if checking_text == '<':
            checking_text_list = []
            while checking_text != '>':
                checking_text_list.append(checking_text)
                counter += 1
                checking_text = data[counter]
            checking_text_list.append(checking_text)
            value = ''.join(checking_text_list)
            if 'item name=' in value:
                value = '<item>'
            if '/' in value and checking_stack != []:
                if checking_stack[-1].replace('<','</') == value:
                    checking_stack.pop()
                    counter -= 1
                else:
                    return False
            else:
                checking_stack.append(value)
        if checking_text in [' ', '\n']:
            counter += 1
            checking_text = data[counter]
            continue


        
        counter += 1     

    if '<' not in dom_text:
            return False

    if checking_stack != []:
        return False
    
    return True