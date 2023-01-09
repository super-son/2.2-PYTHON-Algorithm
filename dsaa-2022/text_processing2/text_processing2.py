#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    """
    인풋으로 받는 스트링에서 숫자만 추출하여 영어 단어로 변환하여 단어들이 연결된 스트링을 반환함
    아래의 요건들을 충족시켜야함
    * 반환하는 단어들은 영어 소문자여야함
    * 단어들 사이에는 띄어쓰기 한칸이 있음
    * 만약 인풋 스트링에서 숫자가 존재하지 않는 다면, 빈 문자열 (empty string)을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
            ex - "Zip Code: 19104"

        Returns:
            digit_string (string): 위 요건을 충족시킨 숫자만 영어단어로 추출된 string
            ex - 'one nine one zero four'

        Examples:
            >>> import text_processing2 as tp2
            >>> digits_str1 = "Zip Code: 19104"
            >>> tp2.digits_to_words(digits_str1)
            'one nine one zero four'
            >>> digits_str2 = "Pi is 3.1415..."
            >>> tp2.digits_to_words(digits_str2)
            'three one four one five'
    """
    new_list = []
    output_list = []

    for i in range(len(input_string)):
        new_list.append(input_string[i])
    
    for i in new_list :
        if i == '0':
            output_list.append("zero")
        if i == '1':
            output_list.append("one")
        if i == '2':
            output_list.append("two")
        if i == '3':
            output_list.append("three")
        if i == '4':
            output_list.append("four")
        if i == '5':
            output_list.append("five")            
        if i == '6':
            output_list.append("six")
        if i == '7':
            output_list.append("seven")
        if i == '8':
            output_list.append("eight")
        if i == '9':
            output_list.append("nine")

    digit_string = " ".join(output_list)
    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    """
    이 문제에서 첫번째 규칙 'underscore variable' 에서 두번째 규칙 'camelcase variable'으로 변환함
    * 앞과 뒤에 여러개의 'underscore'는 무시해도 된
    * 만약 어떤 변수 이름이 underscore로만 이루어 진다면, 빈 문자열만 반환해도 됨

        Parameters:
            underscore_str (string): underscore case를 따른 스트링

        Returns:
            camelcase_str (string): camelcase를 따른 스트링

        Examples:
            >>> import text_processing2 as tp2
            >>> underscore_str1 = "to_camel_case"
            >>> tp2.to_camel_case(underscore_str1)
            "toCamelCase"
            >>> underscore_str2 = "__EXAMPLE__NAME__"
            >>> tp2.to_camel_case(underscore_str2)
            "exampleName"
            >>> underscore_str3 = "alreadyCamel"
            >>> tp2.to_camel_case(underscore_str3)
            "alreadyCamel"
    """
    new_list2 = []
    output_list2 = []

    for i in range(len(underscore_str)):
        new_list2.append(underscore_str[i])

    for idx,i in enumerate(new_list2):
        if i != "_" :
            if i.isupper():
                if new_list2[idx-1].isupper() :
                    output_list2.append(i.lower())
                else :
                    output_list2.append(i.upper())
               
            else :
                if new_list2[idx-1] == "_" :          
                    output_list2.append(i.upper())
                else :
                    output_list2.append(i.lower())

    if output_list2 != []:
        output_list2[0] = output_list2[0].lower()
        
    camelcase_str = "".join(output_list2)
    return camelcase_str


ex = "Zip Code: 19104"
if __name__ == "__main__":
    result = digits_to_words(ex)
    print(result)

ex2 = "to_camel_case"
ex3 = "exampleName"
ex4 = "alreadyCamel"
ex5 = "________"

if __name__ == "__main__":
    result2 = to_camel_case(ex2)
    result3 = to_camel_case(ex3)
    result4 = to_camel_case(ex4)
    result5 = to_camel_case(ex5)
    print(result2, "toCamelCase")
    print(result3, "exampleName")
    print(result4, "alreadyCamel")
    print(result5, "alreadyCamel")