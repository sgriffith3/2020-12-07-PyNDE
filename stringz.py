first_string = "A 'String' within double quotes"
second_string = 'another \'string\' that just uses single quotes'
multi_line_string = '''
This
is a multi-
line string
that wraps.
'''
ma_doc_string = """THIS
IS
A
DOCSTING
"""
print(first_string, second_string, "An int is:", 23, "a float is:", 3.14, sep='&&')
print(second_string, end='\n\n\n')
print(second_string)
# print(multi_line_string)
# print(ma_doc_string)
