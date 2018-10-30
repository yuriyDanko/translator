
import constant


def add_con(collection_records_con, code, name, type):
    collection_records_con.append(constant.Constant(code, name, type))


def show_con(collection_records_con):
    count = len(collection_records_con)
    print(' ')
    print("---------------------------------------------")
    print("|             Constant table                |")
    print("---------------------------------------------")
    print("|  code  |         name        |    type    |")
    print("---------------------------------------------")
    for i in range(0, count):
        print("|   %-4i |         %-8s    |    %-5s   |" % (collection_records_con[i].code,
                                                            collection_records_con[i].name,
                                                            collection_records_con[i].type))
        print("---------------------------------------------")


def type_con(con):
    if con.find('.') != -1:
        return 'float'
    return 'int'

def write(collection_records_con):
    count = len(collection_records_con)
    file = open('constants.txt', 'w')
    for i in range(0, count):
        file.write("   %-4i          %-8s        %-5s   \n" % (collection_records_con[i].code,
                                                            collection_records_con[i].name,
                                                            collection_records_con[i].type))
    file.close()
