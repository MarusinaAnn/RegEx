import re
from pprint import pprint
import csv

PHONE_PATTERN = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
SUBS_PHONE = r'+7(\3)\6-\8-\10 \12\13'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# пункты 1-3 ДЗ

def phonebook(contacts_list: list):
    new_contacts_list = list()
    for cont in contacts_list:
        full_name = ' '.join(cont[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], cont[3], cont[4],
                  re.sub(PHONE_PATTERN, SUBS_PHONE, cont[5]),
                  cont[6]]
        new_contacts_list.append(result)
    return combine_info(new_contacts_list)


def combine_info(contacts: list):
    for contact in contacts:
        name = contact[0]
        surname = contact[1]
        for new_contact in contacts:
            new_name = new_contact[0]
            new_surname = new_contact[1]
            if name == new_name and surname == new_surname:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list

# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(phonebook(contacts_list))