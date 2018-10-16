
# new stuff is from the self study jupyter notebooks.
def newstuff():
    s = "abc def ghi jkl mno pqr"
    s = s.rstrip("pqr")
    s = s.replace("b", "A")
    c = s.count("ghi")
    l = s.split(" ")
    for i in range(len,s):
        if s[i] == A: 
            s[i] = "hello world" # why doesn't it work?
            
    print(s)
    print(c)
    print(l)
    
# ooh, cool example from the course
def cool_example():
    sentence = "?was I tac a ti saW"
    for letter in reversed(sentence):
        print(letter, end='')

# how to print something to 2 dp.
def printto2dp():
    average = 2.22222222222
    print("{:.2f}".format(average))

# how to count unique items in a list using a dictionary
fish_observed = [goldfish, sucker fish, sucker fish, corydoras]

def countunique(fish_observed):
    species_dict = {}
    for entry in range(0,len(fish_observed)):
        if fish_observed[entry] in species_dict:
            species_dict[fish_observed[entry]] += 1
        else:
            species_dict[fish_observed[entry]] = 1
    print("The total number of species is {}".format(len(species_dict)))

# File parsing
def openfile():
    with open("light_trap.csv", "r") as f:
        for line in f:
            clean = line.rstrip("\n").split(",")
            data.extend(clean)
            """The data in the file will look like this
            Name, Age
            
            Bob, 12
            
            Joe, 10
            
            rstrip("\n") removes the line
            Name, Age
            Bob, 12
            Joe, 10
            
            if we did not do that and split it straight away we would end up with 
            [Name, Age\n]
            """

# You can press tab to Auto complete. (helps with spelling errors)
