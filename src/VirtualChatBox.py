import os
import random
import socket
import sys
import time
import threading

try:
    from mcpi import minecraft, block, vec3
except ImportError:
    print '\033[0;33;40m',
    print "Warning: You haven't minecraft-pi yet."
    print " Only in getting minecraft-pi can you run Virtual Chat Box.",
    print '\033[0m'
    sys.exit(1)
disablems = True
try:
    import minecraftstuff
    disablems = False
except ImportError:
    print '\033[0;33;40m',
    print "Warning: Package \"minecraftstuff\" is defined."
    print " It means some commands will not be available."
    print " Try \"sudo pip install minecraftstuff\" to get it.",
    print '\033[0m'

disablegpio = True
try:
    import RPi.GPIO
    disablegpio = False
except ImportError:
    print '\033[0;33;40m',
    print "Warning: Package \"RPi.GPIO\" is defined."
    print " It means some commands will not be available.",
    print '\033[0m'

try:
    if len(sys.argv) == 3:
        mc = minecraft.Minecraft.create(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) == 2:
        mc = minecraft.Minecraft.create(sys.argv[1])
    elif len(sys.argv) == 1:
        mc = minecraft.Minecraft.create()
    else:
        raise TypeError("parameters are too many.")
except ValueError:
    print '\033[0;31;40m',
    print "Parameter value error: ", sys.exc_info()[1],
    print '\033[0m'
    sys.exit(1)
except TypeError:
    print '\033[0;31;40m',
    print "Parameter type error: ", sys.exc_info()[1],
    print '\033[0m'
    sys.exit(1)
except socket.error, arg:
    (errno, err_msg) = arg
    print '\033[0;31;40m',
    print "Cannot connect to server: %s, errno=%d" % (err_msg, errno),
    print '\033[0m'
    sys.exit(1)
if not disablems:
    mcdraw = minecraftstuff.MinecraftDrawing(mc)
    mcshapes = {}
    mcturtles = {}
if not os.path.exists("functions"):
    os.mkdir("functions")
threads = {}
helpPageCount = 12
playerName = "Player"
msgChat = True
blockDictionary = {
    "air": block.AIR,
    "stone": block.STONE,
    "grass": block.GRASS,
    "dirt": block.DIRT,
    "cobblestone": block.COBBLESTONE,
    "wood_planks": block.WOOD_PLANKS,
    "sapling": block.SAPLING,
    "bedrock": block.BEDROCK,
    "water_flowing": block.WATER_FLOWING,
    "water": block.WATER,
    "water_stationary": block.WATER_STATIONARY,
    "lava_flowing": block.LAVA_FLOWING,
    "lava": block.LAVA,
    "lava_stationary": block.LAVA_STATIONARY,
    "sand": block.SAND,
    "gravel": block.GRAVEL,
    "gold_ore": block.GOLD_ORE,
    "iron_ore": block.IRON_ORE,
    "coal_ore": block.COAL_ORE,
    "wood": block.WOOD,
    "leaves": block.LEAVES,
    "glass": block.GLASS,
    "lapis_lazuli_ore": block.LAPIS_LAZULI_ORE,
    "lapis_lazuli_block": block.LAPIS_LAZULI_BLOCK,
    "sandstone": block.SANDSTONE,
    "bed": block.BED,
    "cobweb": block.COBWEB,
    "grass_tall": block.GRASS_TALL,
    "wool": block.WOOL,
    "flower_yellow": block.FLOWER_YELLOW,
    "flower_cyan": block.FLOWER_CYAN,
    "mushroom_brown": block.MUSHROOM_BROWN,
    "mushroom_red": block.MUSHROOM_RED,
    "gold_block": block.GOLD_BLOCK,
    "iron_block": block.IRON_BLOCK,
    "stone_slab_double": block.STONE_SLAB_DOUBLE,
    "stone_slab": block.STONE_SLAB,
    "brick_block": block.BRICK_BLOCK,
    "tnt": block.TNT,
    "bookshelf": block.BOOKSHELF,
    "moss_stone": block.MOSS_STONE,
    "obsidian": block.OBSIDIAN,
    "torch": block.TORCH,
    "fire": block.FIRE,
    "stairs_wood": block.STAIRS_WOOD,
    "chest": block.CHEST,
    "diamond_ore": block.DIAMOND_ORE,
    "diamond_block": block.DIAMOND_BLOCK,
    "crafting_table": block.CRAFTING_TABLE,
    "farmland": block.FARMLAND,
    "furnace_inactive": block.FURNACE_INACTIVE,
    "furnace_active": block.FURNACE_ACTIVE,
    "door_wood": block.DOOR_WOOD,
    "ladder": block.LADDER,
    "stairs_cobblestone": block.STAIRS_COBBLESTONE,
    "door_iron": block.DOOR_IRON,
    "redstone_ore": block.REDSTONE_ORE,
    "snow": block.SNOW,
    "ice": block.ICE,
    "snow_block": block.SNOW_BLOCK,
    "cactus": block.CACTUS,
    "clay": block.CLAY,
    "sugar_cane": block.SUGAR_CANE,
    "fence": block.FENCE,
    "glowstone_block": block.GLOWSTONE_BLOCK,
    "bedrock_invisible": block.BEDROCK_INVISIBLE,
    "stone_brick": block.STONE_BRICK,
    "glass_pane": block.GLASS_PANE,
    "melon": block.MELON,
    "fence_gate": block.FENCE_GATE,
    "glowing_obsidian": block.GLOWING_OBSIDIAN,
    "nether_reactor_core": block.NETHER_REACTOR_CORE,
    "minecraft:air": block.AIR,
    "minecraft:stone": block.STONE,
    "minecraft:grass": block.GRASS,
    "minecraft:dirt": block.DIRT,
    "minecraft:cobblestone": block.COBBLESTONE,
    "minecraft:wood_planks": block.WOOD_PLANKS,
    "minecraft:sapling": block.SAPLING,
    "minecraft:bedrock": block.BEDROCK,
    "minecraft:water_flowing": block.WATER_FLOWING,
    "minecraft:water": block.WATER,
    "minecraft:water_stationary": block.WATER_STATIONARY,
    "minecraft:lava_flowing": block.LAVA_FLOWING,
    "minecraft:lava": block.LAVA,
    "minecraft:lava_stationary": block.LAVA_STATIONARY,
    "minecraft:sand": block.SAND,
    "minecraft:gravel": block.GRAVEL,
    "minecraft:gold_ore": block.GOLD_ORE,
    "minecraft:iron_ore": block.IRON_ORE,
    "minecraft:coal_ore": block.COAL_ORE,
    "minecraft:wood": block.WOOD,
    "minecraft:leaves": block.LEAVES,
    "minecraft:glass": block.GLASS,
    "minecraft:lapis_lazuli_ore": block.LAPIS_LAZULI_ORE,
    "minecraft:lapis_lazuli_block": block.LAPIS_LAZULI_BLOCK,
    "minecraft:sandstone": block.SANDSTONE,
    "minecraft:bed": block.BED,
    "minecraft:cobweb": block.COBWEB,
    "minecraft:grass_tall": block.GRASS_TALL,
    "minecraft:wool": block.WOOL,
    "minecraft:flower_yellow": block.FLOWER_YELLOW,
    "minecraft:flower_cyan": block.FLOWER_CYAN,
    "minecraft:mushroom_brown": block.MUSHROOM_BROWN,
    "minecraft:mushroom_red": block.MUSHROOM_RED,
    "minecraft:gold_block": block.GOLD_BLOCK,
    "minecraft:iron_block": block.IRON_BLOCK,
    "minecraft:stone_slab_double": block.STONE_SLAB_DOUBLE,
    "minecraft:stone_slab": block.STONE_SLAB,
    "minecraft:brick_block": block.BRICK_BLOCK,
    "minecraft:tnt": block.TNT,
    "minecraft:bookshelf": block.BOOKSHELF,
    "minecraft:moss_stone": block.MOSS_STONE,
    "minecraft:obsidian": block.OBSIDIAN,
    "minecraft:torch": block.TORCH,
    "minecraft:fire": block.FIRE,
    "minecraft:stairs_wood": block.STAIRS_WOOD,
    "minecraft:chest": block.CHEST,
    "minecraft:diamond_ore": block.DIAMOND_ORE,
    "minecraft:diamond_block": block.DIAMOND_BLOCK,
    "minecraft:crafting_table": block.CRAFTING_TABLE,
    "minecraft:farmland": block.FARMLAND,
    "minecraft:furnace_inactive": block.FURNACE_INACTIVE,
    "minecraft:furnace_active": block.FURNACE_ACTIVE,
    "minecraft:door_wood": block.DOOR_WOOD,
    "minecraft:ladder": block.LADDER,
    "minecraft:stairs_cobblestone": block.STAIRS_COBBLESTONE,
    "minecraft:door_iron": block.DOOR_IRON,
    "minecraft:redstone_ore": block.REDSTONE_ORE,
    "minecraft:snow": block.SNOW,
    "minecraft:ice": block.ICE,
    "minecraft:snow_block": block.SNOW_BLOCK,
    "minecraft:cactus": block.CACTUS,
    "minecraft:clay": block.CLAY,
    "minecraft:sugar_cane": block.SUGAR_CANE,
    "minecraft:fence": block.FENCE,
    "minecraft:glowstone_block": block.GLOWSTONE_BLOCK,
    "minecraft:bedrock_invisible": block.BEDROCK_INVISIBLE,
    "minecraft:stone_brick": block.STONE_BRICK,
    "minecraft:glass_pane": block.GLASS_PANE,
    "minecraft:melon": block.MELON,
    "minecraft:fence_gate": block.FENCE_GATE,
    "minecraft:glowing_obsidian": block.GLOWING_OBSIDIAN,
    "minecraft:nether_reactor_core": block.NETHER_REACTOR_CORE
}


def ifdo(args, super):
    if (len(args) < 4) or (not args[0].startswith("$")):
        invalid(super)
        return False
    sele = selector(args[0][1:], super)
    if sele == -1024:
        return False
    if args[2].startswith("$"):
        num = selector(args[2][1:], super)
        if not (type(sele) == type(num)):
            invalid(super)
            return False
    elif type(sele) == int:
        num = toint(args[2], -256, 256, super)
        if num <= -257:
            return False
    elif type(sele) == float:
        num = tofloat(args[2], super, -1025)
        if num <= -1025:
            return False
    elif type(sele) == str:
        num = args[2]
    else:
        invalid(super)
        return False
    command = tocommand(args[3:])
    if args[1] == "=":
        if sele == num:
            readCommand(command, super)
            return True
        return False
    else:
        if type(sele) == str or type(num) == str:
            invalid(super)
            return False
        if args[1] == "<":
            if sele < num:
                readCommand(command, super)
                return True
            return False
        elif args[1] == ">":
            if sele > num:
                readCommand(command, super)
                return True
            return False
        elif args[1] == "<=":
            if sele <= num:
                readCommand(command, super)
                return True
            return False
        elif args[1] == ">=":
            if sele >= num:
                readCommand(command, super)
                return True
            return False
        else:
            invalid(super)
            return False


def loop(args, super):
    if len(args) < 2:
        invalid(super)
        return
    if args[0] == "times":
        if len(args) < 3:
            invalid(super)
            return
        times = toint(args[1], 0, 256, super)
        if times == -1:
            return
        command = tocommand(args[2:])
        while times > 0:
            readCommand(command, super)
            times -= 1
    elif args[0] == "if":
        while ifdo(args[1:], super):
            pass
    else:
        invalid(super)
        return


def selector(argv, super):
    if argv.startswith("playerPosX"):
        if len(argv) == 10:
            return mc.player.getPos().x
        else:
            invalid(super)
            return -1024
    elif argv.startswith("playerPosY"):
        if len(argv) == 10:
            return mc.player.getPos().y
        else:
            invalid(super)
            return -1024
    elif argv.startswith("playerPosZ"):
        if len(argv) == 10:
            return mc.player.getPos().z
        else:
            invalid(super)
            return -1024
    elif argv.startswith("playerPosX_int"):
        if len(argv) == 10:
            return int(mc.player.getPos().x)
        else:
            invalid(super)
            return -1024
    elif argv.startswith("playerPosY_int"):
        if len(argv) == 10:
            return int(mc.player.getPos().y)
        else:
            invalid(super)
            return -1024
    elif argv.startswith("playerPosZ_int"):
        if len(argv) == 10:
            return int(mc.player.getPos().z)
        else:
            invalid(super)
            return -1024
    elif argv.startswith("playerName"):
        if len(argv) == 10:
            return playerName
        else:
            invalid(super)
            return -1024
    elif argv.startswith("height("):
        if ("," in argv) and (argv.endswith(")")) and (len(argv) >= 11):
            argva = argv[7:argv.find(",")]
            argvb = argv[argv.find(",") + 1:-1]
            a = toint(argva, -128, 128, super)
            if a <= -257:
                return -1025
            b = toint(argvb, -128, 128, super)
            if b <= -257:
                return -1025
            return mc.getHeight(a, b)
        else:
            invalid(super)
            return -1024
    elif argv.startswith("gpiomode"):
        if len(argv) == 8:
            if RPi.GPIO.getmode() == RPi.GPIO.BCM:
                return "bcm"
            elif RPi.GPIO.getmode() == RPi.GPIO.BOARD:
                return "board"
            else:
                return "none"
        else:
            invalid(super)
            return -1024
    elif argv.startswith("random_int("):
        if ("," in argv) and (argv.endswith(")")) and (len(argv) >= 15):
            argva = argv[11:argv.find(",")]
            argvb = argv[argv.find(",") + 1:-1]
            a = toint(argva, -256, 256, super)
            if a <= -257:
                return -1024
            b = toint(argvb, -256, 256, super)
            if b <= -257:
                return -1024
            return random.randint(a, b)
        else:
            invalid(super)
            return -1024
    elif argv.startswith("random_float("):
        if ("," in argv) and (argv.endswith(")")) and (len(argv) >= 15):
            argva = argv[11:argv.find(",")]
            argvb = argv[argv.find(",") + 1:-1]
            a = tofloat(argva, super, "~")
            if a == "~":
                return -1024
            b = tofloat(argvb, super, "~")
            if b == "~":
                return -1024
            return random.uniform(a, b)
        else:
            invalid(super)
            return -1024
    else:
        invalid(super)
        return -1024


def sleep(args, super):
    if not (len(args) == 1):
        invalid(super)
        return
    sleepTime = tofloat(args[0], super)
    if sleepTime <= -1:
        return
    time.sleep(sleepTime / 20)


def gpio(args, super):
    if len(args) == 0:
        invalid(super)
        return
    if disablegpio:
        if not (super is None):
            trystop(super)
            chatWithSuper("Package \"RPi.GPIO\" is defined, \"/gpio\" is not available.", super)
            return
        print '\033[0;33;40m',
        print "Package \"RPi.GPIO\" is defined, \"/gpio\" is not available.",
        print '\033[0m'
        return
    if args[0] == "mode":
        if len(args) == 1:
            if super is None:
                print "bcm, board"
                return
            else:
                trystop(super)
                chatWithSuper("Cannot use /gpio mode in a function or a thread.", super)
                return
        if not (len(args) == 2):
            invalid(super)
            return
        try:
            if args[1] == "board":
                RPi.GPIO.setmode(RPi.GPIO.BOARD)
                chatWithSuper("Changed GPIO mode to BOARD successfully.", super)
            elif args[1] == "bcm":
                RPi.GPIO.setmode(RPi.GPIO.BCM)
                chatWithSuper("Changed GPIO mode to BCM successfully.", super)
            else:
                invalid(super)
                return
        except ValueError:
            if not (super is None):
                trystop(super)
                chatWithSuper("A different mode has already been set.", super)
                return
            print '\033[0;31;40m',
            print "A different mode has already been set.",
            print '\033[0m'
            return
    elif args[0] == "cleanup":
        if not (len(args) == 2):
            invalid(super)
            return
        channel = toint(args[1], 0, 29, super)
        if channel <= -1:
            return
        RPi.GPIO.cleanup(channel)
        chatWithSuper("Cleaned up Channel " + args[1] + " successfully.", super)
    elif args[0] == "cleanupAll":
        if not (len(args) == 1):
            invalid(super)
            return
        RPi.GPIO.cleanup()
        chatWithSuper("Cleaned up channels successfully.", super)
    elif args[0] == "setup":
        if not (len(args) == 3):
            invalid(super)
            return
        mode = RPi.GPIO.IN
        if args[2] == "out":
            mode = RPi.GPIO.OUT
        elif not (args[2] == "in"):
            invalid(super)
            return
        channel = toint(args[1], 0, 29, super)
        if channel <= -1:
            return
        RPi.GPIO.setup(channel, mode)
        chatWithSuper("Sat up Channel " + args[1] + " successfully.", super)
    elif args[0] == "output":
        if not (len(args) == 3):
            invalid(super)
            return
        mode = RPi.GPIO.LOW
        if args[2] == "high":
            mode = RPi.GPIO.HIGH
        elif not (args[2] == "low"):
            invalid(super)
            return
        channel = toint(args[1], 0, 29, super)
        if channel <= -1:
            return
        RPi.GPIO.output(channel, mode)
        chatWithSuper("Sat Channel " + args[1] + "\'s output to " + args[2] + " successfully.", super)
    else:
        invalid(super)
        return


def function(args, super):
    global commandLines
    if not (len(args) == 1):
        invalid(super)
        return
    if ":" in args[0]:
        namespace = args[0][0:args[0].find(":")] + "/"
    else:
        namespace = ""
    functionName = args[0][args[0].find(":") + 1:]
    if namespace == "" or os.path.isdir("functions/" + namespace):
        if os.path.isfile("functions/" + namespace + functionName + ".mcpifunction"):
            try:
                functionfile = open("functions/" + namespace + functionName + ".mcpifunction", 'r')
                commandLines = functionfile.readlines()
                functionfile.close()
            except EOFError, arg:
                (errno, err_msg) = arg
                if super is None:
                    print '\033[0;31;40m',
                    print "Cannot open file: %s, errno=%d" % (err_msg, errno),
                    print '\033[0m'
                    return
                trystop(super)
                chatWithSuper("Cannot open file: " + err_msg + ", errno=" + errno, super)
            except IOError, arg:
                (errno, err_msg) = arg
                if super is None:
                    print '\033[0;31;40m',
                    print "Cannot open file: %s, errno=%d" % (err_msg, errno),
                    print '\033[0m'
                    return
                trystop(super)
                chatWithSuper("Cannot open file: " + err_msg + ", errno=" + errno, super)
            if super is None:
                funSuper = "f_" + functionName
            else:
                funSuper = super + ".f_" + functionName
            chatWithSuper("Function " + functionName + " started to run.", super)
            errorlevel = 0
            for command in commandLines:
                command = command.strip()
                if not len(command) or command.startswith('#'):
                    continue
                if command.startswith("exit"):
                    if len(command) == 4:
                        break
                    elif len(command) >= 6 and command.startswith("exit "):
                        errorlevel = toint(command[5:], -256, 256, funSuper)
                        if errorlevel <= -257:
                            invalid(funSuper)
                        break
                readCommand(command, funSuper)
            if errorlevel == 0:
                chatWithSuper("Function " + functionName + " succeed.", super)
            else:
                chatWithSuper("Function " + functionName + " failed: " + str(errorlevel) + ".", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Cannot open file: function doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Cannot open file: function doesn't exists.", super)
    else:
        if super is None:
            print '\033[0;31;40m',
            print "Cannot open file: namespace doesn't exists.",
            print '\033[0m'
            return
        trystop(super)
        chatWithSuper("Cannot open file: namespace doesn't exists.", super)


def tocommand(args):
    command = merge(args)
    if command[1] == "/":
        command = command[2:]
    else:
        command = command[1:]
    return command


def camera(args, super):
    if len(args) == 0:
        invalid(super)
        return
    if args[0] == "normal":
        if len(args) == 1:
            mc.camera.setNormal()
            chatWithSuper("Sat camera mode to normal Minecraft view successfully.", super)
        elif len(args) == 2:
            entityId = toint(args[1], 0, 2147483647, super)
            if entityId == -1:
                return
            mc.camera.setNormal(entityId)
            chatWithSuper("Sat camera mode to normal Minecraft view (" + args[1] +") successfully.", super)
        else:
            invalid(super)
            return
    elif args[0] == "fixed":
        if not (len(args) == 1):
            invalid(super)
            return
        mc.camera.setFixed()
        chatWithSuper("Sat camera mode to fixed view successfully.", super)
    elif args[0] == "follow":
        if len(args) == 1:
            mc.camera.setFollow()
            chatWithSuper("Sat camera to follow view successfully.", super)
        elif len(args) == 2:
            entityId = toint(args[1], 0, 2147483647, super)
            if entityId == -1:
                return
            mc.camera.setFollow(entityId)
            chatWithSuper("Sat camera mode to follow Entity " + args[1] + " successfully.", super)
        else:
            invalid(super)
            return
    elif args[0] == "pos":
        if not (len(args) == 4):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], True, super)
        mc.camera.setPos(vec[0], vec[1], vec[2])
        chatWithSuper("Set camera entity position (" + args[1] + "," + args[2] + ", " + args[3] + ") successfully.", super)
    else:
        invalid(super)
        return


def thread(args, super):
    if len(args) == 0:
        invalid(super)
    elif args[0] == "add":
        if len(args) < 5:
            invalid(super)
            return
        name = args[1]
        if len(name) == 0:
            invalid(super)
            return
        if len(name) > 15:
            if super is None:
                print '\033[0;31;40m',
                print "The name you have entered (" + name + ") is too long, it must be at longest 15",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("The name you have entered (" + name + ") is too long, it must be at longest 15", super)
            return
        if name in threads.keys():
            if super is None:
                print '\033[0;31;40m',
                print "Thread " + name + " already exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Thread " + name + " already exists.", super)
            return
        cycle = tobool(args[2], super)
        if cycle <= -1:
            return
        sleep = toint(args[3], 0, 2147483647, super)
        if sleep <= -1:
            return
        command = tocommand(args[4:])
        if super is None:
            threads[name] = CommandThread("t_" + name, cycle, command, float(sleep / 20))
        else:
            threads[name] = CommandThread(super + ".t_" + name, cycle, command, float(sleep / 20))
        threads[name].start()
        chatWithSuper("Created Thread " + name + " successfully.", super)
    elif args[0] == "start":
        if not len(args) == 2:
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        chatWithSuper("Thread " + name + " is running now.", super)
        threads[name].continuethread()
    elif args[0] == "stop":
        if not len(args) == 2:
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        threads[name].setpause()
        chatWithSuper("Thread " + name + " is stoped.", super)
    elif args[0] == "remove":
        if not len(args) == 2:
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        threads[name].stop()
        del threads[name]
        chatWithSuper("Removed Thread " + name + ".", super)
    elif args[0] == "list":
        if not (len(args) == 1):
            invalid(super)
            return
        if not (super is None):
            trystop(super)
            chatWithSuper("Cannot use /thread list in a function or a thread.", super)
            return
        print '\033[0;32;40m', "-------- Showing list of threads --------"
        print " Thread Name     Status", '\033[0m'
        for threadname in threads.keys():
            print " " + threadname.ljust(15),
            if threads[threadname].ispause():
                print "Stoped"
            else:
                print "Running"
    elif args[0] == "removeAll":
        for name in threads.keys():
            threads[name].stop()
            del threads[name]
        chatWithSuper("Cleared threads.", super)
    elif args[0] == "setsleep":
        if not (len(args) == 3):
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        sleep = toint(args[2], 0, 2147483647, super)
        if sleep <= -1:
            return
        threads[name].setsleep(float(sleep / 20))
        chatWithSuper("Sat Thread " + name + "\'s sleep to " + args[2] + ".", super)
    elif args[0] == "setcycle":
        if not (len(args) == 3):
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        cycle = tobool(args[2], super)
        if cycle <= -1:
            return
        threads[name].setcycle(cycle)
        chatWithSuper("Sat Thread " + name + "\'s cycle to " + args[2] + ".", super)
    else:
        invalid(super)


def superoutput(super):
    if "." in super:
        threadname = super[2:super.find(".") + 1]
        fun = superoutput(super[super.find(".") + 1:])
        return threadname + fun
    else:
        return super[2:]


def trystop(super):
    super = super + "."
    if "t_" in super:
        threads[super[super.rfind("t_") + 2 : super.find(".", super.rfind("t_"))]].setpause()


def chatWithSuper(msg, super, ismsg = True):
    if (not ismsg) or msgChat:
        if super is None:
            mc.postToChat(msg)
        else:
            mc.postToChat("[" + superoutput(super) + "] " + msg)


class CommandThread(threading.Thread):
    def __init__(self, name, cycle, command, sleep):
        threading.Thread.__init__(self)
        self.name = name
        self.cycle = cycle
        self.command = command
        self.sleep = sleep
        self.pause = True
        self.delete = False

    def run(self):
        while not self.delete:
            if not self.pause:
                readCommand(self.command, self.name)
                time.sleep(self.sleep)
                if not self.cycle:
                    self.setpause()

    def continuethread(self):
        self.pause = False

    def setpause(self):
        self.pause = True

    def setsleep(self, sleep):
        self.sleep = sleep

    def ispause(self):
        return self.pause

    def stop(self):
        self.delete = True

    def setcycle(self, cycle):
        self.cycle = cycle


def getrotate(yaw, pitch, roll, super):
    rotate = [0, 0, 0]
    try:
        rotate[0] = float(yaw)
        rotate[1] = float(pitch)
        rotate[2] = float(roll)
        return rotate
    except ValueError:
        invalid(super)
        return False


def shape(args, super):
    global shapeblocks
    if disablems:
        if not (super is None):
            trystop(super)
            chatWithSuper("Package \"minecraftstuff\" is defined, \"/shape\" is not available.", super)
            return
        print '\033[0;33;40m',
        print "Package \"minecraftstuff\" is defined, \"/shape\" is not available.",
        print '\033[0m'
        return
    if len(args) == 0:
        invalid(super)
        return
    if args[0] == "add":
        if not (len(args) == 5 or len(args) == 6 or len(args) == 12):
            invalid(super)
            return
        name = args[1]
        if len(name) == 0:
            invalid(super)
            return
        if len(name) > 15:
            if super is None:
                print '\033[0;31;40m',
                print "The name you have entered (" + name + ") is too long, it must be at longest 15",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("The name you have entered (" + name + ") is too long, it must be at longest 15", super)
            return
        if name in mcshapes.keys():
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + name + " already exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + name + " already exists.", super)
            return
        vec = getvec(args[2], args[3], args[4], False, super)
        if not vec:
            return
        if len(args) > 5:
            visible = tobool(args[5], super)
            if visible <= -1:
                return
            if len(args) == 11:
                vecB = getvec(args[6], args[7], args[8], False, super)
                if not vecB:
                    return
                vecE = getvec(args[9], args[10], args[11], False, super)
                if not vecE:
                    return
                shapeblocks = mc.getBlocks(vecB[0], vecB[1], vecB[2], vecE[0], vecE[1], vecE[2])
            else:
                shapeblocks = None
        else:
            visible = True
        mcshapes[name] = minecraftstuff.MinecraftShape(mc, minecraft.Vec3(vec[0], vec[1], vec[2]), shapeblocks, visible)
        chatWithSuper("Created Shape " + name +" successfully.", super)
    elif args[0] == "clearAll":
        if not (len(args) == 1):
            invalid(super)
            return
        for shape in mcshapes:
            shape.clear()
        chatWithSuper("Cleared all shapes successfully.", super)
    elif args[0] == "clear":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcshapes:
            mcshapes[args[1]].clear()
            chatWithSuper("Cleared Shape " + args[1] + " successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "draw":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcshapes:
            mcshapes[args[1]].draw()
            chatWithSuper("Drew Shape " + args[1] + " successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "move":
        if not (len(args) == 5):
            invalid(super)
            return
        if args[1] in mcshapes:
            vec = getvec(args[2], args[3], args[4], False, super)
            if not vec:
                return
            mcshapes[args[1]].move(vec[0], vec[1], vec[2])
            chatWithSuper("Moved Shape " + args[1] + " to (" + args[2] + ", " + args[3] + ", " + args[4] + ") successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "moveBy":
        if not (len(args) == 5):
            invalid(super)
            return
        if args[1] in mcshapes:
            vec = getvec(args[2], args[3], args[4], False, super)
            if not vec:
                return
            mcshapes[args[1]].moveBy(vec[0], vec[1], vec[2])
            chatWithSuper("Moved Shape " + args[1] + " by (" + args[2] + ", " + args[3] + ", " + args[4] + ") successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "redraw":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcshapes:
            mcshapes[args[1]].redraw()
            chatWithSuper("Redrew Shape " + args[1] + " successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "reset":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcshapes:
            mcshapes[args[1]].reset()
            chatWithSuper("Resat Shape " + args[1] + " successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "rotate":
        if not (len(args) == 5):
            invalid(super)
            return
        if args[1] in mcshapes:
            vec = getrotate(args[2], args[3], args[4], super)
            if not vec:
                return
            mcshapes[args[1]].rotate(vec[0], vec[1], vec[2])
            chatWithSuper(
                "Sat the rotate of Shape " + args[1] + " to (" + args[2] + ", " + args[3] + ", " + args[4] + ") successfully.",
                super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "rotateBy":
        if not (len(args) == 5):
            invalid(super)
            return
        if args[1] in mcshapes:
            vec = getrotate(args[2], args[3], args[4], super)
            if not vec:
                return
            mcshapes[args[1]].rotateBy(vec[0], vec[1], vec[2])
            chatWithSuper(
                "Sat the rotate of Shape " + args[1] + " by (" + args[2] + ", " + args[3] + ", " + args[4] + ") successfully.",
                super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "setblock":
        if not (len(args) == 5 or len(args) == 6):
            invalid(super)
            return
        if args[1] in mcshapes:
            vec = getvec(args[2], args[3], args[4], False, super)
            if not vec:
                return
            else:
                if len(args) == 7:
                    special = toint(args[6], 0, 15, super)
                    if special <= -1:
                        return
                else:
                    special = 0
                block = getblock(args[5], super)
                if block <= -1:
                    return
                mcshapes[args[1]].setBlock(vec[0], vec[1], vec[2], block, special)
                chatWithSuper("Shape-block placed", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "fill" or args[0] == "setblocks":
        if not (len(args) == 9 or len(args) == 10):
            invalid(super)
            return
        if args[1] in mcshapes:
            vecB = getvec(args[2], args[3], args[4], False, super)
            if not vecB:
                return
            vecE = getvec(args[5], args[6], args[7], False, super)
            if not vecE:
                return
            blockCount = (abs(vecB[0] - vecE[0]) + 1) * (abs(vecB[1] - vecE[1]) + 1) * (abs(vecB[2] - vecE[2]) + 1)
            if len(args) == 10:
                special = toint(args[9], 0, 15, super)
                if special <= -1:
                    return
            else:
                special = 0
            block = getblock(args[8], super)
            if block <= -1:
                return
            mcshapes[args[1]].setBlocks(vecB[0], vecB[1], vecB[2], vecE[0], vecE[1], vecE[2], block, special)
            chatWithSuper(str(blockCount) + " shape-blocks filled", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "removeAll":
        if not (len(args) == 1):
            invalid(super)
            return
        mcshapes.clear()
        chatWithSuper("Removed all shapes successfully.", super)
    elif args[0] == "remove":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcshapes:
            del mcshapes[args[1]]
            chatWithSuper("Removed Shape " + args[1] + " successfully.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Shape " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Shape " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "list":
        if not (len(args) == 1):
            invalid(super)
            return
        if not (super is None):
            trystop(super)
            chatWithSuper("Cannot use /shape list in a function or a thread.", super)
            return
        print '\033[0;32;40m', "-------- Showing list of Shapes --------"
        for shapename in mcshapes.keys():
            print " " + shapename
    else:
        invalid(super)


def tofloat(argv, super, errorback = -1):
    try:
        return float(argv)
    except ValueError:
        invalid(super)
        return errorback


def turtle(args, super):
    if disablems:
        if not (super is None):
            trystop(super)
            chatWithSuper("Package \"minecraftstuff\" is defined, \"/turtle\" is not available.", super)
            return
        print '\033[0;33;40m',
        print "Package \"minecraftstuff\" is defined, \"/turtle\" is not available.",
        print '\033[0m'
        return
    if len(args) == 0:
        invalid(super)
        return
    if args[0] == "add":
        if not (len(args) == 5 or len(args) == 2):
            invalid(super)
            return
        name = args[1]
        if len(name) == 0:
            invalid(super)
            return
        if len(name) > 15:
            if super is None:
                print '\033[0;31;40m',
                print "The name you have entered (" + name + ") is too long, it must be at longest 15",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("The name you have entered (" + name + ") is too long, it must be at longest 15", super)
            return
        if name in mcturtles.keys():
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + name + " already exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + name + " already exists.", super)
            return
        if len(args) == 5:
            vec = getvec(args[2], args[3], args[4], False, super)
            if not vec:
                return
        else:
            vec = [0, 0, 0]
        mcturtles[name] = minecraftstuff.MinecraftTurtle(mc, minecraft.Vec3(vec[0], vec[1], vec[2]))
        chatWithSuper("Created Turtle " + name + " successfully.", super)
    elif args[0] == "backward":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            disance = toint(args[2], 0, 256, super)
            if disance <= -1:
                return
            mcturtles[args[1]].backward(disance)
            chatWithSuper("Moved Turtle " + args[1] + " backward by " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "down":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            angle = tofloat(args[2], super)
            if angle <= -1:
                return
            mcturtles[args[1]].down(angle)
            chatWithSuper("Rotated Turtle " + args[1] + " down by " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "fly":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            mcturtles[args[1]].fly()
            chatWithSuper("Sat Turtle " + args[1] + " fly.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "forward":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            disance = toint(args[2], 0, 256, super)
            if disance <= -1:
                return
            mcturtles[args[1]].forward(disance)
            chatWithSuper("Moved Turtle " + args[1] + " forward by " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "home":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            mcturtles[args[1]].home()
            chatWithSuper("Resat Turtle " + args[1] + "\'s position.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "left":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            angle = tofloat(args[2], super)
            if angle <= -1:
                return
            mcturtles[args[1]].left(angle)
            chatWithSuper("Rotated Turtle " + args[1] + " left by " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "penblock":
        if not (len(args) == 3 or len(args) == 4):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            block = getblock(args[2], super)
            if block <= -1:
                return
            if len(args) == 4:
                special = toint(args[3], 0, 15, super)
                if special <= -1:
                    return
            else:
                special = 0
            mcturtles[args[1]].penblock(block, special)
            chatWithSuper("Sat Turtle " + args[1] + "\'s pen to Block (" + args[2] + ", " + str(special) + ") .", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "pendown":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            mcturtles[args[1]].pendown()
            chatWithSuper("Put Turtle " + args[1] + "\'s pen down.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "penup":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            mcturtles[args[1]].penup()
            chatWithSuper("Put Turtle " + args[1] + "\'s pen up.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "right":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            angle = tofloat(args[2], super)
            if angle <= -1:
                return
            mcturtles[args[1]].right(angle)
            chatWithSuper("Rotated Turtle " + args[1] + " right by " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "setHorizontalHeading":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            angle = tofloat(args[2], super)
            if angle <= -1:
                return
            mcturtles[args[1]].setheading(angle)
            chatWithSuper("Sat Turtle " + args[1] + "\'s horizontal heading to " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "setVerticalHeading":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            angle = tofloat(args[2], super)
            if angle <= -1:
                return
            mcturtles[args[1]].setverticalheading(angle)
            chatWithSuper("Sat Turtle " + args[1] + "\'s vertical heading to " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "setposition":
        if not (len(args) == 5):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            vec = getvec(args[2], args[3], args[4], False, super)
            if not vec:
                return
            mcturtles[args[1]].setposition(vec[0], vec[1], vec[2])
            chatWithSuper("Sat Turtle " + args[1] + "\'s position to (" + args[2] + ", " + args[3] + ", " + args[4] + ") .", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "setx":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            pos = toint(args[2], -128, 128, super)
            if pos <= -256:
                return
            mcturtles[args[1]].setx(pos)
            chatWithSuper("Sat Turtle " + args[1] + "\'s x position to " + args[2] + ".", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "sety":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            pos = toint(args[2], -64, 64, super)
            if pos <= -1:
                return
            mcturtles[args[1]].sety(pos)
            chatWithSuper("Sat Turtle " + args[1] + "\'s y position to " + args[2] + ".", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "setz":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            pos = toint(args[2], -128, 128, super)
            if pos <= -256:
                return
            mcturtles[args[1]].setz(pos)
            chatWithSuper("Sat Turtle " + args[1] + "\'s z position to " + args[2] + ".", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "speed":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            speed = toint(args[2], 0, 10, super)
            if speed <= -1:
                return
            mcturtles[args[1]].speed(speed)
            chatWithSuper("Sat Turtle " + args[1] + "\'s speed to " + args[2] + ".", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "up":
        if not (len(args) == 3):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            angle = tofloat(args[2], super)
            if angle <= -1:
                return
            mcturtles[args[1]].up(angle)
            chatWithSuper("Rotated Turtle " + args[1] + " up by " + args[2], super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "walk":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            mcturtles[args[1]].walk()
            chatWithSuper("Sat Turtle " + args[1] + " walk.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "remove":
        if not (len(args) == 2):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            del mcturtles[args[1]]
            chatWithSuper("Removed Turtle " + args[1] + ".", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "removeAll":
        if not (len(args) == 1):
            invalid(super)
            return
        if args[1] in mcturtles.keys():
            mcturtles.clear()
            chatWithSuper("Removed all turtles.", super)
        else:
            if super is None:
                print '\033[0;31;40m',
                print "Turtle " + args[1] + " doesn't exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Turtle " + args[1] + " doesn't exists.", super)
            return
    elif args[0] == "list":
        if not (len(args) == 1):
            invalid(super)
            return
        if not (super is None):
            trystop(super)
            chatWithSuper("Cannot use /turtle list in a function or a thread.", super)
            return
        print '\033[0;32;40m', "-------- Showing list of threads --------"
        print " Turtle Name     Pen Status", '\033[0m'
        for turtle in mcturtles.keys():
            print " " + turtle.ljust(15),
            if mcturtles[turtle].isdown():
                print "Down"
            else:
                print "Up"


def draw(args, super):
    if disablems:
        if not (super is None):
            trystop(super)
            chatWithSuper("Package \"minecraftstuff\" is defined, \"/draw\" is not available.", super)
            return
        print '\033[0;33;40m',
        print "Package \"minecraftstuff\" is defined, \"/draw\" is not available.",
        print '\033[0m'
        return
    if len(args) == 0:
        invalid(super)
        return
    if args[0] == "circle":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawCircle(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew circle successfully.", super)
    elif args[0] == "face":
        blocklist = []
        if len(args) >= 7 and not ((len(args) - 4) % 3):
            filled = tobool(args[-3], super)
            if filled <= -1:
                return
            block = getblock(args[-2], super)
            if block <= -1:
                return
            special = toint(args[-1], 0, 15, super)
            if special <= -1:
                return
            times = (len(args) - 4) / 3
        elif len(args) >= 6 and not ((len(args) - 3) % 3):
            filled = tobool(args[-2], super)
            if filled <= -1:
                return
            block = getblock(args[-1], super)
            if block <= -1:
                return
            special = 0
            times = (len(args) - 3) / 3
        else:
            invalid(super)
            return
        time = 1
        while time <= times:
            veclist = getvec(args[time * 3 - 2], args[time * 3 - 1], args[time * 3], False, super)
            if not veclist:
                return
            blocklist.append(vec3.Vec3(veclist[0], veclist[1], veclist[2]))
            time += 1
        mcdraw.drawFace(blocklist, filled, block, special)
        chatWithSuper("Drew face successfully.", super)
    elif args[0] == "hollowSphere":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawHollowSphere(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew hollow sphere successfully.", super)
    elif args[0] == "horizontalCircle":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawHorizontalCircle(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew circle successfully.", super)
    elif args[0] == "line":
        if not (len(args) == 8 or len(args) == 9):
            invalid(super)
            return
        vecB = getvec(args[1], args[2], args[3], False, super)
        if not vecB:
            return
        vecE = getvec(args[4], args[5], args[6], False, super)
        if not vecE:
            return
        block = getblock(args[7], super)
        if block <= -1:
            return
        if len(args) == 9:
            special = toint(args[8], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawLine(vecB[0], vecB[1], vecB[2], vecE[0], vecE[1], vecE[2], block, special)
        chatWithSuper("Drew line successfully.", super)
    elif args[0] == "point":
        if not (len(args) == 5 or len(args) == 6):
            invalid(super)
        else:
            vec = getvec(args[1], args[2], args[3], False, super)
            if not vec:
                return
            else:
                if len(args) == 6:
                    special = toint(args[5], 0, 15, super)
                    if special <= -1:
                        return
                else:
                    special = 0
                block = getblock(args[4], super)
                if block <= -1:
                    return
                mc.setBlock(vec[0], vec[1], vec[2], block, special)
                chatWithSuper("Drew point successfully.", super)
    elif args[0] == "sphere":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawSphere(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew sphere successfully.", super)
    elif args[0] == "vertices":
        blocklist = []
        if len(args) >= 6 and not ((len(args) - 3) % 3):
            block = getblock(args[-2], super)
            if block <= -1:
                return
            special = toint(args[-1], 0, 15, super)
            if special <= -1:
                return
            times = (len(args) - 3) / 3
        elif len(args) >= 5 and not ((len(args) - 2) % 3):
            block = getblock(args[-1], super)
            if block <= -1:
                return
            special = 0
            times = (len(args) - 2) / 3
        else:
            invalid(super)
            return
        time = 1
        while time <= times:
            veclist = getvec(args[time * 3 - 2], args[time * 3 - 1], args[time * 3], False, super)
            if not veclist:
                return
            blocklist.append(vec3.Vec3(veclist[0], veclist[1], veclist[2]))
            time += 1
        mcdraw.drawVertices(blocklist, block, special)
        chatWithSuper("Drew vertices successfully.", super)
    else:
        invalid(super)


def setting(args, super):
    if not (len(args) == 0 or len(args) == 2):
        invalid(super)
    else:
        if len(args) == 0:
            if super is None:
                print "autojump, nametags_visible, world_immutable, exec_message"
            else:
                trystop(super)
                chatWithSuper("Cannot use /setting in a function or a thread.", super)
                return
        else:
            setting = tobool(args[1], super)
            if setting <= -1:
                return
            if args[0] == "autojump":
                mc.player.setting("autojump", setting)
            elif args[0] == "nametags_visible":
                mc.setting("nametags_visible", setting)
            elif args[0] == "world_immutable":
                mc.setting("world_immutable", setting)
            elif args[0] == "exec_message":
                global msgChat
                msgChat = setting
            else:
                invalid(super)
                return
            chatWithSuper("Changed the " + args[0] + " setting to " + args[1], super)


def clear(args, super):
    if not (super is None):
        trystop(super)
        chatWithSuper("Cannot use /clear in a function or a thread.", super)
        return
    if not (len(args) == 0):
        invalid(None)
    else:
        os.system("clear")


def help(args, super):
    global page
    if not (super is None):
        trystop(super)
        chatWithSuper("Cannot use /help in a function or a thread.", super)
        return
    if not (len(args) == 1 or len(args) == 0):
        invalid(None)
    else:
        list = True
        try:
            if len(args) == 0:
                page = 1
            else:
                page = int(args[0])
            if page > helpPageCount:
                page = helpPageCount
            elif page < 1:
                page = 1
        except ValueError:
            list = False
            if args[0] == "say":
                print '\033[0;33;40m',
                print "say:"
                print " Sends a message in the chat to other players."
                print '\033[0m',
                print "Usage:"
                print " - /say <message: string>"
            elif args[0] == "tp":
                print '\033[0;33;40m',
                print "tp:"
                print " Teleports player."
                print '\033[0m',
                print "Usage:"
                print " - /tp <destination: x y z>"
            elif args[0] == "me":
                print '\033[0;33;40m',
                print "me:"
                print " Makes an action to others."
                print '\033[0m',
                print "Usage:"
                print " - /me <action: string>"
            elif args[0] == "setblock":
                print '\033[0;33;40m',
                print "setblock:"
                print " Changes a block to another block."
                print '\033[0m',
                print "Usages:"
                print " - /setblock <position: x y z> <tileName: string> [tileData: int]"
                print " - /setblock <position: x y z> <tileId: int> [tileData: int]"
            elif args[0] == "fill" or args[0] == "setblocks":
                print '\033[0;33;40m',
                print "fill(setblocks):"
                print " Fills all of a region with a specific block."
                print '\033[0m',
                print "Usage:"
                print " - /fill <from: x y z> <to: x y z> <tileName: string> [tileData: int]"
                print " - /fill <from: x y z> <to: x y z> <tileId: int> [tileData: int]"
            elif args[0] == "help":
                print '\033[0;33;40m',
                print "help:"
                print " Provides help/list of commands."
                print '\033[0m',
                print "Usage:"
                print " - /help <command: string>"
                print " - /help [page: int]"
            elif args[0] == "setplayername":
                print '\033[0;33;40m',
                print "setplayername:"
                print " Changes the player\'s name to another name."
                print '\033[0m',
                print "Usage:"
                print " - /setplayername [newPlayerName: string]"
            elif args[0] == "clear":
                print '\033[0;33;40m',
                print "clear:"
                print " Clears the screen of terminal."
                print '\033[0m',
                print "Usage:"
                print " - /clear"
            elif args[0] == "setting":
                print '\033[0;33;40m',
                print "setting:"
                print " Set a setting."
                print '\033[0m',
                print "Usage:"
                print " - /setting"
                print " - /setting <setting: string> <status: bool>"
            elif args[0] == "if":
                print '\033[0;33;40m',
                print "if:"
                print " Do something if condition is established."
                print '\033[0m',
                print "Usage:"
                print " - /if $<selector: string> < = | < | > | <= | >= > <thingToCompare: sameTypeAsSelector> <command: string>"
            elif args[0] == "loop":
                print '\033[0;33;40m',
                print "loop:"
                print " Do something repeated."
                print '\033[0m',
                print "Usage:"
                print " - /loop if $<selector: string> < = | < | > | <= | >= > <thingToCompare: sameTypeAsSelector> <command: string>"
                print " - /loop times <repeatTimes: int> <command: string>"
            elif args[0] == "draw":
                print '\033[0;33;40m',
                print "draw:"
                print " Draws some shapes made of blocks."
                if disablems:
                    print '\033[0;33;40m', "Tip: this command is now unavailable."
                print '\033[0m',
                print "Usage:"
                print " - /draw circle <position: x0 y0 z> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw face <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <filled: bool> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw hollowSphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw horizontalCircle <position: x0 y z0> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw line <position1: x1 y1 z1> <position2: x2 y2 z2> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw point <position: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw sphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw vertices <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <tileName: string | tileId: int> [tileData: int]"
            elif args[0] == "shape":
                print '\033[0;33;40m',
                print "shape:"
                print " Creates and manipulates shapes."
                if disablems:
                    print '\033[0;33;40m', "Tip: this command is now unavailable."
                print '\033[0m',
                print "Usage:"
                print " - /shape add <shapeName: string> <position: x y z> [visible: bool] [<shapeBlocksFrom: x1 y1 z1> <shapeBlocksTo: x2 y2 z2>]"
                print " - /shape clear <shapeName: string>"
                print " - /shape clearAll"
                print " - /shape draw <shapeName: string>"
                print " - /shape list"
                print " - /shape move <shapeName: string> <position: x y z>"
                print " - /shape moveBy <shapeName: string> <relativePosition: x0 y0 z0>"
                print " - /shape redraw <shapeName: string>"
                print " - /shape remove <shapeName: string>"
                print " - /shape removeAll"
                print " - /shape reset <shapeName: string>"
                print " - /shape rotate <x-rot: rotation> <y-rot: rotation> <z-rot: rotation>"
                print " - /shape rotateBy <relativeX-rot: rotation> <relativeY-rot: rotation> <relativeZ-rot: rotation>"
                print " - /shape setblock <position: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " - /shape fill | setblocks <from: x1 y1 z1> <to: x2 y2 z2> <tileName: string | tileId: int> [tileData: int]"
            elif args[0] == "turtle":
                print '\033[0;33;40m',
                print "turtle:"
                print " Creates and manipulates graphics turtle."
                if disablems:
                    print '\033[0;33;40m', "Tip: this command is now unavailable."
                print '\033[0m',
                print "Usage:"
                print " - /turtle add <turtleName: string> <position: x y z>"
                print " - /turtle backward <turtleName: string> <distance: int>"
                print " - /turtle down <turtleName: string> <angle: float>"
                print " - /turtle fly <turtleName: string>"
                print " - /turtle forward <turtleName: string> <distance: int>"
                print " - /turtle home <turtleName: string>"
                print " - /turtle left <turtleName: string> <angle: float>"
                print " - /turtle list"
                print " - /turtle penblock <turtleName: string> <tileName: string | tileId: int> [tileData: int]"
                print " - /turtle pendown <turtleName: string>"
                print " - /turtle penup <turtleName: string>"
                print " - /turtle remove <turtleName: string>"
                print " - /turtle removeAll"
                print " - /turtle right <turtleName: string> <angle: float>"
                print " - /turtle setHorizontalHeading <turtleName: string> <angle: float>"
                print " - /turtle setposition <turtleName: string> <position: x y z>"
                print " - /turtle setVerticalHeading <turtleName: string> <angle: float>"
                print " - /turtle setx <turtleName: string> <x: int>"
                print " - /turtle sety <turtleName: string> <y: int>"
                print " - /turtle setz <turtleName: string> <z: int>"
                print " - /turtle speed <turtleName: string> <turtlespeed: int>"
                print " - /turtle up <turtleName: string> <angle: float>"
                print " - /turtle walk <turtleName: string>"
            elif args[0] == "thread":
                print '\033[0;33;40m',
                print "thread:"
                print " Creates and manipulates command threads."
                print '\033[0m',
                print "Usage:"
                print " - /thread add <threadName: string> <cycle: bool> <sleepTime: int> <command: stirng>"
                print " - /thread list"
                print " - /thread remove <threadName: string>"
                print " - /thread removeAll"
                print " - /thread setcycle <threadName: string> <cycle: bool>"
                print " - /thread setsleep <threadName: string> <sleepTime: int>"
                print " - /thread start <threadName: string>"
                print " - /thread stop <threadName: string>"
            elif args[0] == "camera":
                print '\033[0;33;40m',
                print "camera:"
                print " Changes camera mode."
                print '\033[0m',
                print "Usage:"
                print " - /camera fixed"
                print " - /camera follow [entityId: int]"
                print " - /camera normal [entityId: int]"
                print " - /camera pos <position: x y z>"
            elif args[0] == "function":
                print '\033[0;33;40m',
                print "function:"
                print " Runs a function in a file."
                print '\033[0m',
                print "Usage:"
                print " - /function [namespace: string]:<functionName: string>"
            elif args[0] == "exit":
                print '\033[0;33;40m',
                print "exit:"
                print " Stop running function."
                print '\033[0;34;40m', "This command is for function."
                print '\033[0m',
                print "Usage:"
                print " - /exit"
            elif args[0] == "sleep":
                print '\033[0;33;40m',
                print "sleep:"
                print " Delay for some time(for function and thread)."
                print '\033[0m',
                print "Usage:"
                print " - /sleep <delayTime: float>"
            elif args[0] == "gpio":
                print '\033[0;33;40m',
                print "gpio:"
                print " Manipulates gpios."
                if disablegpio:
                    print '\033[0;33;40m', "Tip: this command is now unavailable."
                print '\033[0m',
                print "Usage:"
                print " - /gpio cleanup <channel: int>"
                print " - /gpio cleanupAll"
                print " - /gpio mode [mode: string]"
                print " - /gpio output <channel: int> <high | low>"
                print " - /gpio setup <channel: int> <out | in>"
            elif args[0] == "/saywos":
                print '\033[0;33;40m',
                print "saywos:"
                print " Sends a message without sending super."
                print '\033[0m',
                print "Usage:"
                print " - /saywos <speaker: string> <message: string>"
            elif args[0] == "mewos":
                print '\033[0;33;40m',
                print "mewos:"
                print " Makes an action without sending super."
                print '\033[0m',
                print "Usage:"
                print " - /mewos <speaker: string> <action: string>"
            else:
                print '\033[0;31;40m',
                print "The command is defined.",
                print '\033[0m'
        if list:
            print '\033[0;32;40m',
            print "--- Showing help page " + str(page) + " of " + str(helpPageCount) + " (/help <page>) ---"
            if page == 1:
                print '\033[0m', "/camera fixed"
                print " /camera follow [entityId: int]"
                print " /camera normal [entityId: int]"
                print " /camera pos <position: x y z>"
                print " /clear"
                print " /fill <from: x y z> <to: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " /function [namespace: string]:<functionName: string>"
            elif page == 2:
                print '\033[0m', "/help [command: string | page: int]"
                print " /if $<selector: string> < = | < | > | <= | >= > <thingToCompare: sameTypeAsSelector> <command: string>"
                print " /loop if $<selector: string> < = | < | > | <= | >= > <thingToCompare: sameTypeAsSelector> <command: string>"
                print " /loop times <repeatTimes: int> <command: string>"
                print " /me <action: string>"
                print " /mewos <speaker: string> <action: string>"
                print " /say <message: string>"
            elif page == 3:
                print '\033[0m', " /saywos <speaker: string> <message: string>"
                print " /setblock <position: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " /setplayername [newPlayerName: string]"
                print " /setting [<setting: string> <status: bool>]"
                print " /sleep <delayTime: float>"
                print " /thread add <threadName: string> <cycle: bool> <sleepTime: int> <command: stirng>"
                print " /thread list"
            elif page == 4:
                print '\033[0m', "/thread remove <threadName: string>"
                print " /thread removeAll"
                print " /thread setsleep <threadName: string> <cycle: bool>"
                print " /thread setsleep <threadName: string> <sleepTime: int>"
                print " /thread start <threadName: string>"
                print " /thread stop <threadName: string>"
                print " /tp <destination: x y z>"
            elif page == 5:
                print '\033[0;33;40m', "/draw circle <position: x0 y0 z> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw face <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <filled: bool> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw hollowSphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw horizontalCircle <position: x0 y z0> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw line <position1: x1 y1 z1> <position2: x2 y2 z2> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw point <position: x y z> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw sphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
            elif page == 6:
                print '\033[0;33;40m', "/draw vertices <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/gpio cleanup <channel: int>", '\033[0m'
                print '\033[0;33;40m', "/gpio cleanupAll", '\033[0m'
                print '\033[0;33;40m', "/gpio mode [mode: string]", '\033[0m'
                print '\033[0;33;40m', "/gpio output <channel: int> <high | low>", '\033[0m'
                print '\033[0;33;40m', "/gpio setup <channel: int> <out | in>", '\033[0m'
                print '\033[0;33;40m', "/shape add <shapeName: string> <position: x y z> [visible: bool] [<shapeBlocksFrom: x1 y1 z1> <shapeBlocksTo: x2 y2 z2>]", '\033[0m'
            elif page == 7:
                print '\033[0;33;40m', "/shape clear <shapeName: string>", '\033[0m'
                print '\033[0;33;40m', "/shape clearAll", '\033[0m'
                print '\033[0;33;40m', "/shape draw <shapeName: string>", '\033[0m'
                print '\033[0;33;40m', "/shape list", '\033[0m'
                print '\033[0;33;40m', "/shape move <shapeName: string> <position: x y z>", '\033[0m'
                print '\033[0;33;40m', "/shape moveBy <shapeName: string> <relativePosition: x0 y0 z0>", '\033[0m'
                print '\033[0;33;40m', "/shape redraw <shapeName: string>", '\033[0m'
            elif page == 8:
                print '\033[0;33;40m', "/shape remove <shapeName: string>", '\033[0m'
                print '\033[0;33;40m', "/shape removeAll", '\033[0m'
                print '\033[0;33;40m', "/shape reset <shapeName: string>", '\033[0m'
                print '\033[0;33;40m', "/shape rotate <x-rot: rotation> <y-rot: rotation> <z-rot: rotation>", '\033[0m'
                print '\033[0;33;40m', "/shape rotateBy <relativeX-rot: rotation> <relativeY-rot: rotation> <relativeZ-rot: rotation>", '\033[0m'
                print '\033[0;33;40m', "/shape setblock <position: x y z> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/shape fill | setblocks <from: x1 y1 z1> <to: x2 y2 z2> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
            elif page == 9:
                print '\033[0;33;40m', "/turtle add <turtleName: string> <position: x y z>", '\033[0m'
                print '\033[0;33;40m', "/turtle backward <turtleName: string> <distance: int>", '\033[0m'
                print '\033[0;33;40m', "/turtle down <turtleName: string> <angle: float>", '\033[0m'
                print '\033[0;33;40m', "/turtle fly <turtleName: string>", '\033[0m'
                print '\033[0;33;40m', "/turtle forward <turtleName: string> <distance: int>", '\033[0m'
                print '\033[0;33;40m', "/turtle home <turtleName: string>", '\033[0m'
                print '\033[0;33;40m', "/turtle left <turtleName: string> <angle: float>", '\033[0m'
            elif page == 10:
                print '\033[0;33;40m', "/turtle list", '\033[0m'
                print '\033[0;33;40m', "/turtle penblock <turtleName: string> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/turtle pendown <turtleName: string>", '\033[0m'
                print '\033[0;33;40m', "/turtle penup <turtleName: string>", '\033[0m'
                print '\033[0;33;40m', "/turtle remove <turtleName: string>", '\033[0m'
                print '\033[0;33;40m', "/turtle removeAll", '\033[0m'
                print '\033[0;33;40m', "/turtle right <turtleName: string> <angle: float>", '\033[0m'
            elif page == 11:
                print '\033[0;33;40m', "/turtle setHorizontalHeading <turtleName: string> <angle: float>", '\033[0m'
                print '\033[0;33;40m', "/turtle setposition <turtleName: string> <position: x y z>", '\033[0m'
                print '\033[0;33;40m', "/turtle setVerticalHeading <turtleName: string> <angle: float>", '\033[0m'
                print '\033[0;33;40m', "/turtle setx <turtleName: string> <x: int>", '\033[0m'
                print '\033[0;33;40m', "/turtle sety <turtleName: string> <y: int>", '\033[0m'
                print '\033[0;33;40m', "/turtle setz <turtleName: string> <z: int>", '\033[0m'
                print '\033[0;33;40m', "/turtle speed <turtleName: string> <turtlespeed: int>", '\033[0m'
            elif page == 12:
                print '\033[0;33;40m', "/turtle up <turtleName: string> <angle: float>", '\033[0m'
                print '\033[0;33;40m', "/turtle walk <turtleName: string>", '\033[0m'
                print '\033[0;34;40m', "/exit", '\033[0m'
            print '\033[0;32;40m', "Tip: " + '\033[0;33;40m' + "yellow" + '\033[0;32;40m' + " commands are add-ons' commands.", '\033[0m'
            print '\033[0;34;40m', "     " + "blue" + '\033[0;32;40m' + " commands are for function.", '\033[0m'


def setplayername(args, super):
    if not (len(args) == 1 or len(args) == 0):
        invalid(super)
    else:
        global playerName
        if len(args) == 1:
            playerName = args[0]
            if len(playerName) == 0:
                invalid(super)
                return
        else:
            playerName = "Player"
        chatWithSuper("Player\'s name changed to \"" + playerName + "\" successfully", super)


def merge(args):
    output = ""
    for argv in args:
        output += " " + argv
    return output


def say(args, super):
    if not (len(args) > 0):
        invalid(super)
    else:
        output = merge(args)
        if super is None:
            mc.postToChat("[" + playerName + "]" + output)
        else:
            chatWithSuper(output, super, False)


def me(args, super):
    if not (len(args) > 0):
        invalid(super)
    else:
        output = merge(args)
        if super is None:
            mc.postToChat("* " + playerName + output)
        else:
            mc.postToChat("* " + superoutput(super) + output)


def sayWithoutSuper(args, super):
    if not (len(args) > 1):
        invalid(super)
    else:
        output = merge(args[1:])
        mc.postToChat("[" + args[0] + "]" + output)


def meWithoutSuper(args, super):
    if not (len(args) > 1):
        invalid(super)
    else:
        output = merge(args[1:])
        mc.postToChat("* " + args[0] + output)


def teleport(args, super):
    if not (len(args) == 3):
        invalid(super)
    else:
        vec = getvec(args[0], args[1], args[2], True, super)
        if not vec:
            return
        else:
            mc.player.setTilePos(vec[0], vec[1], vec[2])
            chatWithSuper("Teleport Player to " + str(vec[0]) + ", " + str(vec[1]) + ", " + str(vec[2]), super)


def setblock(args, super):
    if not (len(args) == 4 or len(args) == 5):
        invalid(super)
    else:
        vec = getvec(args[0], args[1], args[2], False, super)
        if not vec:
            return
        else:
            if len(args) == 5:
                special = toint(args[4], 0, 15, super)
                if special <= -1:
                    return
            else:
                special = 0
            block = getblock(args[3], super)
            if block <= -1:
                return
            mc.setBlock(vec[0], vec[1], vec[2], block, special)
            chatWithSuper("Block placed", super)


def fill(args, super):
    if not (len(args) == 7 or len(args) == 8):
        invalid(super)
    else:
        vecB = getvec(args[0], args[1], args[2], False, super)
        if not vecB:
            return
        vecE = getvec(args[3], args[4], args[5], False, super)
        if not vecE:
            return
        blockCount = (abs(vecB[0] - vecE[0]) + 1) * (abs(vecB[1] - vecE[1]) + 1) * (abs(vecB[2] - vecE[2]) + 1)
        if len(args) == 8:
            special = toint(args[7], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        block = getblock(args[6], super)
        if block <= -1:
            return
        mc.setBlocks(vecB[0], vecB[1], vecB[2], vecE[0], vecE[1], vecE[2], block, special)
        chatWithSuper(str(blockCount) + " blocks filled", super)


def switchcommand(args, super):
    if args[0] == "say":
        say(args[1:], super)
    elif args[0] == "tp":
        teleport(args[1:], super)
    elif args[0] == "me":
        me(args[1:], super)
    elif args[0] == "setblock":
        setblock(args[1:], super)
    elif args[0] == "fill" or args[0] == "setblocks":
        fill(args[1:], super)
    elif args[0] == "help":
        help(args[1:], super)
    elif args[0] == "setplayername":
        setplayername(args[1:], super)
    elif args[0] == "clear":
        clear(args[1:], super)
    elif args[0] == "setting":
        setting(args[1:], super)
    elif args[0] == "draw":
        draw(args[1:], super)
    elif args[0] == "thread":
        thread(args[1:], super)
    elif args[0] == "camera":
        camera(args[1:], super)
    elif args[0] == "shape":
        shape(args[1:], super)
    elif args[0] == "turtle":
        turtle(args[1:], super)
    elif args[0] == "function":
        function(args[1:], super)
    elif args[0] == "sleep":
        sleep(args[1:], super)
    elif args[0] == "gpio":
        gpio(args[1:], super)
    elif args[0] == "loop":
        loop(args[1:], super)
    elif args[0] == "if":
        if ifdo(args[1:], super):
            chatWithSuper("The command had enforced.", super)
        else:
            chatWithSuper("The command had not enforced.", super)
    elif args[0] == "saywos":
        sayWithoutSuper(args[1:], super)
    elif args[0] == "mewos":
        meWithoutSuper(args[1:], super)
    else:
        if super is None:
            print '\033[0;31;40m',
            print "Unknown command. Try /help for a list of commands",
            print '\033[0m'
        else:
            trystop(super)
            chatWithSuper("Unknown command.", super)


def invalid(super):
    if super is None:
        print '\033[0;31;40m',
        print "Invalid command syntax",
        print '\033[0m'
    else:
        trystop(super)
        chatWithSuper("Invalid command syntax", super)


def toomin(num, min, super):
    if super is None:
        print '\033[0;31;40m',
        print "The number you have entered (" + str(num) + ") is too small, it must be at least " + str(min),
        print '\033[0m'
    else:
        trystop(super)
        chatWithSuper("The number you have entered (" + str(num) + ") is too small, it must be at least " + str(min), super)


def toomax(num, max, super):
    if super is None:
        print '\033[0;31;40m',
        print "The number you have entered (" + str(num) + ") is too big, it must be at most " + str(max),
        print '\033[0m'
    else:
        trystop(super)
        chatWithSuper("The number you have entered (" + str(num) + ") is too big, it must be at most " + str(max), super)


def getblock(argv, super):
    if argv in blockDictionary.keys():
        return blockDictionary[argv]
    else:
        blockId = toint(argv, 0, 256, super)
        if blockId <= -1:
            return -1


def toint(intStr, min, max, super):
    try:
        res = int(intStr)
        if res < min:
            toomin(res, min, super)
            if min < 0:
                return -257
            return -1
        if res > max:
            toomax(res, max, super)
            if min < 0:
                return -257
            return -1
    except ValueError:
        invalid(super)
        return -1
    return res


def tobool(argv, super):
    if argv == "true":
        return True
    elif argv == "false":
        return False
    else:
        invalid(super)
        return -1


def getvec(x, y, z, isFloat, super):
    if isFloat:
        vec = [0, 0, 0]
        if x.startswith("~"):
            try:
                if len(x) == 1:
                    add = 0
                else:
                    add = float(x[1:])
            except ValueError:
                invalid(super)
                return False
            vec[0] = mc.player.getTilePos().x + add
        else:
            try:
                vec[0] = float(x)
            except ValueError:
                invalid(super)
                return False
        if y.startswith("~"):
            try:
                if len(y) == 1:
                    add = 0
                else:
                    add = float(y[1:])
            except ValueError:
                invalid(super)
                return False
            vec[1] = mc.player.getTilePos().y + add
        else:
            try:
                vec[1] = float(y)
            except ValueError:
                invalid(super)
                return False
        if z.startswith("~"):
            try:
                if len(z) == 1:
                    add = 0
                else:
                    add = float(z[1:])
            except ValueError:
                invalid(super)
                return False
            vec[2] = mc.player.getTilePos().z + add
        else:
            try:
                vec[2] = float(z)
            except ValueError:
                invalid(super)
                return False
    else:
        vec = [0, 0, 0]
        if x[0] == "~":
            try:
                if len(x) == 1:
                    add = 0
                else:
                    add = int(x[1:])
            except ValueError:
                invalid(super)
                return False
            vec[0] = int(mc.player.getTilePos().x) + add
        else:
            try:
                vec[0] = int(x)
            except ValueError:
                invalid(super)
                return False
        if y[0] == "~":
            try:
                if len(y) == 1:
                    add = 0
                else:
                    add = int(y[1:])
            except ValueError:
                invalid(super)
                return False
            vec[1] = int(mc.player.getTilePos().y) + add
        else:
            try:
                vec[1] = int(y)
            except ValueError:
                invalid(super)
                return False
        if z[0] == "~":
            try:
                if len(z) == 1:
                    add = 0
                else:
                    add = int(z[1:])
            except ValueError:
                invalid(super)
                return False
            vec[2] = int(mc.player.getTilePos().z) + add
        else:
            try:
                vec[2] = int(z)
            except ValueError:
                invalid(super)
                return False
    if vec[0] > 128:
        toomax(vec[0], 128, super)
    elif vec[0] < -128:
        toomin(vec[0], -128, super)
    elif vec[1] > 64:
        toomax(vec[1], 64, super)
    elif vec[1] < -64:
        toomin(vec[1], -64, super)
    elif vec[2] > 128:
        toomax(vec[2], 128, super)
    elif vec[2] < -128:
        toomin(vec[2], -128, super)
    else:
        return vec
    return False


def readCommand(command, super=None):
    commandArgs = []
    addingArgv = ""
    for word in command + " ":
        if not (word == " "):
            addingArgv += word
        else:
            commandArgs.append(addingArgv)
            addingArgv = ""
    switchcommand(commandArgs, super)


while True:
    input = raw_input("> ")
    if input == '\x1b':
        for name in threads:
            threads[name].stop()
        if not disablegpio:
            try:
                RPi.GPIO.cleanup()
            except RuntimeWarning:
                pass
        break
    if len(input) == 0:
        continue
    if not (input.find("/") == 0):
        mc.postToChat("<" + playerName + "> " + input)
    else:
        readCommand(input[1:])
