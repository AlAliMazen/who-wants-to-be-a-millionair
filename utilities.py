

def split_list(list, single_question):
    """
    for making sublist of the big questions list
    """
    return [list[i:i + single_question] for i in range(0, len(list), single_question)]


def read_file(file):
    """
    reading the content of  txt file which contains the questions
    and return a list of lists from the questions
    """
    print( "Reading questions")
    content=[]
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            content.append(line.strip())  # Stripping '\n' character from each line
        
        questions=split_list(content,6)
        return questions
