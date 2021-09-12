import csv
import datetime
import dateutil.parser
import six


divisionmapping = {
    "7U Baseball Schedule": "Rookie League Baseball",
    "10U Baseball Schedule": "Minor League Baseball",
    "12U Baseball Schedule": "Major League Baseball",
    "Babe Ruth Schedule": "Senior Baseball",
    "8U Softball Schedule": "Girls Softball 8U",
    "10U Softball Schedule": "Girls Softball 10U",
    "12U Softball Schedule": "Girls Softball 12U",
    "16U Softball Schedule": "Girls Softball 16U"
}

venuemapping = {
    "South Amboy": "South Amboy - Allie Clark Sports Complex",
    "South Amboy High School": "South Amboy High School",
    "Spotswood Front Field": "SYBSL Front Field",
    "Spotswood Back Field": "SYBSL Back Field",
    "Sayreville AA Complex Field #1": "Sayreville A.A. Complex #1",
    "Sayreville AA Complex Field #2_": "Sayreville A.A. Complex #2",
    "Sayreville Babe Ruth": "The Pit",
    "Youth Complex Field 1": "Perth Amboy Youth Complex #1",
    "Youth Complex Field 2": "Perth Amboy Youth Complex #2",
    "Youth Complex Field 3": "Perth Amboy Youth Complex #3",
    "Youth Complex Field 4": "Perth Amboy Youth Complex #4",
    "Cheesequake Road Field A": "Cheesequake Road A",
    "Cheesequake Road Field B": "Cheesequake Road B"
}

teammapping = {
    'Rookie': {
        "Spotswood #1": "Rookies Williams",
        "Spotswood #2": "Rookies Waldman",
    },
    'Minor': {
        "Spotswood #1": "Minors Williams",
        "Spotswood #2": "Minors Dobres",
        "Spotswood #3": "Minors Genito"
    },
    'Major': {
        "Spotswood #1": "Majors Casterline"
    },
    '8U': {
        "Spotswood #1": "8U Softball Patel",
        "Spotswood #2": "8U Softball Olivia"
    },
    '10U': {
        "Spotswood #1": "10U Softball Varick",
        "Spotswood #2": "10U Softball Direnzo"
    },
    '12U': {
        "Spotswood #1": "12U Softball Shearn"
    },
    '16U': {
        "Spotswood #1": "16U Softball Ziegler"
    }
}

with open('schedules/MASTER SCHEDULE FALL 2021 - Baseball.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == row[2] == row[3] == row[4] == '':
            division = divisionmapping[row[0]]
            continue
        if row[0] == 'Date':
            continue
        # division
        field0 = str(division)
        # visting team
        if 'Spotswood' in row[2]:
            shortleaguename = division.split()[0]
            field1 = teammapping[shortleaguename][row[2]]
        else:    
            field1 = row[2]
        # home team
        if 'Spotswood' in row[3]:
            shortleaguename = division.split()[0]
            field2 = teammapping[shortleaguename][row[3]]
        else:    
            field2 = row[3]
        # date
        field3 = (dateutil.parser.parse(row[0])).strftime('%m/%d/%y')
        # start time
        field4 = (dateutil.parser.parse(row[1])).strftime('%I:%M %p')
        # venue
        if row[4] in venuemapping:
            field5 = venuemapping[row[4]]
        else:
            field5 = row[4]
        # print("field 0 is " + field0)
        # print("field 1 is " + field1)
        # print("field 2 is " + field2)
        # print("field 3 is " + field3)
        # print("field 4 is " + field4)
        # print("field 5 is " + field5)
        if "Spotswood" in row[2] or "Spotswood" in row[3]:
            print(",".join([field0, field1, field2, field3, field4, field5]))


with open('schedules/MASTER SCHEDULE FALL 2021 - Softball.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == row[2] == row[3] == row[4] == '':
            division = divisionmapping[row[0]]
            continue
        if row[0] == 'Date':
            continue
        # division
        field0 = str(division)
        # visting team
        if 'Spotswood' in row[2]:
            shortleaguename = division.split()[2]
            field1 = teammapping[shortleaguename][row[2]]
        else:    
            field1 = row[2]
        # home team
        if 'Spotswood' in row[3]:
            shortleaguename = division.split()[2]
            field2 = teammapping[shortleaguename][row[3]]
        else:    
            field2 = row[3]
        # date
        field3 = (dateutil.parser.parse(row[0])).strftime('%m/%d/%y')
        # start time
        field4 = (dateutil.parser.parse(row[1])).strftime('%I:%M %p')
        # venue
        if row[4] in venuemapping:
            field5 = venuemapping[row[4]]
        else:
            field5 = row[4]
        # print("field 0 is " + field0)
        # print("field 1 is " + field1)
        # print("field 2 is " + field2)
        # print("field 3 is " + field3)
        # print("field 4 is " + field4)
        # print("field 5 is " + field5)
        if "Spotswood" in row[2] or "Spotswood" in row[3]:
            print(",".join([field0, field1, field2, field3, field4, field5]))