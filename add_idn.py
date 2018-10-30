
import identifier


def add_idn(collection_records_idn, code, name, type):
    collection_records_idn.append(identifier.Identifier(code, name, type))


def show_idn(collection_records_idn):
    count = len(collection_records_idn)
    print(' ')
    print("---------------------------------------------")
    print("|            Table of identifier            |")
    print("---------------------------------------------")
    print("|  code  |         name        |    type    |")
    print("---------------------------------------------")
    for i in range(0, count):
        print("|   %-4i |         %-8s    |    %-5s   |" % (collection_records_idn[i].code,
                                                                     collection_records_idn[i].name,
                                                                     collection_records_idn[i].type))
        print("---------------------------------------------")

def findIDN(idn, collection_records_idn):
    count = len(collection_records_idn)
    for i in range(0, count):
        if collection_records_idn[i].name == idn:
            return collection_records_idn[i].code
    return None




def write(collection_records_idn):
    count = len(collection_records_idn)
    file = open('idn.txt', 'w')
    for i in range(0, count):
        file.write("   %-4i          %-8s        %-5s   \n" % (collection_records_idn[i].code,
                                                            collection_records_idn[i].name,
                                                            collection_records_idn[i].type))
    file.close()