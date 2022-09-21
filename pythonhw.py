# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call
# 2. Determine the memberships status of all applicants
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}


def applicantPrice(applicant, members):
    if applicant in members:
        return 3.5
    return 5

def generateTicket(applicant, members):
    ticket = {
        "name": applicant,
        "membershipStatus": applicant in members,
        "price": applicantPrice(applicant, members)
    }
    return ticket

def getmembershipStatus(membershipStatus, members):
    for applicant in request["applicants"]:
        if applicant in members:
            membershipStatus[applicant] = True
        else:
            membershipStatus[applicant] = False

def getMembers():
    members = []
    
    for key, value in memberStatus.items():
        if value:
            members.append(key)
    
    return members

def getSuccessfulApplicants(bannedApplicants):
    successfulApplicants = []

    for name in request["applicants"]:
        if name in bannedApplicants:
            continue
        successfulApplicants.append(name)

    return successfulApplicants

def checkBanned(name):
    return name in bannedVisitors

def getBannedApplicants():
    bannedApplicants = filter(checkBanned, request["applicants"])
    return list(bannedApplicants)

def processRequest(request):
    try:
        firstApplicant = request["applicants"][0]
    except IndexError:
        result = {"error": "No applicants"}
        return result
    else:
        bannedApplicants = getBannedApplicants()
        successfulApplicants = getSuccessfulApplicants(bannedApplicants)

        members = getMembers()
        membershipStatus = {}
        getmembershipStatus(membershipStatus, members)
        
        totalCost = 0
        for applicant in successfulApplicants:
            totalCost += applicantPrice(applicant, members)

        tickets = []
        for applicant in successfulApplicants:
            tickets.append(generateTicket(applicant, members))

        result = {
            "successfulApplicants": successfulApplicants,
            "bannedApplicants": bannedApplicants,
            "totalCost": totalCost,
            "tickets": tickets,
        }

        return result


print(processRequest(request))

# {
#   successfulApplicants:
#   bannedApplicatns:
#   totalCost:
#   tickets: [
#       {
#            "name": ,
#            "membershipStatus": ,
#            "price":
#       }, ....
#   ]
#
# }


# OR

# {"error": "No applicants"}