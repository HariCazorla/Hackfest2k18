import os
import csv
import json
import numpy as np
import pandas as pd

UUID = "uuid"
CS = "cellserver"
CLIENTS = "clients"
MS = "mediaserver"
CBL = "capacitybasedlicensing"
LIC = "licensescategory"

#Different License types
dpLicenses = ["Micro Focus Data Protector Express - per CPU",
              "Micro Focus Data Protector Premium - per CPU"]

HOST = "host"
OS = "os"
DEVTYPE = "devicetype"
USAGE = "usage"
BTYPE = "backuptype"
PROTECTEDDATA = "totalprotecteddata"
VER = "ver"

ANALYSED_DATA = {}

#define a list for different type of clients
clientComponent = ["cc","da","ma","oracle","sap","mssql","vepa","clus","momgui","core","ts_core","ts_cs","ts_as"]
inList = lambda x:x in clientComponent

def initCsvFiles():

    with open('CM.csv', 'w+', newline='') as cmcsv:
        writer = csv.writer(cmcsv, delimiter=',')
        row = ["uuid","os","ver"]
        writer.writerow(row)
    cmcsv.close()

    with open('BACKUP_DETAILS.csv', 'w+', newline='') as bkpcsv:
        writer = csv.writer(bkpcsv, delimiter=',')
        row = ["BackupType","DataProtected"]
        writer.writerow(row)
    bkpcsv.close()

    with open('CLIENTS.csv', 'w+', newline='') as clicsv:
        writer = csv.writer(clicsv, delimiter=',')
        row = ["clients","os","ver"]
        writer.writerow(row)
    clicsv.close()

    with open('LIC.csv', 'w+', newline='') as liccsv:
        writer = csv.writer(liccsv, delimiter=',')
        row = ["category","value"]
        writer.writerow(row)
    liccsv.close()

    with open('MEDIA.csv', 'w+', newline='') as mediacsv:
        writer = csv.writer(mediacsv, delimiter=',')
        row = ["MediaType","DataProtected"]
        writer.writerow(row)
        mediacsv.close()

def getCellDetails(json_data):
    CellManager = ""
    uuid = json_data[UUID]
    cellserver = json_data[CS]
    osType = -1
    dpVer = -1
    clients_json = json_data[CLIENTS]
    for client in clients_json:
        try:
            # Writing to CM.csv uuid,os type
            if client[HOST] == cellserver:
                osType = client[OS]

                dpVer = client['ts_as']
                row = [uuid, osType, dpVer]
                print("cellmanager is " + client[HOST] + " And OS is "+ client[OS])
                with open('CM.csv','a',newline='') as cmcsv:
                    writer = csv.writer(cmcsv, delimiter=',')
                    writer.writerow(row)
                cmcsv.close()

            # Writing to CLIENTS.csv
            else:
                osType = client[OS]
                for key in client.keys():
                    if inList(key):
                        dpVer = client[key]
                row = [client['host'], osType, dpVer]
                with open('CLIENTS.csv','a',newline='') as clicsv:
                    writer = csv.writer(clicsv, delimiter=',')
                    writer.writerow(row)
                clicsv.close()

        except:
            print("caught exception while writing into csv files")

    # Writing into LIC.csv
    licDict = {}
    if LIC in json_data:
        licDetails = json_data[LIC]
        count = 0
        for lic in licDetails:
            if "numberoflicenses" in lic:
                licDict[lic['category']] = lic['numberoflicenses']
            if "totalLicensesInstalled" in lic:
                licDict[lic['category']] = lic['totalLicensesInstalled']

        with open('LIC.csv', 'a', newline='') as liccsv:
            writer = csv.writer(liccsv, delimiter=',')
            for key, value in licDict.items():
                writer.writerow([key, value])
        liccsv.close()
    else:
        print("N0 LICENSING INFO FOUND IN "+cellserver)

    # Writing into MEDIA.csv
    if MS in json_data:
        mediaDetails = json_data[MS]
        for media in mediaDetails:
            if media:
                if DEVTYPE in media:
                    if USAGE in media:
                        row = [media[DEVTYPE], media[USAGE][:-3]]
                    else:
                        row = [media[DEVTYPE], 0]
                    with open('MEDIA.csv', 'a', newline='') as mediacsv:
                        writer = csv.writer(mediacsv, delimiter=',')
                        writer.writerow(row)
                    mediacsv.close()
                else:
                    print("NO USAGE/DEVTYPE FIELD IN MEDIA INFO IN "+cellserver)
                    continue
            else:
                print("NO MEDIA INFO FOUND IN "+cellserver)
                continue

    # Writing into BACKUP_DETAILS.csv
    if CBL in json_data:
        cblDetails = json_data[CBL]
        for cbl in cblDetails:
            if cbl:
                if BTYPE in cbl and PROTECTEDDATA in cbl:
                    row = [cbl[BTYPE], cbl[PROTECTEDDATA][:-3]]
                    with open('BACKUP_DETAILS.csv', 'a', newline='') as bdcsv:
                        writer = csv.writer(bdcsv, delimiter=',')
                        writer.writerow(row)
                    bdcsv.close()
                else:
                    print("NO BTYPE/PROTECTED DATA INFO FOUND IN CBL IN "+cellserver)
                    continue
            else:
                print("NO CBL INFO FOUND IN "+cellserver)
                continue


def generateCsv():
    #location of telemetry files
    tele_dir = os.getcwd()+"\\tele"

    for tele_filename in os.listdir(tele_dir):
        tele_filename = "tele\\"+tele_filename
        with open(tele_filename) as json_file:
            json_data = json.load(json_file)
            getCellDetails(json_data)
        json_file.close()

################################
## ANALYSIS OF CSV DATA ##
################################

def analyseCsv():
    #CM.csv analysis
    CM_DF = pd.read_csv("CM.csv")
    CM_OS = {}
    CM_VER = {}
    CM_OS_DF = CM_DF[OS]
    CM_VER_DF = CM_DF[VER]
    CM_TOTAL = CM_DF[UUID].count()

    for i in CM_OS_DF:
        if i in CM_OS:
            CM_OS[i] = CM_OS[i] + 1
        else:
            CM_OS[i] = 1

    for i in CM_VER_DF:
        if i in CM_VER:
            CM_VER[i] = CM_VER[i] + 1
        else:
            CM_VER[i] = 1


    ANALYSED_DATA["CM_TOTAL"] = CM_TOTAL
    ANALYSED_DATA["CM_VER"] = CM_VER
    ANALYSED_DATA["CM_OS"] = CM_OS


    #CLIENTS.csv analysis
    CLIENTS_DF = pd.read_csv("CLIENTS.csv")
    CLIENTS_OS = {}
    CLIENTS_VER = {}
    CLIENTS_OS_DF = CLIENTS_DF[OS]
    CLIENTS_VER_DF = CLIENTS_DF[VER]
    CLIENTS_TOTAL = CLIENTS_DF[OS].count()

    for i in CLIENTS_OS_DF:
        if i in CLIENTS_OS:
            CLIENTS_OS[i] = CLIENTS_OS[i] + 1
        else:
            CLIENTS_OS[i] = 1

    for i in CLIENTS_VER_DF:
        if i in CLIENTS_VER:
            CLIENTS_VER[i] = CLIENTS_VER[i] + 1
        else:
            CLIENTS_VER[i] = 1

    ANALYSED_DATA["CLIENTS_TOTAL"] = CLIENTS_TOTAL
    ANALYSED_DATA["CLIENTS_VER"] = CLIENTS_VER
    ANALYSED_DATA["CLIENTS_OS"] = CLIENTS_OS


    # MEDIA.csv analysis
    MEDIA_DF = pd.read_csv("MEDIA.csv")
    MEDIA_INFO = {}

    for index, row in MEDIA_DF.iterrows():
        if row["MediaType"] in MEDIA_INFO:
            MEDIA_INFO[row["MediaType"]] = MEDIA_INFO[row["MediaType"]] + row["DataProtected"]
        else:
            MEDIA_INFO[row["MediaType"]] = row["DataProtected"]

    ANALYSED_DATA["MEDIA_INFO"] = MEDIA_INFO

    # BACKUP_DETAILS.csv analysis
    BD_DF = pd.read_csv("BACKUP_DETAILS.csv")
    BACKUP_INFO = {}

    for index, row in BD_DF.iterrows():
        if row["BackupType"] in MEDIA_INFO:
            BACKUP_INFO[row["BackupType"]] = BACKUP_INFO[row["BackupType"]] + row["DataProtected"]
        else:
            BACKUP_INFO[row["BackupType"]] = row["DataProtected"]

    ANALYSED_DATA["BACKUP_INFO"] = BACKUP_INFO

    # LIC.csv analysis
    LIC_DF = pd.read_csv("LIC.csv")
    LIC_INFO = {}

    for index, row in LIC_DF.iterrows():
        if row["category"] in LIC_INFO:
            LIC_INFO[row["category"]] = LIC_INFO[row["category"]] + row["value"]
        else:
            LIC_INFO[row["category"]] = row["value"]

    ANALYSED_DATA["LIC_INFO"] = LIC_INFO


def main():
    # clear all csv files and add header
    initCsvFiles()
    # Parse telemetry data from files in tele folder
    generateCsv()
    #generate ANALYSED_DATA output dictionary
    analyseCsv()
    return ANALYSED_DATA


#main()
#for k in json_data.keys():
#   print(k)



