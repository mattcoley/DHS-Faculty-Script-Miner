__author__ = 'mattcoley'

import urllib2
import sys
response = urllib2.urlopen('http://www.darienps.org/dhs/cms/index2.php?option=com_content&view=article&id=66&Itemid=248')
html = response.read()

cut = html.index('<td style="border-bottom-width: 1px; color: #0000ff; padding: 6px 8px;" align="center" valign="top">Department</td>')
html = html[cut + 150:]


#Loop through the table
while html.__len__() > 1500:
    val = 'valign="top">'
    start = html.index(val) + val.__len__()
    html = html[start:]
    val = '</td>'
    temp = html[:html.index(val)]

    link = ""
    firstName = ""
    lastName = ""
    email = ""
    phone = ""
    office = ""
    department = ""
    special = ""


    #TO GET THE LINKS AND LAST NAME
    if temp[0] == '<':
        if temp[1] == 'a':
            val = 'href="'
            beg = temp.index(val) + val.__len__()
            end = temp.index('"', beg + 1, temp.__len__())
            link = temp[beg:end]
            if link[0] == '/':
                link = "http://darienps.org" + link

            start = end + 2;
            end = temp.index('<', start, temp.__len__())
            lastName = temp[start:end]


        if temp[1] == 's':
            link = ''
            val = 'pan style="color: #0000ff;">'
            beg = temp.index(val) + val.__len__()
            end = temp.index('<', beg + 1, temp.__len__())
            lastName = temp[beg:end]

            html = html[val.__len__():]
    else:
        lastName = temp + ""

    #TO GET THE FIRST NAME
    val = 'valign="top">'
    end = '</td>'

    html = html[html.index(val) + val.__len__():]
    if html[0:5] == '<span':
        val = '#0000ff;">'
        html = html[html.index(val) + val.__len__():]
        end = '</span>'

    temp = html[:html.index(end)]
    firstName = temp


    #TO GET NUMBER
    val = 'valign="top">'

    html = html[html.index(val) + val.__len__():]
    temp = html[:html.index('</td>')]
    phone = temp
    if '-' in phone:
        phone = ''

    phone.replace(' ', '')

    while '<' in phone:
        fIn = phone.index('<')
        fTwo = phone.index('>')
        phone = phone[:fIn] + phone[fTwo + 1:]

    #TO GET EMAIL
    firstName = firstName.replace(" ", "")
    lastName = lastName.replace(" ", "")

    adjust = lastName
    if '-' in adjust:
        adjust = adjust[:adjust.index('-')]

    email = firstName[0].lower() + adjust + "@darienps.org"
    val = 'valign="top">'

    html = html[html.index(val) + val.__len__():]

    #TO GET ROOM
    val = 'valign="top">'

    html = html[html.index(val) + val.__len__():]
    temp = html[:html.index('</td>')]
    office = temp
    office = office.replace(" ", "")
    office = office.strip()
    if '-' in office:
        office = ''

    while '<' in office:
        fIn = office.index('<')
        fTwo = office.index('>')
        office = office[:fIn] + office[fTwo + 1:]

    #TO GET DEPARTMENT
    val = 'valign="top">'
    end = '</td>'

    html = html[html.index(val) + val.__len__():]
    if (html[0:5] == '<span'):
        val = '#0000ff;">'
        html = html[html.index(val) + val.__len__():]
        end = '</span>'

    temp = html[:html.index(end)]
    while '<' in temp:
        fIn = temp.index('<')
        fTwo = temp.index('>')
        temp = temp[:fIn] + temp[fTwo + 1:]

    if 'Coordinator' in temp:
        temp = temp.replace('Coordinator', '')
        special = 'Coordinator'
    elif 'Secretary' in temp:
        temp = temp.replace('Secretary', '')
        special = 'Secretary'

    temp = temp.replace('-', '')
    if '&amp;' in temp:
        temp = temp[:temp.index('&amp')]

    temp = temp.strip()

    department = temp


    #Print out results
    print("******************************")
    if link.__len__() != 0:
        print(link)
    if lastName.__len__() != 0:
        print(lastName)
    if firstName.__len__() != 0:
        print(firstName)
    if phone.__len__() != 0:
        print(phone)
    if email.__len__() != 0:
        print(email)
    if office.__len__() != 0:
        print(office)
    if department.__len__() != 0:
        print(department)
    if special.__len__() != 0:
        print(special)
