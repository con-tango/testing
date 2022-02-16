def get_summ(one, two, delimiter='&'):
     return str(f'{one}{delimiter}{two}')

final_summ = get_summ('Learn', 'Python')
print(final_summ)
print(final_summ.upper())
