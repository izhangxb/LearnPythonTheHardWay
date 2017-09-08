formater = "%r %r %r %r"
print formater % (1, 2, 3, 4)
print formater % ('one', 'two', 'three', 'four')
print formater % (True, False, True, True)
print formater % (formater, formater, formater, formater)
print formater % (
    "i had this thing",
    "that you could type up right",
    "but it didnot sing",
    "so i said goodnight"
)
