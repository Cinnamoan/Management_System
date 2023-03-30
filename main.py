# Name:         Ian Carlos, Richard Chow, Kaleb Stuart, Franklin Oshevire Olore
# Student ID:   000893983, 000907549, 000896651, 000894515,
# Course Code:  CPRG216-C
# Instructor:   Mark Yoon
# Date:         14/12/2022 (Extension Approved)

class Doctor:
    # List of Doctor objects
    doctorsList = []

    def __init__(self, doctorID, doctorName, doctorSpecialty, doctorTime, doctorQualification, doctorRoomNum):
        self.doctorID = doctorID
        self.doctorName = doctorName
        self.doctorSpecialty = doctorSpecialty
        self.doctorTime = doctorTime
        self.doctorQualification = doctorQualification
        self.doctorRoomNum = doctorRoomNum

    # Formats each doctor’s information (properties) in the same format used in the .txt file
    def formatDrInfo(self):

        return 0

    # Asks the user to enter doctor properties (listed in the Properties point).
    def enterDrInfo(self):

        inputID = input("\nEnter the doctor's ID:\n\t")

        inputName = input("Enter the doctor's name:\n\t")

        inputSpecialty = input("Enter the doctor's specialty:\n\t")

        inputTime = input("Enter the doctor's times (e.g., 7am-10pm)\n\t")

        inputQualification = input("Enter the doctor's qualification(s):\n\t")

        inputRoomNumber = input("Enter the doctor's room number:\n\t")

        doctor = Doctor(inputID, inputName, inputSpecialty, inputTime, inputQualification, inputRoomNumber)

        # Add the newly created Doctor object at the end of the Doctor list
        Doctor.doctorsList.append(doctor)

        Doctor.addDrToFile(doctor)

    # Reads from “doctors.txt” file and fills the doctor objects in a list.
    def readDoctorsFile(self):

        with open("doctors.txt") as fh:
            # Skip first line/header
            next(fh)
            # Go through each line in the text file
            for line in fh:
                # Find each string separated by an underscore
                row = line.strip().split("_")
                # Then use each row variable to create a Doctor object
                Doctor.doctorsList.append(Doctor(*row))

        return Doctor.doctorsList

    # Searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters.
    def searchDoctorById(self):

        inputSearchDoctorID = input("\nEnter the doctor ID: ")

        # Boolean flag to indicate if a match has been found to know when
        # to continue or break in the following for loop
        searchFound = False

        # Loop through each Doctor object in the Doctor list
        for aDoctor in Doctor.doctorsList:

            if aDoctor.doctorID == inputSearchDoctorID:
                searchFound = True
                aDoctor.displayDoctorInfo()
                break

        if not searchFound:
            print("Doctor ID not found. Please try again.")

    # Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters.
    def searchDoctorByName(self):

        inputSearchDoctorName = input("\nEnter the doctor name: ")

        searchFound = False

        for aDoctor in Doctor.doctorsList:

            if aDoctor.doctorName == inputSearchDoctorName:
                searchFound = True
                aDoctor.displayDoctorInfo()
                break

        if not searchFound:
            print("Doctor name not found. Please try again.")

    # Displays doctor information on different lines, as a list.
    def displayDoctorInfo(self):

        print("\n{: <19}{: <19}{: <19}{: <19}{: <19}{: <19}".format("ID", "Name", "Specialty", "Timing",
                                                                    "Qualification", "Room Number"))

        print("\n{: <19}{: <19}{: <19}{: <19}{: <19}{: <19}".format(self.doctorID, self.doctorName,
                                                                    self.doctorSpecialty,
                                                                    self.doctorTime,
                                                                    self.doctorQualification,
                                                                    self.doctorRoomNum))

    # Asks the user to enter the ID of the doctor to change their information, and then the user can enter the
    # new doctor information.
    def editDoctorInfo(self):

        inputEditDoctorInfo = input("\nPlease enter the doctor ID that you want to edit their information: ")

        searchFound = False

        for aDoctor in Doctor.doctorsList:

            if aDoctor.doctorID == inputEditDoctorInfo:
                searchFound = True
                editDoctor = aDoctor
                break

        if not searchFound:
            print("Doctor ID not found. Please try again.")

        else:

            inputNewDoctorName = input("\nEnter the doctor's new name: \n\t")

            editDoctor.doctorName = inputNewDoctorName

            inputNewDoctorSpecialty = input("Enter the doctor's new specialty: \n\t")

            editDoctor.doctorSpecialty = inputNewDoctorSpecialty

            inputNewDoctorTime = input("Enter the doctor's new times: \n\t")

            editDoctor.doctorTime = inputNewDoctorTime

            inputNewDoctorQualification = input("Enter the doctor's new qualification: \n\t")

            editDoctor.doctorQualification = inputNewDoctorQualification

            inputNewDoctorRoomNum = input("Enter the doctor new room number: \n\t")

            editDoctor.doctorRoomNum = inputNewDoctorRoomNum

    # Displays all the doctors’ information, read from the file, as a report/table.
    def displayDoctorList(self):

        print("\n{: <19}{: <19}{: <19}{: <19}{: <19}{: <19}".format("ID", "Name", "Specialty", "Timing",
                                                                    "Qualification", "Room Number"))

        for doctor in Doctor.doctorsList:
            print("\n{: <19}{: <19}{: <19}{: <19}{: <19}{: <19}".format(doctor.doctorID, doctor.doctorName,
                                                                        doctor.doctorSpecialty, doctor.doctorTime,
                                                                        doctor.doctorQualification,
                                                                        doctor.doctorRoomNum))

    # Writes the list of doctors to the doctors.txt file after formatting it correctly.
    def writeListOfDoctorsToFile(self):
        return 0

    # Writes doctors to the doctors.txt file after formatting it correctly.
    def addDrToFile(self):

        with open('patients.txt', 'a') as f:
            f.write("\n" + str(self.doctorID) + "_" + str(self.doctorName) + "_" + str(self.doctorSpecialty) + "_"
                    + str(self.doctorTime) + "_" + str(self.doctorQualification) + "_" + str(self.doctorRoomNum))

            f.close()


class Facility:
    # List of Facility objects
    facilitiesList = []

    def __init__(self, facilityName):
        self.facilityName = facilityName

    # Adds and writes the facility name to the file.
    def addFacility(self):

        inputName = input("\nEnter the facility name:\n\t")

        facility = Facility(inputName)

        # Add the newly created Facility object at the end of the Facility list
        Facility.facilitiesList.append(facility)

    # Displays the list of facilities.
    def displayFacilities(self):

        print("\nThe Hospital Facilities are:")

        for facility in Facility.facilitiesList:
            print("\n", facility.facilityName)

    # Writes the facilities list to facilities.txt.
    def writeListOfFacilitiesToFile(self):

        with open('patients.txt', 'a') as f:
            f.write("\n" + str(self.facilityName))

            f.close()

    # *NEW* Not from the instructions
    # Reads the laboratories.txt file and fills its contents in a list of Facility objects.
    def readFacilitiesFile(self):

        with open("facilities.txt") as fh:
            # Skip first line/header
            next(fh)
            # Go through each line in the text file
            for line in fh:
                # Find each string separated by an underscore
                row = line.strip().split("_")
                # Then use each row variable to create a Doctor object
                Facility.facilitiesList.append(Facility(*row))

        return Facility.facilitiesList


class Laboratory:
    # List of Laboratory objects
    labsList = []

    def __init__(self, labName, labCost):
        self.labName = labName
        self.labCost = labCost

    # Adds and writes the lab name to the file in the format of the data that is in the file.
    def addLabToFile(self):
        return 0

    # Writes the list of labs into the file laboratories.txt.
    def writeListOfLabsToFile(self):
        with open('patients.txt', 'a') as f:
            f.write("\n" + str(self.labName) + "_" + str(self.labCost))

            f.close()

    # Displays the list of laboratories.
    def displayLabsList(self):

        print("\n{: <16}Cost".format("Lab"))

        for lab in Laboratory.labsList:
            # Need to format this properly
            print("\n{:<16}{}".format(lab.labName, lab.labCost))

    # Formats the Laboratory object similar to the laboratories.txt file.
    def formatLaboratoryInfo(self):
        return 0

    # Asks the user to enter lab name and cost and forms a Laboratory object.
    def enterLaboratoryInfo(self):

        inputName = input("\nEnter the Lab's name:\n\t")

        inputCost = input("Enter the Lab's cost:\n\t")

        lab = Laboratory(inputName, inputCost)

        # Add the newly created Laboratory object at the end of the Laboratory list
        Laboratory.labsList.append(lab)

    # Reads the laboratories.txt file and fills its contents in a list of Laboratory objects.
    def readLaboratoriesFile(self):

        with open("laboratories.txt.") as fh:
            # Skip first line/header
            next(fh)
            # Go through each line in the text file
            for line in fh:
                # Find each string separated by an underscore
                row = line.strip().split("_")
                # Then use each row variable to create a Doctor object
                Laboratory.labsList.append(Laboratory(*row))

        return Laboratory.labsList


class Patient:
    patientsList = []

    def __init__(self, patientID, patientName, patientDisease, patientGender, patientAge):
        self.patientID = patientID
        self.patientName = patientName
        self.patientDisease = patientDisease
        self.patientGender = patientGender
        self.patientAge = patientAge

    # Formats patient information to be added to the file
    def formatPatientInfo(self):
        return 0

    # Asks the user to enter the patient info
    def enterPatientInfo(self):

        inputID = input("\nEnter the patient's ID:\n\t")

        inputName = input("Enter the patient's name:\n\t")

        inputDisease = input("Enter the patient's disease:\n\t")

        inputGender = input("Enter the patient's gender:\n\t")

        inputAge = input("Enter the patient's age:\n\t")

        patient = Patient(inputID, inputName, inputDisease, inputGender, inputAge)

        Patient.patientsList.append(patient)

        Patient.addPatientToFile(patient)

    # Reads from file patients.txt
    def readPatientsFile(self):
        with open("patients.txt") as fh:
            # Skip first line/header
            next(fh)
            # Go through each line in the text file
            for line in fh:
                #
                row = line.strip().split("_")
                Patient.patientsList.append(Patient(*row))

        return Patient.patientsList

    # Searches for a patient using their ID
    def searchPatientByID(self):

        inputSearchPatientID = input("\nEnter the patient ID: ")

        searchFound = False

        for aPatient in Patient.patientsList:

            if aPatient.patientID == inputSearchPatientID:
                searchFound = True
                aPatient.displayPatientInfo()
                break

        if not searchFound:
            print("Patient ID not found. Please try again.")

    # Displays patient info
    def displayPatientInfo(self):

        print("\n{: <19}{: <19}{: <19}{: <19}{}".format("ID", "Name", "Disease", "Gender", "Age"))

        print("\n{: <19}{: <19}{: <19}{: <19}{}".format(self.patientID, self.patientName, self.patientDisease,
                                                        self.patientGender, self.patientAge))

    # Asks the user to edit patient information
    def editPatientInfo(self):

        inputEditPatientInfo = input("\nPlease enter the ID of the patient whose information you want to edit: ")

        searchFound = False

        for aPatient in Patient.patientsList:

            if aPatient.patientID == inputEditPatientInfo:
                searchFound = True
                editPatient = aPatient
                break

        if not searchFound:
            print("Patient ID not found. Please try again.")

        else:

            inputNewPatientName = input("\nEnter the patient's new name: \n\t")

            editPatient.patientName = inputNewPatientName

            inputNewPatientDisease = input("Enter the patient's new disease: \n\t")

            editPatient.patientDisease = inputNewPatientDisease

            inputNewPatientGender = input("Enter the patient's gender: \n\t")

            editPatient.patientGender = inputNewPatientGender

            inputNewPatientAge = input("Enter the patient's age: \n\t")

            editPatient.patientAge = inputNewPatientAge

    # Displays the list of patients
    def displayPatientsList(self):

        print("\n{: <19}{: <19}{: <19}{: <19}{}".format("ID", "Name", "Disease", "Gender", "Age"))

        for patient in Patient.patientsList:
            print("\n{: <19}{: <19}{: <19}{: <19}{}".format(patient.patientID, patient.patientName,
                                                            patient.patientDisease, patient.patientGender,
                                                            patient.patientAge))

    # Writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self):
        return 0

    # Adds a new patient to the file
    def addPatientToFile(self):

        with open('patients.txt', 'a') as f:
            f.write("\n" + str(self.patientID) + "_" + str(self.patientName) + "_" + str(self.patientDisease) + "_"
                    + str(self.patientGender) + "_" + str(self.patientAge))

            f.close()


class Management:

    # To display the menu shown in the Sample Run section
    def displayMenu(self):

        # Open each respective text file
        Doctor.readDoctorsFile(self)
        Facility.readFacilitiesFile(self)
        Laboratory.readLaboratoriesFile(self)
        Patient.readPatientsFile(self)

        while True:

            user_input = input("\nWelcome to the Alberta Hospital (AH) Management System."
                               "\nSelect from the following or options, or press 0 to exit:"
                               "\n1 - Doctors"
                               "\n2 - Facilities"
                               "\n3 - Laboratories"
                               "\n4 - Patients\n\n")

            if not user_input.isdigit():
                print("\nInvalid input. Please enter a number.")
                continue

            user_input = int(user_input)

            if user_input < 0 or user_input > 5:
                print("\nInvalid input. Please enter a number from 0-4.")
                continue
            elif user_input == 0:
                print("\nThank you for using the Alberta Hospital (AH) Management System. Have a good one!")
                break

            # Doctors Menu
            if user_input == 1:

                while True:

                    doctor_user_input = input("\nDoctors Menu:"
                                              "\n1 - Display doctors list"
                                              "\n2 - Search for doctor by ID"
                                              "\n3 - Search for doctor by name"
                                              "\n4 - Add doctor"
                                              "\n5 - Edit doctor info"
                                              "\n6 - Back to Main Menu\n\n")

                    if not doctor_user_input.isdigit():
                        print("\nInvalid input. Please enter a number.")
                        continue

                    doctor_user_input = int(doctor_user_input)

                    if doctor_user_input < 0 or doctor_user_input > 7:
                        print("\nInvalid input. Please enter a number from 0-6.")

                    if doctor_user_input == 1:
                        Doctor.displayDoctorList(self)

                    if doctor_user_input == 2:
                        Doctor.searchDoctorById(self)

                    if doctor_user_input == 3:
                        Doctor.searchDoctorByName(self)

                    if doctor_user_input == 4:
                        Doctor.enterDrInfo(self)

                    if doctor_user_input == 5:
                        Doctor.editDoctorInfo(self)

                    if doctor_user_input == 6:
                        break

            # Facilities Menu
            if user_input == 2:

                while True:

                    facility_user_input = input("\nFacilities Menu:"
                                                "\n1 - Display facilities list"
                                                "\n2 - Add Facility"
                                                "\n3 - Back to Main Menu\n\n")

                    if not facility_user_input.isdigit():
                        print("\nInvalid input. Please enter a number.")
                        continue

                    facility_user_input = int(facility_user_input)

                    if facility_user_input < 0 or facility_user_input > 4:
                        print("\nInvalid input. Please enter a number from 0-3.")

                    if facility_user_input == 1:
                        Facility.displayFacilities(self)

                    if facility_user_input == 2:
                        Facility.addFacility(self)

                    if facility_user_input == 3:
                        break

            # Laboratories Menu
            if user_input == 3:

                while True:

                    laboratory_user_input = input("\nLaboratories Menu:"
                                                  "\n1 - Display laboratories list"
                                                  "\n2 - Add laboratory"
                                                  "\n3 - Back to Main Menu\n\n")

                    if not laboratory_user_input.isdigit():
                        print("\nInvalid input. Please enter a number.")
                        continue

                    laboratory_user_input = int(laboratory_user_input)

                    if laboratory_user_input < 0 or laboratory_user_input > 4:
                        print("\nInvalid input. Please enter a number from 0-3.")

                    if laboratory_user_input == 1:
                        Laboratory.displayLabsList(self)

                    if laboratory_user_input == 2:
                        Laboratory.enterLaboratoryInfo(self)

                    if laboratory_user_input == 3:
                        break

            # Patients Menu
            if user_input == 4:

                while True:

                    patient_user_input = input("\nPatients Menu:"
                                               "\n1 - Display patients list"
                                               "\n2 - Search for patient by ID"
                                               "\n3 - Add patient"
                                               "\n4 - Edit patient info"
                                               "\n5 - Back to Main Menu\n\n")

                    if not patient_user_input.isdigit():
                        print("\nInvalid input. Please enter a number.")
                        continue

                    patient_user_input = int(patient_user_input)

                    if patient_user_input < 0 or patient_user_input > 5:
                        print("\nInvalid input. Please enter a number from 0-4.")

                    if patient_user_input == 1:
                        Patient.displayPatientsList(self)

                    if patient_user_input == 2:
                        Patient.searchPatientByID(self)

                    if patient_user_input == 3:
                        Patient.enterPatientInfo(self)

                    if patient_user_input == 4:
                        Patient.editPatientInfo(self)

                    if patient_user_input == 5:
                        break


# ********************************************************************************************************************

testMenu = Management()

testMenu.displayMenu()
