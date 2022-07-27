import getpass
import sqlite3
import boto3
from boto3.s3.transfer import S3UploadFailedError
from botocore.exceptions import ClientError
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
            "codeguru-reviewer:ListRecommendations"
         ],
         "Resource": "arn:aws:codeguru-reviewer:us-east-2:123456789012:association:association-uuid"
      }
   ]
}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "codeguru-reviewer:DescribeRepositoryAssociation"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "aws:RequestTag/ViewAssocatedRepositoryDetails": "DenyViewRepository"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": [
        "codeguru-reviewer:DisassociateRepository"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "aws:TagKeys": ["DenyDisassociate"]
        }
      }
    }
  ]
}
def do_scenario(s3_resource):
    print('-'*88)
    print("Welcome to the Amazon S3 getting started demo!")
    print('-'*88)

    bucket_name = f'doc-example-bucket-{uuid.uuid4()}'
    bucket = s3_resource.Bucket(bucket_name)
    try:
        bucket.create(
            CreateBucketConfiguration={
                'LocationConstraint': s3_resource.meta.client.meta.region_name})
        print(f"Created demo bucket named {bucket.name}.")
    except ClientError as err:
        print(f"Tried and failed to create demo bucket {bucket_name}.")
        print(f"\t{err.response['Error']['Code']}:{err.response['Error']['Message']}")
        print(f"\nCan't continue the demo without a bucket!")
        return
def find_violation(current_tags, required_tags):
    violation = ""
    for rtag,rvalues in required_tags.iteritems():
        tag_present = False
        for tag in current_tags:
            if tag['key'] == rtag:
                value_match = False
                tag_present = True
                rvaluesplit = rvalues.split(",")
                for rvalue in rvaluesplit:
                    if tag['value'] == rvalue:
                        value_match = True
                    if tag['value'] != "":
                        if rvalue == "*":
                            value_match = True
                if value_match == False:
                    violation = violation + "\n" + tag['value'] + " doesn't match any of " + required_tags[rtag] + "!"
        if not tag_present:
            violation = violation + "\n" + "Tag " + str(rtag) + " is not present."
    if violation == "":
        return None
    return  violation
connection=sqlite3.connect('hospital.db')
cursor=connection.cursor()
error=1
from os import system, name
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
cursor.execute("""select count(name) from sqlite_master where type='table' and name='doctor'""")
if cursor.fetchone()[0]==0:
    cursor.execute("""CREATE TABLE doctor ( 
    d_id number primary key, 
    dnamedfirst VARCHAR2(20), 
    dnamedlast VARCHAR2(30), 
    password varchar2(20) not null,
    speciality varchar2(40) not null,
    shift varchar2(10) not null,
    phone number(10) not null);""")
cursor.execute("""select count(name) from sqlite_master where type='table' and name='patient'""")
if cursor.fetchone()[0]==0:
    cursor.execute("""CREATE TABLE patient ( 
    p_id number primary key, 
    pfirst VARCHAR2(20), 
    pdlast VARCHAR2(30), 
    City varchar2(20) not null,
    DOB date not null,
    age number not null,
    DOA date not null,
    number number(10) not null);""")
    cursor.execute("""CREATE TABLE virus ( 
    p_id number not null, 
    dname VARCHAR2(20) primary key,
    vname VARCHAR2(20), 
    treatment VARCHAR2(50), 
    symptoms varchar2(50) not null);""")
    cursor.execute("""CREATE TABLE bacteria ( 
    p_id number not null, 
    dname VARCHAR2(20) primary key,
    bname VARCHAR2(20), 
    treatment VARCHAR2(50), 
    symptoms varchar2(50) not null);""")
    cursor.execute("""CREATE TABLE injury ( 
    p_id number not null, 
    iname VARCHAR2(20) primary key,
    idiagnosis VARCHAR2(50), 
    type varchar2(50) not null);""")
    cursor.execute("""insert into patient values(101,'1mohit','Nayak','Bangalore','15-March-2001',18,'08-March-2020',9078435952)""")
    cursor.execute("""insert into patient values(102,'Anikiat','Saraf','Kolkata','22-Dec-2000','19','15-Feb-2020',9674825476)""")
    cursor.execute("""insert into patient values(103,'Rishank','Pratik','Orissa','22-Dec-2001','18','19-Nov-2015',9117854569)""")
    cursor.execute("""insert into patient values(104,'Risav','Jana','Nepal','06-Jan-2001',18,'25-Oct-2010',7854963284)""")
    cursor.execute("""insert into patient values(105,'Wilson','Vidyut','Mumbai','23-Nov-2001',18,'23-Nov-2005',7854129645)""")
    cursor.execute("""insert into patient values(106,'Dinesh','Sharma','Rajasthan','23-Feb-2000',20,'23-Feb-2000',8476423858)""")
    cursor.execute("""insert into virus values(103,'Ebola','Ebov','Oxygen Therapy, IV Fluids','Muscle Pain, Fever, Bleeding')""")
    cursor.execute("""insert into virus values(105,'Measles','Paramyxo','Vitamin A','Cough, Skin Rash')""")
    cursor.execute("""insert into bacteria values(101,'TB','Mycobacterium','Antibiotics','Cough and Sneezes')""")
    cursor.execute("""insert into bacteria values(106,'Cholera','Vibrio','IV Fluids, Antibiotics','Seizures, Diarrhoea')""")
    cursor.execute("""insert into injury values(102,'Hair line Fracture','Plaster, Pain Killer','Toe Fracture')""")
    cursor.execute("""insert into injury values(104,'bullet wound','Removal of Bullet','Wound')""")
    print("Databse created successfully")
    
else:
    e=1
    while e!=0:
        e=int(input("1. Sign In\n2. Create a New Doctor Account\n"))
        if e==2:
            did=int(input('\nEnter id - '))
            dnf=input('Enter first name - ')
            dnl=input('Enter last name - ')
            pas=getpass.getpass('Enter password - ')
            spec=input('Enter speciality - ')
            shf=input('Enter working shift - ')
            ph=int(input('Enter phone number - '))
            cursor.execute("""insert into doctor values(?,?,?,?,?,?,?)""",(did,dnf,dnl,pas,spec,shf,ph))
            screen_clear()
            e=1
        elif e==1:
            while error==1:
                i=input("\nEnter your ID - ")
                p=getpass.getpass("Enter your Password - ")
                cursor.execute("""select count(d_id) from doctor where d_id=(?)""",(i,))
                if cursor.fetchone()[0]==1:
                    cursor.execute("""select count(password) from doctor where password=?""",(p,))
                    if cursor.fetchone()[0]==1:
                        print("\nSign in successful!")
                        screen_clear()
                        error=0
                        e=0
                        r=1
                        cursor.execute("""select d_id,dnamedfirst,dnamedlast,speciality,shift,phone from doctor where d_id=(?)""",(i,))
                        for row in cursor.fetchall():
                           print("ID -",row[0],"  Name -",row[1], row[2],"  Speciality -",row[3],"\nShift -",row[4],"  Phone Number -",row[5])
                        while r!=0:
                           print("\n1. View Patient details\n2. Add a New Patient\n3. Delete Patient Details\n0. Exit")
                           r=int(input())
                           if r==1:
                              access=input("\nEnter Patient ID:- ")
                              cursor.execute("""select count(*) from patient where p_id=(?)""",(access,))
                              if cursor.fetchone()[0]!=0:
                                 cursor.execute("""select * from patient where p_id=(?)""",(access,))
                                 print("\nPatient Details - ")
                                 for row in cursor.fetchall():
                                    print("Id: ", row[0])
                                    print("First Name: ", row[1])
                                    print("Last Name: ", row[2])
                                    print("City: ", row[3])
                                    print("Date of Birth: ", row[4])
                                    print("Age: ", row[5])
                                    print("Date of Admission: ", row[6])
                                 print("\nDiagnosis Report - ")
                                 cursor.execute("""select count(*) from virus where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""select * from virus where p_id=(?)""",(access,))
                                    for row in cursor.fetchall():
                                       print("Id: ", row[0])
                                       print("Disease Name: ", row[1])
                                       print("Virus Name: ", row[2])
                                       print("Treatment: ", row[3])
                                       print("Symptoms: ", row[4])
                                    print("\n")
                                 cursor.execute("""select count(*) from bacteria where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""select * from bacteria where p_id=(?)""",(access,))
                                    for row in cursor.fetchall():
                                       print("Id: ", row[0])
                                       print("Disease Name: ", row[1])
                                       print("Bacteria Name: ", row[2])
                                       print("Treatment: ", row[3])
                                       print("Symptoms: ", row[4])
                                    print("\n")
                                 cursor.execute("""select count(*) from injury where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""select * from injury where p_id=(?)""",(access,))
                                    for row in cursor.fetchall():
                                       print("Id: ", row[0])
                                       print("Injury Name: ", row[1])
                                       print("Diagnosis Name: ", row[2])
                                       print("Type: ", row[3])
                                    print("\n")
                              else:
                                 print("Incorrect Patient id")
                           elif r==2:
                              pid=int(input('\nEnter id - '))
                              pnf=input('Enter first name - ')
                              pnl=input('Enter last name - ')
                              pcity=input('Enter city - ')
                              pdob=input('Enter date of birth - ')
                              page=int(input('Enter age - '))
                              pdoa=input('Enter date of admission - ')
                              pnum=int(input('Enter phone number - '))
                              cursor.execute("""insert into patient values(?,?,?,?,?,?,?,?)""",(pid,pnf,pnl,pcity,pdob,page,pdoa,pnum))
                              print("\n1. Virus\n2. Bacteria\n3. Injury")
                              m=int(input())
                              if m==1:
                                 dname=input("\nEnter disease name - ")
                                 bname=input("Enter virus name - ")
                                 treatment=input("Enter treatment - ")
                                 symptoms=input("Enter symptoms - ")
                                 cursor.execute("""insert into virus values(?,?,?,?,?)""",(pid,dname,bname,treatment,symptoms))
                              elif m==2:
                                 dname=input("\nEnter disease name - ")
                                 bname=input("Enter bacteria name - ")
                                 treatment=input("Enter treatment - ")
                                 symptoms=input("Enter symptoms - ")
                                 cursor.execute("""insert into bacteria values(?,?,?,?,?)""",(pid,dname,bname,treatment,symptoms))
                              elif m==3:
                                 iname=input("\nEnter injury name - ")
                                 idiag=input("Enter diagnosis - ")
                                 itype=input("Enter injury type - ")
                                 cursor.execute("""insert into injury values(?,?,?,?)""",(pid,iname,idiag,itype))
                              print("\nPatient Added")
                              connection.commit()
                           elif r==3:
                              access=input("\nEnter Patient ID:- ")
                              cursor.execute("""select count(*) from patient where p_id=(?)""",(access,))
                              if cursor.fetchone()[0]!=0:
                                 cursor.execute("""delete from patient where p_id=(?)""",(access,))
                                 cursor.execute("""select count(*) from virus where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""delete from virus where p_id=(?)""",(access,))
                                 cursor.execute("""select count(*) from bacteria where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""delete from bacteria where p_id=(?)""",(access,))
                                 cursor.execute("""select count(*) from injury where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""delete from injury where p_id=(?)""",(access,))
                              else:
                                 print("Incorrect Patient id Patient does not exist")
                              print("\nPatient Deleted")
                              connection.commit()
                           elif r==0:
                              break
                    else:
                        print("Incorrect passoword. Please retry ")
                else:
                    print("Incorrect User ID. Please retry ")
            break
        elif e==2212:
            cursor.execute("""select * from doctor""")
            print(cursor.fetchall())
            cursor.execute("""select * from virus""")
            print(cursor.fetchall())
            cursor.execute("""select * from bacteria""")
            print(cursor.fetchall())
            cursor.execute("""select * from injury""")
            print(cursor.fetchall())
            break
connection.commit()
connection.close()
print("")
def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')
    altimeter-valeport-lcm/
├── altimeter_valeport_lcm
│   ├── __init__.py
│   ├── __main__.py
│   ├── parser.py
│   └── snake_case.py
├── README.rst
└── setup.py

try:
    sqliteCon = sqlite3.connect('hospital.db')
    backupCon = sqlite3.connect('hospital_backup.db')
    with backupCon:
        sqliteCon.backup(backupCon, pages=1, progress=progress)
    print("backup successful")
except sqlite3.Error as error:
    print("Error while taking backup: ", error)
finally:
    if(backupCon):
        backupCon.close()
        sqliteCon.close()
