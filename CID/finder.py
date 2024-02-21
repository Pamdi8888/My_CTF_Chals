# Make sure you download the updated version of gedcompy from GitHub which is not available on pip
import gedcom

file = gedcom.parse("MogamBro_Investigation.ged")


def men_w_many_wives():
    personlist = []
    # Iterate through all individuals
    for i in file.individuals:
        if i.sex == 'M':
            templist = []
            for k in i.child_elements:
                templist.append(k.tag)
            # print(templist)
            wife_count = templist.count('FAMS')
            # print(f"No of Wives = {wife_count}")
            if wife_count > 3:
                print(i.name)
                print(wife_count)
                personlist.append(i.name)
                # print(personlist)
    print(len(personlist))


def men_with_ten_children():
    personlist = []
    famlist = []
    for i in file.families:
        # print(i)
        child_count = 0
        # print(i.child_elements)
        for k in i.child_elements:
            # print(k.tag)
            if k.tag == 'CHIL':
                child_count += 1
        if child_count == 10:
            famlist.append(i.id)
            personlist.append(i.husbands[0].as_individual().name)
    # print(famlist)
    # print(len(famlist))
    print(personlist)


def women_with_6_daughters():
    personlist = []
    for i in file.families:
        # print(i)
        child_count = 0
        # print(i.child_elements)
        for k in i.child_elements:
            if k.tag == 'CHIL' and file.__getitem__(k.value).sex == 'F':
                # print(k)
                # print(file.__getitem__(k.value).name)
                child_count += 1
        if child_count == 6:
            personlist.append(i.wives[0].as_individual().name)
    print(personlist)
    print(len(personlist))


def birthday_on_30_oct():
    for i in file.individuals:
        try:
            if "30 OCT" in i.birth.child_elements[0].value:
                print(i.name)
        except:
            pass
